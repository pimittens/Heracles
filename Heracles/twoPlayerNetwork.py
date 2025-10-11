import math
import numpy as np
import tensorflow as tf
import Game
import time
from tensorflow.keras import layers, Model


def build2pModel(inputDim=1770, numMoves=512):
    inputs = tf.keras.Input(shape=(inputDim,), name="observation")

    # shared body (feature extractor)
    x = layers.Dense(1024, activation='relu')(inputs)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dense(256, activation='relu')(x)

    # policy head
    policyLogits = layers.Dense(numMoves, activation=None, name="policy")(x)

    # value head
    value_hidden = layers.Dense(128, activation='relu')(x)
    value = layers.Dense(1, activation='tanh', name="value")(value_hidden)

    model = Model(inputs=inputs, outputs=[policyLogits, value], name="AlphaZeroModel")

    # optional compilation for supervised pretraining or testing
    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-4),
        loss={
            "policy": tf.keras.losses.CategoricalCrossentropy(from_logits=True),
            "value": tf.keras.losses.MeanSquaredError(),
        },
        loss_weights={"policy": 1.0, "value": 1.0},
    )

    return model


# model = build2pModel(input_dim=1765, num_moves=512)
# model.summary()

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # BoardState object
        self.parent = parent
        self.children = {}  # move → child Node
        self.P = {}  # move → prior prob from NN
        self.N = {}  # move → visit count
        self.W = {}  # move → total value
        self.value = 0.0  # value predicted by NN for this state
        self.player = state.getOptions()[0][1]  # player currently making a move

    def is_expanded(self):
        return len(self.P) > 0

    def Q(self, move):
        if self.N[move] == 0:
            return 0.0
        return self.W[move] / self.N[move]

    def select(self, c_puct):
        """Selects move using UCB (Upper Confidence Bound)"""
        total_N = sum(self.N.values()) + 1e-8
        best_move, best_score = None, -float('inf')

        for move in self.P.keys():
            q = self.Q(move)
            u = c_puct * self.P[move] * math.sqrt(total_N) / (1 + self.N[move])
            score = q + u
            if score > best_score:
                best_score, best_move = score, move

        return best_move


class NeuralMCTS:
    def __init__(self, model, c_puct=1.4, num_simulations=10):
        self.model = model
        self.c_puct = c_puct
        self.num_simulations = num_simulations

    def masked_softmax(self, logits, legal_moves):
        """Softmax over only the legal moves."""
        logits = np.array(logits).squeeze()
        # take only first len(legal_moves) logits (or random subset)
        logits = logits[:len(legal_moves)]
        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / np.sum(exp_logits)
        return probs

    def predict(self, state):
        """Run the NN to get policy logits and value."""
        obs = np.array(state.observation(), dtype=np.float32)[np.newaxis, :]
        logits, value = self.model.predict(obs, verbose=0)
        return logits.squeeze(), float(value)

    def expand(self, node):
        """Expand node using NN priors."""
        state = node.state
        legal_moves = state.getOptions()

        logits, value = self.predict(state)
        priors = self.masked_softmax(logits, legal_moves)

        # store priors in dictionaries keyed by move objects
        for move, p in zip(legal_moves, priors):
            node.P[move] = p
            node.N[move] = 0
            node.W[move] = 0.0

        node.value = value
        return value

    def run(self, root_state):
        root = self.simulate(root_state)
        move_visits = np.array([root.N.get(m, 0) for m in root.P.keys()])
        policy = move_visits / np.sum(move_visits)
        return policy

    def simulate(self, root_state):
        root = Node(root_state)
        for _ in range(self.num_simulations):
            node = root

            # 1. Selection
            while node.is_expanded() and not node.state.isOver():
                move = node.select(self.c_puct)
                node = node.children.get(move) or self.create_child(node, move)

            # 2. Expansion
            if not node.state.isOver():
                value = self.expand(node)
            else:
                # Terminal node value based on game result
                winners = node.state.getWinners()
                if sum(winners) > 1:
                    value = 0  # tie
                else:
                    value = winners[node.player]

            # 3. Backpropagation
            self.backpropagate(node, value)
        return root

    def create_child(self, parent, move):
        child_state = parent.state.copyState()
        child_state.makeMove(move)
        child = Node(child_state, parent)
        parent.children[move] = child
        return child

    def backpropagate(self, node, value):
        """Propagate value back up the tree."""
        last_player = node.player
        while node.parent is not None:
            parent = node.parent
            # Find which move led to this node
            for move, child in parent.children.items():
                if child is node:
                    parent.W[move] += value
                    parent.N[move] += 1
                    break
            # Flip value for the opponent’s perspective
            if parent.player != last_player:
                value = -value
                last_player = parent.player
            node = parent


def self_play_game(model, num_simulations=50):
    mcts = NeuralMCTS(model, num_simulations=num_simulations)
    states, policies, players = [], [], []
    module = np.random.choice(range(3))
    state = Game.LoggingBoardState([Game.Player(0, True, module), Game.Player(1, True, module)], True, module,
                                   False)  # start new game
    state.startLogging()
    while not state.isOver():
        root = mcts.simulate(state.copyState())

        # Extract policy proportional to visit counts
        legal_moves = list(root.P.keys())
        visits = np.array([root.N[m] for m in legal_moves], dtype=np.float32)
        policy = visits / np.sum(visits)

        # Store training data
        states.append(state.observation())
        policies.append((legal_moves, policy))
        players.append(state.getOptions()[0][1])

        # Choose move (stochastic for training)
        selection = np.random.choice(len(legal_moves), p=policy)
        state.makeMove(state.getOptions()[selection])
    state.endLogging()

    # Once game ends
    winners = state.getWinners()
    tie = sum(winners) > 1

    # Create training tuples
    data = []
    for obs, (moves, policy), player in zip(states, policies, players):
        if tie:
            value = 0
        else:
            value = winners[player] * 2 - 1  # convert 1/0 to +1/-1
        data.append((obs, moves, policy, value))

    return data


def train(model, num_iterations, num_games_per_iteration):
    startTime = time.time()
    for iteration in range(num_iterations):
        iterationStartTime = time.time()
        all_data = []

        print("generating self play data")

        # 1. Generate self-play data
        for i in range(num_games_per_iteration):
            gameStartTime = time.time()
            data = self_play_game(model)
            print(f"finished game {i} of {num_games_per_iteration} in {(time.time() - gameStartTime) / 60} minutes")
            all_data.extend(data)

        # 2. Prepare batches for training
        X = np.array([d[0] for d in all_data])  # observations
        y_policy = np.array([d[2] for d in all_data])  # policy distributions
        y_value = np.array([d[3] for d in all_data])  # scalar values

        # 3. Train model
        model.fit(X, [y_policy, y_value],
                  batch_size=64,
                  epochs=5,
                  verbose=1)

        # Optionally: save model, evaluate against previous versions
        model.save(f"model_iter_{iteration}.h5")

        print(f"finished iteration {iteration} of {num_iterations} in {(time.time() - iterationStartTime) / 60} minutes")


train(build2pModel(), 5, 5)
