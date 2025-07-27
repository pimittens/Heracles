import random
import math
import copy

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.points = 0

    def isTerminalNode(self):
        return self.state.isOver() > 0

    def isFullyExpanded(self):
        return len(self.children) == len(self.state.getOptions())

    def bestChild(self, explorationWeight=1.41):
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
        for move in options:
            if move not in tried:
                nextState = self.state.copyState()
                nextState.makeMove(move)
                childNode = Node(nextState, self, move)
                self.children.append(childNode)
                return childNode

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
    root = Node(rootState.copyState())
    for _ in range(numSims):
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
    print("mcts results")
    for node in root.children:
        print(f"Move: {node.move}, visits:{node.visits} , average points: {node.points/node.visits}")
    return root.mostVisitedChild().move


def rollout(state):
    currentState = state.copyState()
    while currentState.isOver() == 0:
        possibleMoves = currentState.getOptions()
        move = random.choice(possibleMoves)
        currentState.makeMove(move)
    return currentState.getPoints()