import random
import math
import Data
import Game
import time
import numpy as np


class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.points = 0

    def isTerminalNode(self):
        return self.state.isOver()

    def isFullyExpanded(self):
        if self.children and self.children[0].move[0] == Game.Move.ROLL:
            return True
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
        if self.children[0].move[0] == Game.Move.ROLL:
            roll = random.choice(range(0, 6))
            i = 0
            for child in self.children:
                i += child.move[2][1]
                if roll < i:
                    return child
        choicesWeights = [
            (child.points / child.visits) + explorationWeight * math.sqrt(
                math.log(self.visits) / child.visits
            )
            for child in self.children
        ]
        return self.children[choicesWeights.index(max(choicesWeights))]

    def mostVisitedChild(self):
        visits = [child.visits for child in self.children]
        return self.children[visits.index(max(visits))]

    def expand(self):
        tried = [child.move for child in self.children]
        options = self.state.getOptions()
        if options[0][0] == Game.Move.ROLL:
            for move in options:
                if move[0] == Game.Move.ROLL:
                    nextState = self.state.copyState()
                    nextState.makeMove(move)
                    childNode = Node(nextState, self, move)
                    self.children.append(childNode)
            return self.bestChild()
        for move in options:
            if move not in tried:
                nextState = self.state.copyState()
                nextState.makeMove(move)
                childNode = Node(nextState, self, move)
                self.children.append(childNode)
                return childNode
        print(options)  # shouldn't ever get here unless something is wrong
        self.state.printBoardState()

    def backpropagate(self, result):
        self.visits += 1
        self.points += result[self.state.lastPlayer]
        if self.parent:
            self.parent.backpropagate(result)


class HeuristicNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.points = 0

    def isTerminalNode(self):
        return self.state.isOver()

    def isFullyExpanded(self):
        if self.children and self.children[0].move[0] == Game.Move.ROLL:
            return True
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
        if self.children[0].move[0] == Game.Move.ROLL:
            roll = random.choice(range(0, 6))
            i = 0
            for child in self.children:
                i += child.move[2][1]
                if roll < i:
                    return child
        if self.children[0].move[0] == Game.Move.CHOOSE_BUY_FACES and (self.state.round == 1 or (
                self.state.round < 4 and self.state.players[self.children[0].move[1]].gold >= 8)):
            # buy faces early if player has a lot of gold
            return self.children[0]
        elif self.children[0].move[0] == Game.Move.BUY_FACES and len(self.children) > 5:
            # don't consider face buys which don't spend most of current gold
            gold = self.state.players[self.children[0].move[1]].gold
            if self.state.round > 3:
                gold -= 1
            choicesWeights = []
            for child in self.children:
                if child.move[0] != Game.Move.BUY_FACES or Data.getTotalGoldCost(child.move[2]) < gold:
                    choicesWeights.append(0)
                else:
                    choicesWeights.append((child.points / child.visits) + explorationWeight * math.sqrt(
                        math.log(self.visits) / child.visits
                    ))
            if max(choicesWeights) > 0:
                return self.children[choicesWeights.index(max(choicesWeights))]
        elif self.children[0].move[0] == Game.Move.FORGE_FACE:
            # prioritize forging over gold 1 faces
            choicesWeights = []
            for child in self.children:
                if child.move[0] == Game.Move.FORGE_FACE and child.move[2][2] == Data.DieFace.GOLD1:
                    choicesWeights.append((child.points / child.visits) + explorationWeight * math.sqrt(
                        math.log(self.visits) / child.visits
                    ))
                else:
                    choicesWeights.append(0)
            if max(choicesWeights) > 0:
                return self.children[choicesWeights.index(max(choicesWeights))]
        choicesWeights = [
            (child.points / child.visits) + explorationWeight * math.sqrt(
                math.log(self.visits) / child.visits
            )
            for child in self.children
        ]
        return self.children[choicesWeights.index(max(choicesWeights))]

    def mostVisitedChild(self):
        visits = [child.visits for child in self.children]
        return self.children[visits.index(max(visits))]

    def expand(self):
        tried = [child.move for child in self.children]
        options = self.state.getOptions()
        if options[0][0] == Game.Move.ROLL:
            for move in options:
                if move[0] == Game.Move.ROLL:
                    nextState = self.state.copyState()
                    nextState.makeMove(move)
                    childNode = HeuristicNode(nextState, self, move)
                    self.children.append(childNode)
            return self.bestChild()
        for move in options:
            if move not in tried:
                nextState = self.state.copyState()
                nextState.makeMove(move)
                childNode = HeuristicNode(nextState, self, move)
                self.children.append(childNode)
                return childNode
        print(options)  # shouldn't ever get here unless something is wrong
        self.state.printBoardState()

    def backpropagate(self, result):
        self.visits += 1
        self.points += result[self.state.lastPlayer]
        if self.parent:
            self.parent.backpropagate(result)


class EvalNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.points = 0

    def isTerminalNode(self):
        return self.state.isOver()

    def isFullyExpanded(self):
        if self.children and self.children[0].move[0] == Game.Move.ROLL:
            return True
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
        if self.children[0].move[0] == Game.Move.ROLL:
            roll = random.choice(range(0, 6))
            i = 0
            for child in self.children:
                i += child.move[2][1]
                if roll < i:
                    return child
        elif self.children[0].move[0] == Game.Move.BUY_FACES and len(self.children) > 15:
            # don't consider face buys which don't spend most of current gold
            gold = self.state.players[self.children[0].move[1]].gold
            if self.state.round > 3:
                gold -= 1
            choicesWeights = []
            for child in self.children:
                if child.move[0] != Game.Move.BUY_FACES or Data.getTotalGoldCost(child.move[2]) < gold:
                    choicesWeights.append(0)
                else:
                    choicesWeights.append((child.points / child.visits) + explorationWeight * math.sqrt(
                        math.log(self.visits) / child.visits
                    ))
            if max(choicesWeights) > 0:
                return self.children[choicesWeights.index(max(choicesWeights))]
        elif self.children[0].move[0] == Game.Move.FORGE_FACE:
            # prioritize forging over gold 1 faces
            choicesWeights = []
            for child in self.children:
                if child.move[0] == Game.Move.FORGE_FACE and child.move[2][2] == Data.DieFace.GOLD1:
                    choicesWeights.append((child.points / child.visits) + explorationWeight * math.sqrt(
                        math.log(self.visits) / child.visits
                    ))
                else:
                    choicesWeights.append(0)
            if max(choicesWeights) > 0:
                return self.children[choicesWeights.index(max(choicesWeights))]
        choicesWeights = [
            (child.points / child.visits) + explorationWeight * math.sqrt(
                math.log(self.visits) / child.visits
            )
            for child in self.children
        ]
        return self.children[choicesWeights.index(max(choicesWeights))]

    def mostVisitedChild(self):
        visits = [child.visits for child in self.children]
        return self.children[visits.index(max(visits))]

    def expand(self):
        tried = [child.move for child in self.children]
        options = self.state.getOptions()
        if options[0][0] == Game.Move.ROLL:
            for move in options:
                if move[0] == Game.Move.ROLL:
                    nextState = self.state.copyState()
                    nextState.makeMove(move)
                    childNode = EvalNode(nextState, self, move)
                    self.children.append(childNode)
            return self.bestChild()
        for move in options:
            if move not in tried:
                nextState = self.state.copyState()
                nextState.makeMove(move)
                childNode = EvalNode(nextState, self, move)
                self.children.append(childNode)
                return childNode
        print(options)  # shouldn't ever get here unless something is wrong
        self.state.printBoardState()

    def backpropagate(self, result):
        self.visits += 1
        self.points += result[self.state.lastPlayer]
        if self.parent:
            self.parent.backpropagate(result)


