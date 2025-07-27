import Game

players = [Game.Player(0, False), Game.Player(1, True), Game.Player(2, True), Game.Player(3, True)]
theBoard = Game.BoardState(players, True)
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

while theBoard.round < 10:
    options = theBoard.getOptions()
    i = 1
    for option in options:
        print(f"{i}: {option}")
        i += 1
    while True:
        choice = input("select from the above options:")
        choice = int(choice)
        if choice in list(range(1,len(options) + 1)):
            break
        print("invalid choice")
    theBoard.makeMove(options[choice - 1])