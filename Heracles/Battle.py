import Game
import time
import DiceforgePlayers
import Data
import json


def initialize_data():
    ret = {}
    ret["games"] = 0
    ret["points"] = 0
    for feat in Data.HeroicFeat:
        ret[feat.name] = {"winner": 0, "loser": 0, "unused": 0}
    for face in Data.DieFace:
        ret[face.name] = {"winner": 0, "loser": 0}
    return ret


def append_data(data, board):
    data["games"] += 1
    data["points"] += sum(board.getScores())
    winners = board.getWinners()

    for feat in Data.HeroicFeat:
        winner_feats = loser_feats = unused_feats = 0
        if Data.isBoarFeat(feat):
            for island in board.islands:
                for ft in island:
                    if Data.isBoarFeat(ft):
                        unused_feats += 1
            for player in board.players:
                if winners[player.playerID] == 1:
                    for ft in player.feats:
                        if Data.isBoarFeat(ft):
                            winner_feats += 1
                else:
                    for ft in player.feats:
                        if Data.isBoarFeat(ft):
                            loser_feats += 1
        elif Data.isMisfortuneFeat(feat):
            for island in board.islands:
                for ft in island:
                    if Data.isMisfortuneFeat(ft):
                        unused_feats += 1
            for player in board.players:
                if winners[player.playerID] == 1:
                    for ft in player.feats:
                        if Data.isMisfortuneFeat(ft):
                            winner_feats += 1
                else:
                    for ft in player.feats:
                        if Data.isMisfortuneFeat(ft):
                            loser_feats += 1
        else:
            for island in board.islands:
                for ft in island:
                    if ft == feat:
                        unused_feats += 1
            for player in board.players:
                if winners[player.playerID] == 1:
                    for ft in player.feats:
                        if ft == feat:
                            winner_feats += 1
                else:
                    for ft in player.feats:
                        if ft == feat:
                            loser_feats += 1
        data[feat.name]["winner"] += winner_feats
        data[feat.name]["loser"] += loser_feats
        data[feat.name]["unused"] += unused_feats

    for face in Data.DieFace:
        winner_faces = loser_faces = 0
        for player in board.players:
            if winners[player.playerID] == 1:
                for fc in player.die1.faces:
                    if face == fc:
                        winner_faces += 1
                for fc in player.die2.faces:
                    if face == fc:
                        winner_faces += 1
            else:
                for fc in player.die1.faces:
                    if face == fc:
                        loser_faces += 1
                for fc in player.die2.faces:
                    if face == fc:
                        loser_faces += 1
        data[face.name]["winner"] += winner_faces
        data[face.name]["loser"] += loser_faces


def collect_data(num_games, sims, data):
    print(f"playing {num_games} games")
    i = 0
    startTime = time.time()
    while i < num_games:

        if i % 10 == 0 and i > 0:
            with open("data.json", "w") as f:
                json.dump(data, f)
            f.close()

        gameStartTime = time.time()
        module = i % 3  # 0 is no module, 1 is goddess maze, 2 is titans
        players = [Game.Player(0, DiceforgePlayers.MCTSHeuristicPlayer(sims), module),
                   Game.Player(1, DiceforgePlayers.MCTSHeuristicPlayer(sims), module)]
        theBoard = Game.BoardState(players, True, module)

        while not theBoard.isOver():
            theBoard.makeMove(theBoard.getOptionPlayer().play(theBoard))

        append_data(data, theBoard)

        i += 1
        print(f"finished game {i} out of {num_games}")
        print(f"game took {(time.time() - gameStartTime) / 60} minutes")
        print(f"total time elapsed: {(time.time() - startTime) / 60} minutes")
        print(f"average time per game: {(time.time() - startTime) / i / 60} minutes")
        print(f"estimated time remaining: {((time.time() - startTime) / i * (num_games - i)) / 60} minutes")

    with open("data.json", "w") as f:
        json.dump(data, f)
    f.close()


def battle(numGames, iter1, iter2):  # iterations should be different
    print(f"playing {numGames} games")
    iter1Wins = iter2Wins = 0
    i = 0
    startTime = time.time()
    while i < numGames:

        if i < numGames // 2:
            first = iter1
            second = iter2
        else:
            first = iter2
            second = iter1

        gameStartTime = time.time()
        module = i % 3  # 0 is no module, 1 is goddess maze, 2 is titans
        players = [Game.Player(0, DiceforgePlayers.NeuralNetPlayer(first), module),
                   Game.Player(1, DiceforgePlayers.NeuralNetPlayer(second), module)]
        theBoard = Game.LoggingBoardState(players, True, module, False)
        theBoard.startLogging()

        while not theBoard.isOver():
            move = theBoard.getOptionPlayer().play(theBoard)
            if theBoard.printingEnabled:
                print(f"making move: {move}")
            theBoard.makeMove(move)
            if move[0] == Game.Move.RANDOM_ROLL and theBoard.printingEnabled:
                print(
                    f"After rolling, player {move[1]} has the faces {theBoard.players[move[1]].getDie1UpFace()} and {theBoard.players[move[1]].getDie2UpFace()}")

        if theBoard.printingEnabled:
            theBoard.printBoardState()
        if theBoard.printingEnabled:
            theBoard.printPoints()
        theBoard.endLogging()
        theBoard.printPoints()
        print(f"player 1 was iteration {first} and player 2 was iteration {second}")
        if theBoard.getWinners()[0] == 1:
            if first == iter1:
                print(f"player 1 won so iteration {iter1} gains a win")
                iter1Wins += 1
            else:
                print(f"player 1 won so iteration {iter2} gains a win")
                iter2Wins += 1
        if theBoard.getWinners()[1] == 1:
            if second == iter1:
                print(f"player 2 won so iteration {iter1} gains a win")
                iter1Wins += 1
            else:
                print(f"player 2 won so iteration {iter2} gains a win")
                iter2Wins += 1
        i += 1
        print(f"finished game {i} out of {numGames}")
        print(f"game took {(time.time() - gameStartTime) / 60} minutes")
        print(f"total time elapsed: {(time.time() - startTime) / 60} minutes")
        print(f"estimated time remaining: {((time.time() - startTime) / i * (numGames - i)) / 60} minutes")

    print(
        f"results: iteration {iter1} won {iter1Wins} games out of {numGames} ({100 * iter1Wins / numGames}% winrate), and iteration {iter2} won {iter2Wins} games out of {numGames} ({100 * iter2Wins / numGames}% winrate)")


# battle(18, 140, 0)


try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = initialize_data()

collect_data(500, 500, data)