"""
class TicTacToeState:
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.lastPlayer = 2

    def copyState(self):
        newBoard = TicTacToeState()
        newBoard.board = copy.deepcopy(self.board)
        newBoard.lastPlayer = self.lastPlayer
        return newBoard

    def makeMove(self, move):
        if self.lastPlayer == 1:
            self.board[move // 3][move % 3] = 2
            self.lastPlayer = 2
        else:
            self.board[move // 3][move % 3] = 1
            self.lastPlayer = 1

    def getOptions(self):
        ret = []
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if self.board[i][j] == 0:
                    ret.append(3 * i + j)
                j += 1
            i += 1
        return ret

    def isOver(self):
        if self.board[0][0] > 0:
            if ((self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2])
                    or (self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0])):
                return  self.board[0][0]
        if self.board[1][1] > 0:
            if ((self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2])
                    or (self.board[1][1] == self.board[0][1] and self.board[1][1] == self.board[2][1])
                    or (self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0])
                    or (self.board[1][1] == self.board[1][0] and self.board[1][1] == self.board[1][2])):
                return  self.board[1][1]
        if self.board[2][2] > 0:
            if ((self.board[2][2] == self.board[2][0] and self.board[2][2] == self.board[2][1])
                    or (self.board[2][2] == self.board[0][2] and self.board[2][2] == self.board[1][2])):
                return  self.board[2][2]
        if not self.getOptions():
            return 3 # draw
        return 0

    def getPoints(self):
        result = self.isOver()
        if result == 1:
            return [1,-1]
        if result == 2:
            return [-1,1]
        return [0,0]

    def printBoard(self):
        print(f"{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}")
        print(f"{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}")
        print(f"{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}")
"""


def evaluate(state, weights):
    if state.isOver():
        scores = state.getWinners()
    else:
        scores = [scorePlayer(p, weights[p.playerID]) for p in state.players]
    total = sum(scores)
    return [score / total for score in scores]


def scorePlayer(player, weights):
    score = max(player.vp + Data.getAllegiancePoints(player.allegiance), 0) * weights[0]
    score += math.sqrt(player.gold) * weights[1]
    score += math.sqrt(player.sun) * weights[2]
    score += math.sqrt(player.moon) * weights[3]
    score += math.sqrt(player.ancientShards) * weights[4]
    for face in player.die1.faces:
        score += weights[5 + face.value]
    for face in player.die2.faces:
        score += weights[5 + face.value]
    for feat in player.feats:
        score += weights[5 + len(Data.DieFace) + feat.value]
    score += sum(player.scepters) * weights[len(weights) - 1]
    return max(score, 1)  # force nonzero


