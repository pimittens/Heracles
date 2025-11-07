import torch
import torch.nn as nn
import random
import Game
import math
import pickle
from collections import deque


class TwoPlayerNetwork(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Tanh()  # output in [-1, 1]
        )

    def forward(self, x):
        return self.net(x)


class MCTSNode:
    def __init__(self, state, move=None):
        self.state = state
        self.move = move
        self.player = move[1] if move else -1  # whose turn it was to move at this node
        self.children = {}
        self.N = 0
        self.W = 0.0  # total value
        self.Q = 0.0  # mean value


def mcts_search(root_state, model, num_simulations=100):
    root = MCTSNode(root_state)
    num_legal_moves = len(root_state.getOptions())
    if 10 < num_legal_moves < 50:
        num_simulations *= 3
    elif num_legal_moves >= 50 or root_state.getOptions()[0][0] == Game.Move.CHOOSE_BUY_FACES:
        num_simulations *= 6
    for _ in range(num_simulations):
        node = root
        path = [node]
        # SELECTION
        while node.children and not node.state.isOver():
            node = select_child(node)
            path.append(node)

        # EXPANSION
        if not node.state.isOver():
            legal_moves = node.state.getOptions()
            for move in legal_moves:
                if move[0] == Game.Move.RANDOM_ROLL:
                    continue
                next_state = node.state.copyState()
                next_state.makeMove(move)
                node.children[move] = MCTSNode(next_state, move)
            node = random.choice(list(node.children.values()))
            path.append(node)

        # EVALUATION (via neural network)
        if node.state.isOver():
            if sum(node.state.getWinners()) > 1:
                value = 0 # zero value for draws
            else:
                value = node.state.getWinners()[node.player]
        else:
            encoded = torch.tensor(node.state.observation()).unsqueeze(0)
            with torch.no_grad():
                value = model(encoded).item()

        # BACKPROPAGATION
        for n in reversed(path):
            n.N += 1
            n.W += value if node.player == n.player else -value
            n.Q = n.W / n.N

    # Choose move with highest visit count
    choice, _ = max(root.children.items(), key=lambda kv: kv[1].N)
    if root_state.printingEnabled:
        print("mcts (with neural net evaluation) results")
        for move, node in root.children.items():
            print(
                f"Move: {move}, visits:{node.N}, average points: {node.Q}")
        # print(f"time elapsed: {time.time() - startTime} seconds")
    if root_state.loggingEnabled:
        root_state.log.write("mcts (with neural net evaluation) results\n")
        for move, node in root.children.items():
            root_state.log.write(
                f"Move: {move}, visits:{node.N}, average points: {node.Q}\n")
        # root_state.log.write(f"time elapsed: {time.time() - startTime} seconds\n")
    return choice


def select_child(node, c_puct=1.4):
    if next(iter(node.children.keys()))[0] == Game.Move.CHOOSE_RESOLVE_ORDER:
        # don't bother with resolve order nodes since they hardly ever matter
        for move, child in node.children.items():
            return child
    if next(iter(node.children.keys()))[0] == Game.Move.ROLL:
        roll = random.choice(range(0, 6))
        i = 0
        for move, child in node.children.items():
            i += move[2][1]
            if roll < i:
                return child
    total_N = sum(child.N for child in node.children.values()) + 1e-6
    best_score, best_child = -1e9, None
    for move, child in node.children.items():
        ucb = child.Q + c_puct * math.sqrt(math.log(total_N) / (child.N + 1))
        if ucb > best_score:
            best_score, best_child = ucb, child
    return best_child


def self_play(model, num_games=9):
    dataset = []
    for g in range(num_games):
        players = [Game.Player(0, None, g % 3), Game.Player(1, None, g % 3)]
        env = Game.LoggingBoardState(players, True, g % 3, False)
        env.startLogging()
        states = []
        while not env.isOver():
            options = env.getOptions()
            if options[0][0] == Game.Move.ROLL:
                env.makeMove(options[len(options) - 1])
                continue
            if options[0][0] == Game.Move.CHOOSE_RESOLVE_ORDER:
                env.makeMove(random.choice(options)) # pick random resolve order since it rarely matters
                continue
            s = env.observation()
            if len(options) == 1:
                move = options[0]
            else:
                move = mcts_search(env, model, num_simulations=200)
            states.append((s, env.getOptions()[0][1]))
            env.makeMove(move)

        env.endLogging()

        # Game result for each player
        results = env.getWinners()  # list of values per player, e.g. +1/-1
        for s, player in states:
            dataset.append((s, results[player]))
        print(f"finished game {g + 1} of {num_games}")
    return dataset


def train_value_net(model, data, optimizer, epochs=10, batch_size=64, device=None, ):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    start_epoch = 0

    # --- Prepare data ---
    states, targets = zip(*data)  # list of (state_tensor, value)
    states = [torch.as_tensor(s, dtype=torch.float32) for s in states]
    states = torch.stack(states).to(device)
    targets = torch.tensor(targets, dtype=torch.float32).unsqueeze(1).to(device)

    loss_fn = nn.MSELoss()

    for epoch in range(start_epoch, epochs):
        model.train()

        # Shuffle each epoch
        perm = torch.randperm(states.size(0))
        states, targets = states[perm], targets[perm]

        total_loss = 0.0
        for i in range(0, len(states), batch_size):
            batch_states = states[i: i + batch_size]
            batch_targets = targets[i: i + batch_size]

            preds = model(batch_states)
            loss = loss_fn(preds, batch_targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / (len(states) / batch_size)
        print(f"Epoch {epoch + 1}/{epochs} — Loss: {avg_loss:.4f}")

    print("Training complete.")


if __name__ == "__main__":
    try:
        with open("replay_buffer.pkl", "rb") as f:
            replay_buffer = deque(pickle.load(f), maxlen=50000)
    except FileNotFoundError:
        replay_buffer = deque(maxlen=50000)

    model = TwoPlayerNetwork(input_size=1770)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    # Try to load previous progress
    try:
        ckpt = torch.load("checkpoint.pt")
        model.load_state_dict(ckpt["model_state"])
        optimizer.load_state_dict(ckpt["optimizer_state"])
        start_iter = ckpt["iteration"] + 1
        print(f"Resumed from iteration {start_iter}")
    except FileNotFoundError:
        start_iter = 0
        print("Starting fresh")

    # Main loop
    for iteration in range(start_iter, 201):
        print(f"begin iteration {iteration}")
        data = self_play(model, num_games=9)
        replay_buffer.extend(data)

        for _ in range(20):  # number of training batches per iteration
            batch = random.sample(replay_buffer, k=128)
            train_value_net(model, batch, optimizer, epochs=1)

        torch.save({
            "model_state": model.state_dict(),
            "optimizer_state": optimizer.state_dict(),
            "iteration": iteration,
        }, "checkpoint.pt")

        if iteration % 20 == 0:
            torch.save({
                "model_state": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "iteration": iteration,
            }, f"checkpoint_{iteration}.pt")

        with open("replay_buffer.pkl", "wb") as f:
            pickle.dump(list(replay_buffer), f)
