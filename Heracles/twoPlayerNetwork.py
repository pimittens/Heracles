import math
import random
import numpy as np
import tensorflow as tf
import pickle
import Game
import time
from tensorflow.keras import layers, Model
from multiprocessing import Pool, freeze_support
from keras.src.saving import load_model


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

        if self.state.getOptions()[0][0] == Game.Move.ROLL:
            # do random die rolls
            roll = random.choice(range(0, 6))
            i = 0
            for move in self.state.getOptions():
                i += move[2][1]
                if roll < i:
                    return move

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
    def __init__(self, model, c_puct=1.4, num_simulations=50):
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
        startTime = time.time()
        root = self.simulate(root_state.copyState())
        move_visits = np.array([root.N.get(m, 0) for m in root.P.keys()])
        policy = move_visits / np.sum(move_visits)
        if root_state.loggingEnabled:
            root_state.log.write("mcts (with neural network) results\n")
            for move in root.children.keys():
                root_state.log.write(
                    f"Move: {move}, prior: {root.P[move]}, visits:{root.N[move]}, Q value: {root.Q(move)}\n")
            root_state.log.write("move order:\n")
            for option in root_state.getOptions():
                root_state.log.write(f"{option}\n")
            root_state.log.write(f"policy:\n{policy}\n")
            root_state.log.write(f"time elapsed: {time.time() - startTime} seconds\n")
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


def self_play_game(model, game_num, num_simulations=50):
    mcts = NeuralMCTS(model, num_simulations=num_simulations)
    states, policies, players = [], [], []
    module = np.random.choice(range(3))
    state = Game.LoggingBoardState([Game.Player(0, True, module), Game.Player(1, True, module)], True, module,
                                   False)  # start new game
    state.startLogging(game_num)
    while not state.isOver():
        options = state.getOptions()
        if len(options) == 1:
            state.makeMove(options[0])
            continue
        elif options[0][0] == Game.Move.ROLL:
            state.makeMove(options[len(options) - 1])  # random roll
            continue

        policy = mcts.run(state)

        # Store training data
        states.append(state.observation())
        policies.append((options, policy))
        players.append(state.getOptions()[0][1])

        # Choose move (stochastic for training)
        selection = np.random.choice(len(options), p=policy)
        state.makeMove(options[selection])
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
        policy_full = np.zeros(
            512)  # max number of possible legal moves, ensure all policy vectors are padded to this length
        option_to_index = {m: i for i, m in enumerate(state.getOptions())}
        for move, prob in zip(moves, policy):
            if move in option_to_index:
                policy_full[option_to_index[move]] = prob
        data.append((obs, policy_full, value))
    return data


def worker_play(iteration, game_num):
    if iteration == -1:
        model = build2pModel()
        return self_play_game(model)
    model = load_model(f"model_iter_{iteration}.keras")
    return self_play_game(model, game_num)


def train(initial_iteration, num_iterations, num_games_per_iteration):
    start = time.time()
    if initial_iteration == -1:
        model = build2pModel()
        all_data = []
    else:
        model = load_model(f"model_iter_{initial_iteration}.keras")
        with open(f"replay/replay_{initial_iteration}.pkl", "rb") as f:
            all_data = pickle.load(f)
    for iteration in range(num_iterations):
        print(f"begin iteration {iteration + initial_iteration + 1}")
        iterationStartTime = time.time()

        print("generating self play data")

        # Generate self-play data
        for i in range(num_games_per_iteration // 4):
            gameStartTime = time.time()
            with Pool(processes=4) as p:
                results = p.starmap(worker_play, [(iteration + initial_iteration, iteration + initial_iteration + (i * 4) + j) for j in [0, 1, 2, 3]])
            print(
                f"finished games {i * 4 + 1} through {i * 4 + 4} of {num_games_per_iteration} in {(time.time() - gameStartTime) / 60} minutes")
            for result in results:
                all_data.extend(result)

        # Prepare batches for training
        if len(all_data) > 8192:
            batch = random.sample(all_data, 8192)
        else:
            batch = all_data
        X = np.array([d[0] for d in batch])  # observations
        y_policy = np.array([d[1] for d in batch])  # policy distributions
        y_value = np.array([d[2] for d in batch])  # scalar values

        # Train model
        model.fit(X, [y_policy, y_value],
                  batch_size=64,
                  epochs=3,
                  verbose=1)

        # Save model
        model.save(f"model_iter_{iteration + initial_iteration + 1}.keras")
        with open(f"replay/replay_{iteration + initial_iteration + 1}.pkl", "wb") as f:
            pickle.dump(all_data, f)

        print(
            f"finished iteration {iteration + initial_iteration + 1} of {num_iterations} in {(time.time() - iterationStartTime) / 60} minutes")

    print(f"finished training in {(time.time() - start) / 3600} hours")


if __name__ == "__main__":
    freeze_support()
    train(0, 2, 8)
