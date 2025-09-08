import math
import random
import numpy as np
from collections import defaultdict, deque
import tensorflow as tf
from tensorflow.keras import layers, Model, optimizers, losses

# ----------------------------
# 1) Minimal Game Interface
# ----------------------------
class Game:
    """
    Required methods to adapt to a new game:
      - initial_state() -> any
      - current_player(state) -> +1 or -1
      - legal_actions(state) -> List[int] (fixed-size action space)
      - step(state, action) -> next_state
      - is_terminal(state) -> bool
      - outcome(state) -> +1 (player 1 win), -1 (player -1 win), 0 (draw)  [only call if terminal]
      - encode(state) -> np.array shaped [H, W, C] (or [features]) for the NN
      - action_size -> int (constant)
    """
    action_size: int
    def initial_state(self): raise NotImplementedError
    def current_player(self, state): raise NotImplementedError
    def legal_actions(self, state): raise NotImplementedError
    def step(self, state, action): raise NotImplementedError
    def is_terminal(self, state): raise NotImplementedError
    def outcome(self, state): raise NotImplementedError
    def encode(self, state): raise NotImplementedError


# ----------------------------
# 2) Example Game: Tic-Tac-Toe
# ----------------------------
class TicTacToe(Game):
    def __init__(self):
        self.n = 3
        self.action_size = self.n * self.n

    def initial_state(self):
        # board values: 1 for player1 (X), -1 for player2 (O), 0 empty
        board = np.zeros((self.n, self.n), dtype=np.int8)
        player = 1
        return (board, player)

    def current_player(self, state):
        _, player = state
        return player

    def legal_actions(self, state):
        board, _ = state
        return [i for i in range(self.action_size) if board[i // self.n, i % self.n] == 0]

    def step(self, state, action):
        board, player = state
        r, c = divmod(action, self.n)
        if board[r, c] != 0:
            raise ValueError("Illegal action")
        next_board = board.copy()
        next_board[r, c] = player
        return (next_board, -player)

    def is_terminal(self, state):
        board, _ = state
        # rows/cols
        lines = []
        lines.extend(list(board))                      # rows
        lines.extend(list(board.T))                    # cols
        # diagonals
        lines.append(np.diag(board))
        lines.append(np.diag(np.fliplr(board)))
        if any(abs(line.sum()) == self.n for line in lines):
            return True
        if not (board == 0).any():
            return True
        return False

    def outcome(self, state):
        board, _ = state
        lines = []
        lines.extend(list(board))
        lines.extend(list(board.T))
        lines.append(np.diag(board))
        lines.append(np.diag(np.fliplr(board)))
        for line in lines:
            s = line.sum()
            if s == self.n:  return +1
            if s == -self.n: return -1
        return 0  # draw

    def encode(self, state):
        # Encode as (3x3x3) planes: [current_player stones, opponent stones, current_player indicator]
        board, player = state
        cur = (board == player).astype(np.float32)
        opp = (board == -player).astype(np.float32)
        turn = np.full_like(cur, 1.0 if player == 1 else 0.0, dtype=np.float32)
        x = np.stack([cur, opp, turn], axis=-1)  # shape (3,3,3)
        return x


# ----------------------------
# 3) Policy + Value Network
# ----------------------------
def build_policy_value_net(input_shape, action_size):
    inp = layers.Input(shape=input_shape)  # e.g., (3,3,3)

    x = layers.Conv2D(64, 3, padding="same", activation="relu")(inp)
    x = layers.Conv2D(64, 3, padding="same", activation="relu")(x)
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation="relu")(x)

    # Policy head
    p = layers.Dense(64, activation="relu")(x)
    p_logits = layers.Dense(action_size)(p)  # unnormalized log-probabilities

    # Value head
    v = layers.Dense(64, activation="relu")(x)
    v_out = layers.Dense(1, activation="tanh")(v)     # in [-1, 1]

    model = Model(inputs=inp, outputs=[p_logits, v_out])
    model.compile(
        optimizer=optimizers.Adam(1e-3),
        loss=[losses.CategoricalCrossentropy(from_logits=True), losses.MeanSquaredError()],
        loss_weights=[1.0, 1.0],
    )
    return model


# ----------------------------
# 4) MCTS (PUCT)
# ----------------------------
class MCTS:
    def __init__(self, game: Game, net: Model, cpuct=1.5, dirichlet_alpha=0.3, dirichlet_frac=0.25):
        self.game = game
        self.net = net
        self.cpuct = cpuct
        self.dirichlet_alpha = dirichlet_alpha
        self.dirichlet_frac = dirichlet_frac

        # Per-state containers (by state key)
        self.P = {}       # prior policy (masked)
        self.N = defaultdict(int)   # visit counts for (s,a)
        self.W = defaultdict(float) # total value for (s,a)
        self.Q = defaultdict(float) # mean value for (s,a)
        self.children = {}          # state_key -> [child_state_keys or None]
        self.legals = {}            # state_key -> legal action list

    def key(self, state):
        # Make a hashable key for dicts
        board, player = state
        return (tuple(board.flatten()), player)

    def policy_value(self, state, legal_actions):
        # NN forward
        x = np.expand_dims(self.game.encode(state), axis=0)
        p_logits, v = self.net.predict(x, verbose=0)
        p = tf.nn.softmax(p_logits[0]).numpy()
        # Mask illegal moves and renormalize
        mask = np.zeros(self.game.action_size, dtype=bool)
        mask[legal_actions] = True
        p = p * mask
        s = p.sum()
        if s > 0:
            p = p / s
        else:
            # all illegal got masked (shouldn't happen), fallback to uniform over legal
            p = mask.astype(np.float32) / mask.sum()
        return p, float(v[0,0])

    def add_dirichlet_noise(self, p, legal_actions):
        noise = np.random.dirichlet([self.dirichlet_alpha] * len(legal_actions))
        p_legal = p[legal_actions]
        p_legal = (1 - self.dirichlet_frac) * p_legal + self.dirichlet_frac * noise
        p = p.copy()
        p[legal_actions] = p_legal
        return p

    def search(self, state, root=False):
        s_key = self.key(state)

        if self.game.is_terminal(state):
            res = self.game.outcome(state)
            return res  # value from current player's perspective

        if s_key not in self.P:
            legal = self.game.legal_actions(state)
            self.legals[s_key] = legal
            p, v = self.policy_value(state, legal)
            if root:
                p = self.add_dirichlet_noise(p, legal)
            self.P[s_key] = p
            self.children[s_key] = [None] * self.game.action_size
            return v

        # Select action with highest PUCT
        legal = self.legals[s_key]
        total_N = sum(self.N[(s_key, a)] for a in legal) + 1e-8
        best_score, best_a = -1e9, None
        for a in legal:
            q = self.Q[(s_key, a)]
            u = self.cpuct * self.P[s_key][a] * math.sqrt(total_N) / (1 + self.N[(s_key, a)])
            score = q + u
            if score > best_score:
                best_score, best_a = score, a

        a = best_a
        # Expand
        if self.children[s_key][a] is None:
            next_state = self.game.step(state, a)
            self.children[s_key][a] = self.key(next_state)
        else:
            # Reconstruct the child state from key lightweight (for simple games we can rebuild)
            next_state = self.state_from_key(self.children[s_key][a], state)

        v = self.search(next_state, root=False)
        # Value from current player's perspective; after a move, perspective flips
        v = -v

        # Backprop
        self.W[(s_key, a)] += v
        self.N[(s_key, a)] += 1
        self.Q[(s_key, a)] = self.W[(s_key, a)] / self.N[(s_key, a)]
        return v

    def state_from_key(self, key, parent_state):
        # For simple games we can rebuild board from key; otherwise store full states.
        board_tuple, player = key
        n = int(math.sqrt(len(board_tuple)))
        board = np.array(board_tuple, dtype=np.int8).reshape(n, n)
        return (board, player)

    def run(self, state, num_simulations=100, temperature=1.0):
        for _ in range(num_simulations):
            self.search(state, root=True)

        s_key = self.key(state)
        legal = self.legals[s_key]
        counts = np.array([self.N[(s_key, a)] for a in range(self.game.action_size)], dtype=np.float32)

        if temperature == 0:
            a = np.argmax(counts)
            pi = np.zeros_like(counts)
            pi[a] = 1.0
        else:
            counts_pow = np.power(counts, 1.0 / temperature)
            if counts_pow.sum() == 0:
                # fallback uniform legal
                pi = np.zeros_like(counts_pow)
                pi[legal] = 1.0 / len(legal)
            else:
                pi = counts_pow / counts_pow.sum()

        return pi


# ----------------------------
# 5) Self-Play and Training
# ----------------------------
class AlphaZero:
    def __init__(self, game: Game, model: Model,
                 sims_per_move=100, temp_moves=6, replay_size=20000, batch_size=128):
        self.game = game
        self.model = model
        self.sims_per_move = sims_per_move
        self.temp_moves = temp_moves
        self.memory = deque(maxlen=replay_size)
        self.batch_size = batch_size

    def self_play_game(self):
        mcts = MCTS(self.game, self.model)
        state = self.game.initial_state()
        history = []  # (encoded_state, pi, player)
        move_count = 0

        while not self.game.is_terminal(state):
            temperature = 1.0 if move_count < self.temp_moves else 0.0
            pi = mcts.run(state, num_simulations=self.sims_per_move, temperature=temperature)
            enc = self.game.encode(state)
            history.append((enc, pi, self.game.current_player(state)))
            # sample action from pi (stochastic early, argmax late)
            action = np.random.choice(np.arange(self.game.action_size), p=pi)
            state = self.game.step(state, action)
            move_count += 1

        z_final = self.game.outcome(state)  # from player +1 perspective
        # Convert to each state's current-player perspective:
        for enc, pi, player in history:
            z = z_final if player == 1 else -z_final
            self.memory.append((enc, pi, z))

    def train_step(self, epochs=1):
        if len(self.memory) < self.batch_size:
            return 0.0, 0.0
        batch = random.sample(self.memory, self.batch_size)
        X = np.stack([s for (s, _, _) in batch], axis=0)
        P = np.stack([p for (_, p, _) in batch], axis=0)
        Z = np.array([z for (_, _, z) in batch], dtype=np.float32).reshape(-1, 1)
        history = self.model.fit(X, [P, Z], batch_size=64, epochs=epochs, verbose=0)
        pol_loss = float(history.history["loss"][0])  # total loss
        return pol_loss, 0.0

    def evaluate(self, games=50):
        # quick sanity: play both sides at temp=0 using current net vs itself
        wins = draws = losses = 0
        for _ in range(games):
            res = self.play_match(temp_moves=0)
            if res == 1: wins += 1
            elif res == 0: draws += 1
            else: losses += 1
        return wins, draws, losses

    def play_match(self, temp_moves=0):
        mcts = MCTS(self.game, self.model)
        state = self.game.initial_state()
        move = 0
        while not self.game.is_terminal(state):
            pi = mcts.run(state, num_simulations=self.sims_per_move, temperature=(1.0 if move < temp_moves else 0.0))
            action = np.argmax(pi)
            state = self.game.step(state, action)
            move += 1
        return self.game.outcome(state)

# ----------------------------
# 6) Wire it up
# ----------------------------
def main():
    game = TicTacToe()
    dummy = game.encode(game.initial_state())  # shape e.g. (3,3,3)
    model = build_policy_value_net(dummy.shape, game.action_size)
    az = AlphaZero(game, model, sims_per_move=60, temp_moves=4, replay_size=5000, batch_size=256)

    # Training loop (tiny demo)
    for it in range(30):  # iterations
        # Generate self-play data
        for _ in range(20):  # games per iteration
            az.self_play_game()

        # Train on accumulated data
        az.train_step(epochs=2)

        # Quick progress print
        w, d, l = az.evaluate(games=10)
        print(f"Iter {it+1:02d}: vs-self W/D/L = {w}/{d}/{l}, replay={len(az.memory)}")

    # Save the trained model
    model.save("tictactoe_alphazero.h5")
    print("Saved model -> tictactoe_alphazero.h5")

if __name__ == "__main__":
    main()