def geneticAlgorithm(populationSize, generations, mutationRate, mutationStd):
    startTime = time.time()
    population = loadPopulation()
    #population = [np.random.uniform(0, 10, size=6 + len(Data.DieFace) + len(Data.HeroicFeat)) for _ in
    #              range(populationSize)]
    for gen in range(generations):
        fitness = evaluateFitness(population)

        # select parents (top 20%)
        sortedPop = [w for _, w in sorted(zip(fitness, population), key=lambda x: x[0], reverse=True)]
        parents = sortedPop[:populationSize // 5]

        # generate new children
        newPopulation = parents.copy()
        while len(newPopulation) < populationSize:
            p1, p2 = random.sample(parents, 2)
            alpha = np.random.rand()
            child = alpha * p1 + (1 - alpha) * p2

            # mutate
            if np.random.rand() < mutationRate:
                child += np.random.normal(0, mutationStd, size=6 + len(Data.DieFace) + len(Data.HeroicFeat))

            newPopulation.append(child)

        population = newPopulation
        print(f"Gen {gen}: best fitness = {max(fitness):.3f}, time elapsed: {(time.time() - startTime) / 60} minutes")
        print(f"previous generation with fitnesses: {sorted(zip(fitness, population), key=lambda x: x[0], reverse=True)}")
        savePopulation(population, gen)


def savePopulation(population, generation):
    save = open("population.txt", "w")
    save.write(f"generation {generation}\n")
    for individual in population:
        for i in range(len(individual)):
            save.write(f"{individual[i]}")
            if i < len(individual) - 1:
                save.write(", ")
        save.write("\n")
    save.close()

def loadPopulation():
    population = []
    save = open("population.txt", "r")
    contents = save.read()
    contents = contents.split("\n")
    for line in contents:
        if "generation" in line or not line:
            continue
        population.append(np.fromstring(line, dtype=float, sep=", "))
    save.close()
    return population


def evaluateFitness(players):
    numPlayers = len(players)
    wins = np.zeros(numPlayers)
    game = 1
    totalGames = numPlayers * (numPlayers - 1) // 2
    i = 0
    while i < numPlayers - 1:
        j = i + 1
        while j < numPlayers:
            p0 = random.choice([True, False])
            if p0:
                startTime = time.time()
                result = playGame(players[i], players[j])
                print(f"game {game} out of {totalGames} completed in {(time.time() - startTime) / 60} minutes")
                game += 1
                if result[0]:
                    wins[i] += 1
                if result[1]:
                    wins[j] += 1
            else:
                startTime = time.time()
                result = playGame(players[j], players[i])
                print(f"game {game} out of {totalGames} completed in {(time.time() - startTime) / 60} minutes")
                game += 1
                if result[0]:
                    wins[j] += 1
                if result[1]:
                    wins[i] += 1
            j += 1
        i += 1
    return wins


def playGame(p0Weights, p1Weights):
    module = random.choice(range(3))
    players = [Game.Player(0, True, module), Game.Player(1, True, module)]
    state = Game.LoggingBoardState(players, True, module, False)
    state.startLogging()
    while not state.isOver():
        options = state.getOptions()
        if options[0][0] == Game.Move.ROLL:
            state.makeMove(options[len(options) - 1])  # always do random roll
        elif len(options) == 1:
            state.makeMove(options[0])
        else:
            move = mctsWithBoardEval(state, 500, (p0Weights, p1Weights))
            state.makeMove(move)
    state.endLogging()
    return state.getWinners()


def mcts(rootState, numSims):
    startTime = time.time()
    root = Node(rootState.copyState())
    if len(root.state.getOptions()) == 1:
        return root.state.getOptions()[0]
    if root.state.getOptions()[0][0] == Game.Move.CHOOSE_RESOLVE_ORDER:
        sims = max(numSims // 100, 100)
    else:
        sims = numSims
    for _ in range(sims):
        node = root
        # selection
        while node.isFullyExpanded() and node.children:
            node = node.bestChild()
        # expansion
        if not node.isTerminalNode():
            node = node.expand()
        # simulation
        result = rollout(node.state)
        # backpropagation
        node.backpropagate(result)
    if rootState.printingEnabled:
        print("mcts results")
        for node in root.children:
            print(
                f"Move: {node.move}, visits:{node.visits}, win probability: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}")
        print(f"time elapsed: {time.time() - startTime} seconds")
    if rootState.loggingEnabled:
        rootState.log.write("mcts (with heuristic) results\n")
        for node in root.children:
            rootState.log.write(
                f"Move: {node.move}, visits:{node.visits}, win probability: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}\n")
        rootState.log.write(f"time elapsed: {time.time() - startTime} seconds\n")
    return root.mostVisitedChild().move


def mctsWithHeuristic(rootState, numSims):
    startTime = time.time()
    root = HeuristicNode(rootState.copyState())
    if len(root.state.getOptions()) == 1:
        return root.state.getOptions()[0]
    if root.state.getOptions()[0][0] == Game.Move.CHOOSE_RESOLVE_ORDER:
        sims = max(numSims // 100, 100)
    else:
        sims = numSims
    for _ in range(sims):
        node = root
        # selection
        while node.isFullyExpanded() and node.children:
            node = node.bestChild()
        # expansion
        if not node.isTerminalNode():
            node = node.expand()
        # simulation
        result = rollout(node.state)
        # backpropagation
        node.backpropagate(result)
    if rootState.printingEnabled:
        print("mcts (with heuristic) results")
        for node in root.children:
            print(
                f"Move: {node.move}, visits:{node.visits}, win probability: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}")
        print(f"time elapsed: {time.time() - startTime} seconds")
    if rootState.loggingEnabled:
        rootState.log.write("mcts (with heuristic) results\n")
        for node in root.children:
            rootState.log.write(
                f"Move: {node.move}, visits:{node.visits}, win probability: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}\n")
        rootState.log.write(f"time elapsed: {time.time() - startTime} seconds\n")
    return root.mostVisitedChild().move


def mctsWithBoardEval(rootState, numSims, weights):
    startTime = time.time()
    root = EvalNode(rootState.copyState())
    if len(root.state.getOptions()) == 1:
        return root.state.getOptions()[0]
    if root.state.getOptions()[0][0] == Game.Move.CHOOSE_RESOLVE_ORDER:
        sims = max(numSims // 100, 100)
    else:
        sims = numSims
    for _ in range(sims):
        node = root
        # selection
        while node.isFullyExpanded() and node.children:
            node = node.bestChild()
        # expansion
        if not node.isTerminalNode():
            node = node.expand()
        # simulation
        result = evaluate(node.state, weights)
        # backpropagation
        node.backpropagate(result)
    if rootState.printingEnabled:
        print("mcts (with board eval) results")
        for node in root.children:
            print(
                f"Move: {node.move}, visits:{node.visits}, score: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}")
        print(f"time elapsed: {time.time() - startTime} seconds")
    if rootState.loggingEnabled:
        rootState.log.write("mcts (with board eval) results\n")
        for node in root.children:
            rootState.log.write(
                f"Move: {node.move}, visits:{node.visits}, score: {node.points / node.visits}, lastPlayer: {node.state.lastPlayer}\n")
        rootState.log.write(f"time elapsed: {time.time() - startTime} seconds\n")
    return root.mostVisitedChild().move


def rollout(state):
    currentState = state.copyState()
    # i = 0
    # if not os.path.exists("logs"):
    #    os.makedirs("logs")
    # if os.path.exists("logs/rollout.txt"):
    #    os.remove("logs/rollout.txt")
    # log = open("logs/rollout.txt", "a")
    # log.write("Begin rollout\n")
    while not currentState.isOver():
        possibleMoves = currentState.getOptions()
        if possibleMoves[0][0] == Game.Move.ROLL:
            currentState.makeMove(possibleMoves[len(possibleMoves) - 1])  # random roll
            continue
        # log.write(f"phase: {currentState.phase}, options: {possibleMoves}\n")
        # log.write(f"activeplayer gold: {currentState.players[currentState.activePlayer].gold}, sun: {currentState.players[currentState.activePlayer].sun}, moon: {currentState.players[currentState.activePlayer].moon}, goldToSpend: {currentState.players[currentState.activePlayer].goldToSpend}, sunToSpend: {currentState.players[currentState.activePlayer].sunToSpend}, moonToSpend: {currentState.players[currentState.activePlayer].moonToSpend}\n")
        # for scepter in currentState.players[currentState.activePlayer].scepters:
        #    log.write(f"scepter: {scepter}\n")
        # if not possibleMoves:
        #    log.close()
        move = random.choice(possibleMoves)
        # log.write(f"making move: {move}\n")
        currentState.makeMove(move)
        # i += 1
        # if i > 4990: # this is just for testing
        # print(f"phase: {currentState.phase}")
        # print(move)
        # if i > 5000:
        # print("game went too long")
        # currentState.printBoardState()
        # break
    # log.close()
    return currentState.getWinners()

if __name__ == "__main__":
    geneticAlgorithm(15, 1, 0.2, 0.3)
