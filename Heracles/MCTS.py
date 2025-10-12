import os
import random
import math
from Game import Move
from Data import getTotalGoldCost
from Data import DieFace
import time


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
        if self.children and self.children[0].move[0] == Move.ROLL:
            return True
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
        if self.children[0].move[0] == Move.ROLL:
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
        if options[0][0] == Move.ROLL:
            for move in options:
                if move[0] == Move.ROLL:
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
        if self.children and self.children[0].move[0] == Move.ROLL:
            return True
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
        if self.children[0].move[0] == Move.ROLL:
            roll = random.choice(range(0, 6))
            i = 0
            for child in self.children:
                i += child.move[2][1]
                if roll < i:
                    return child
        if self.children[0].move[0] == Move.CHOOSE_BUY_FACES and (self.state.round == 1 or (
                self.state.round < 4 and self.state.players[self.children[0].move[1]].gold >= 8)):
            # buy faces early if player has a lot of gold
            return self.children[0]
        elif self.children[0].move[0] == Move.BUY_FACES and len(self.children) > 5:
            # don't consider face buys which don't spend most of current gold
            gold = self.state.players[self.children[0].move[1]].gold
            if self.state.round > 3:
                gold -= 1
            choicesWeights = []
            for child in self.children:
                if child.move[0] != Move.BUY_FACES or getTotalGoldCost(child.move[2]) < gold:
                    choicesWeights.append(0)
                else:
                    choicesWeights.append((child.points / child.visits) + explorationWeight * math.sqrt(
                        math.log(self.visits) / child.visits
                    ))
            if max(choicesWeights) > 0:
                return self.children[choicesWeights.index(max(choicesWeights))]
        elif self.children[0].move[0] == Move.FORGE_FACE:
            # prioritize forging over gold 1 faces
            choicesWeights = []
            for child in self.children:
                if child.move[0] == Move.FORGE_FACE and child.move[2][2] == DieFace.GOLD1:
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
        if options[0][0] == Move.ROLL:
            for move in options:
                if move[0] == Move.ROLL:
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


def mcts(rootState, numSims):
    startTime = time.time()
    root = Node(rootState.copyState())
    if len(root.state.getOptions()) == 1:
        return root.state.getOptions()[0]
    if root.state.getOptions()[0][0] == Move.CHOOSE_RESOLVE_ORDER:
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
    if root.state.getOptions()[0][0] == Move.CHOOSE_RESOLVE_ORDER:
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


def rollout(state):
    currentState = state.copyState()
    #i = 0
    #if not os.path.exists("logs"):
    #    os.makedirs("logs")
    #if os.path.exists("logs/rollout.txt"):
    #    os.remove("logs/rollout.txt")
    #log = open("logs/rollout.txt", "a")
    #log.write("Begin rollout\n")
    while not currentState.isOver():
        possibleMoves = currentState.getOptions()
        if possibleMoves[0][0] == Move.ROLL:
            currentState.makeMove(possibleMoves[len(possibleMoves) - 1]) # random roll
            continue
        #log.write(f"phase: {currentState.phase}, options: {possibleMoves}\n")
        #log.write(f"activeplayer gold: {currentState.players[currentState.activePlayer].gold}, sun: {currentState.players[currentState.activePlayer].sun}, moon: {currentState.players[currentState.activePlayer].moon}, goldToSpend: {currentState.players[currentState.activePlayer].goldToSpend}, sunToSpend: {currentState.players[currentState.activePlayer].sunToSpend}, moonToSpend: {currentState.players[currentState.activePlayer].moonToSpend}\n")
        #for scepter in currentState.players[currentState.activePlayer].scepters:
        #    log.write(f"scepter: {scepter}\n")
        #if not possibleMoves:
        #    log.close()
        move = random.choice(possibleMoves)
        #log.write(f"making move: {move}\n")
        currentState.makeMove(move)
        #i += 1
        #if i > 4990: # this is just for testing
            #print(f"phase: {currentState.phase}")
            #print(move)
        #if i > 5000:
            #print("game went too long")
            #currentState.printBoardState()
            #break
    #log.close()
    return currentState.getWinners()
