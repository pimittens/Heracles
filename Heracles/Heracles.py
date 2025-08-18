import random
import Game
import MCTS

players = [Game.Player(0, True), Game.Player(1, True)]
theBoard = Game.BoardState(players, True)
undoState = theBoard.copyState()
theBoard.printBoardState()

"""
theBoard.players[0].gold = 12
options = theBoard.generateBuyFaces()
for action in options:
    print("Buy Faces:")
    for face in action[2]:
        print(face)

theBoard.players[0].sun = 6
theBoard.players[0].moon = 6
options = theBoard.generatePerformFeats()
for action in options:
    print(f"Perform Feat: {action[2][0]}")

print(Data.getResourceValues(Game.DieFace.BLUEBOAR))
"""

while not theBoard.isOver():
    options = theBoard.getOptions()
    i = 1
    for option in options:
        print(f"{i}: {option}")
        i += 1
    if theBoard.players[options[0][1]].ai:
        if options[0][0] == Game.Move.ROLL:
            theBoard.makeMove(options[len(options) - 1]) # always do random roll
        elif options[0][1] == 1:
            theBoard.makeMove(MCTS.mcts(theBoard.copyState(), 500))
        else:
            theBoard.makeMove(random.choice(options))
    else:
        #theBoard.makeMove(options[0])
        while True:
            choice = input("select from the above options: ")
            if choice == "print":
                theBoard.printBoardState()
                for option in options:
                    print(f"{i}: {option}")
                i += 1
                continue
            if choice == "undo":
                theBoard = undoState
                options = theBoard.getOptions()
                for option in options:
                    print(f"{i}: {option}")
                i += 1
                continue
            choice = int(choice)
            if choice in list(range(1,len(options) + 1)):
                break
            print("invalid choice")
            for option in options:
                print(f"{i}: {option}")
                i += 1
        undoState = theBoard.copyState()
        theBoard.makeMove(options[choice - 1])



theBoard.printBoardState()
theBoard.printPoints()