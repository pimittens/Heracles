import random
import Game
import MCTS
import time
import DiceforgePlayers


def printMove(move):
    print(f"making move: {move}")  # todo: more detail


def generateData(numGames):
    print(f"playing {numGames} games")
    i = 0
    startTime = time.time()
    cutoff = 60 * 60 * 8 # 8 hours
    while i < numGames:

        gameStartTime = time.time()
        module = i % 3  # 0 is no module, 1 is goddess maze, 2 is titans
        players = [Game.Player(0, DiceforgePlayers.RandomPlayer(), module), Game.Player(1, DiceforgePlayers.RandomPlayer(), module)]
        theBoard = Game.LoggingBoardState(players, True, module, True)
        theBoard.startLogging()

        while not theBoard.isOver():
            move = theBoard.getOptionPlayer().play(theBoard)
            if theBoard.printingEnabled:
                printMove(move)
            theBoard.makeMove(move)
            if move[0] == Game.Move.RANDOM_ROLL and theBoard.printingEnabled:
                print(f"After rolling, player {move[1]} has the faces {theBoard.players[move[1]].getDie1UpFace()} and {theBoard.players[move[1]].getDie2UpFace()}")

        if theBoard.printingEnabled:
            theBoard.printBoardState()
        if theBoard.printingEnabled:
            theBoard.printPoints()
        theBoard.endLogging()
        i += 1
        print(f"finished game {i} out of {numGames}")
        print(f"game took {(time.time() - gameStartTime) / 60} minutes")
        print(f"total time elapsed: {(time.time() - startTime) / 60} minutes")
        print(f"estimated time remaining: {((time.time() - startTime) / i * (numGames - i)) / 60} minutes")
        if time.time() - startTime > cutoff:
            print("runtime exceeded cutoff time, terminating early")
            break

generateData(1)