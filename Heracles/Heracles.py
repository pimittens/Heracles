import random
import Game
import MCTS
import time
import numpy as np
import twoPlayerNetwork


def printOptions(options, boardState):
    print(f"Decision for player {options[0][1]}")
    i = 1
    for option in options:
        match option[0]:
            case Game.Move.PASS:
                print(f"{i}: Pass")
            case Game.Move.TAKE_EXTRA_TURN:
                if option[2][0]:
                    print(f"{i}: Take an extra turn (spend 2 sun)")
                else:
                    print(f"{i}: Do not take an extra turn")
            case Game.Move.CHOOSE_BUY_FACES:
                print(f"{i}: Buy die faces")
            case Game.Move.CHOOSE_PERFORM_FEAT:
                print(f"{i}: Perform a feat")
            case Game.Move.BUY_FACES:
                faces = ""
                for face in option[2]:
                    faces += f"{face} "
                print(f"{i}: Buy the following die faces: {faces}")
            case Game.Move.PERFORM_FEAT:
                print(f"{i}: Perform the feat {option[2][0]}")
            case Game.Move.FORGE_FACE:
                if option[2][0]:
                    die = 1
                else:
                    die = 2
                print(f"{i}: Forge face {option[2][1]} over face {option[2][2]} on die {die}")
            case Game.Move.CHOOSE_DIE_OR:
                resource = "gold"
                match option[2][0]:
                    case 1:
                        resource = "sun"
                    case 2:
                        resource = "moon"
                    case 3:
                        resource = "vp"
                    case 4:
                        resource = "ancient shard"
                    case 5:
                        resource = "loyalty"
                if boardState.phase == Game.Phase.MINOR_CHOOSE_OR:
                    if boardState.players[option[1]].dieChoice:
                        dieFace = boardState.players[option[1]].getDie1Result()
                    else:
                        dieFace = boardState.players[option[1]].getDie2Result()
                elif boardState.phase == Game.Phase.DIE_1_CHOOSE_OR or Game.Phase.MISFORTUNE_1_CHOOSE_OR or Game.Phase.MINOR_MISFORTUNE_1_OR:
                    if boardState.satyrs:
                        satyrsChoice = boardState.players[option[1]].orChoice1
                        if satyrsChoice % 2 == 0:
                            dieFace = boardState.players[satyrsChoice // 2].getDie1UpFace()
                        else:
                            dieFace = boardState.players[satyrsChoice // 2].getDie2UpFace()
                    else:
                        dieFace = boardState.players[option[1]].getDie1Result()
                else:  # elif boardState.phase == Game.Phase.DIE_2_CHOOSE_OR or Game.Phase.MISFORTUNE_2_CHOOSE_OR or Game.Phase.MINOR_MISFORTUNE_2_OR:
                    if boardState.satyrs:
                        satyrsChoice = boardState.players[option[1]].orChoice2
                        if satyrsChoice % 2 == 0:
                            dieFace = boardState.players[satyrsChoice // 2].getDie1UpFace()
                        else:
                            dieFace = boardState.players[satyrsChoice // 2].getDie2UpFace()
                    else:
                        dieFace = boardState.players[option[1]].getDie2Result()
                print(f"{i}: Gain resource {resource} from die face {dieFace}")
            case Game.Move.CHOOSE_REINF_EFFECT:
                print(f"{i}: Use reinforcement effect {option[2][0]}")
            case Game.Move.USE_ELDER:
                if option[2][0]:
                    print(f"{i}: Use the effect of The Elder (pay 3 gold to gain 4 vp)")
                else:
                    print(f"{i}: Do not use the effect of The Elder")
            case Game.Move.OWL_CHOICE:
                print(f"{i}: Use the effect of The Guardian's Owl to gain 1 {option[2][0]}")
            case Game.Move.CHOOSE_BOAR_PLAYER:
                print(f"{i}: Choose player {option[2][0]} to be the face bearer")
            case Game.Move.BOAR_CHOICE:
                print(f"{i}: Use the effect of Tenacious Boar to gain {option[2][0]}")
            case Game.Move.ROLL:
                if boardState.phase == Game.Phase.ROLL_DIE_1 or boardState.phase == Game.Phase.BLESSING_ROLL_DIE_1 or boardState.phase == Game.Phase.TWINS_REROLL_1:
                    print(f"{i}: Roll face {option[2][0]} on die 1")
                elif boardState.phase == Game.Phase.ROLL_DIE_2 or boardState.phase == Game.Phase.BLESSING_ROLL_DIE_2 or boardState.phase == Game.Phase.TWINS_REROLL_2:
                    print(f"{i}: Roll face {option[2][0]} on die 2")
                else:
                    if boardState.players[option[1]].dieChoice:
                        print(f"{i}: Roll face {option[2][0]} on die 1")
                    else:
                        print(f"{i}: Roll face {option[2][0]} on die 2")
            case Game.Move.RANDOM_ROLL:
                print(f"{i}: Roll randomly")
            case Game.Move.MIRROR_CHOICE:
                print(
                    f"{i}: Use the effect of The Mirror of the Abyss die face to copy the effect of the face {option[2][0]}")
            case Game.Move.USE_TWINS:
                if option[2][0]:
                    print(f"{i}: Use the effect of The Twins (pay 3 gold to reroll)")
                else:
                    print(f"{i}: Do not use the effect of The Twins")
            case Game.Move.TWINS_CHOOSE_DIE:
                if option[2][0]:
                    print(f"{i}: Use the effect of The Twins to reroll die 1")
                else:
                    print(f"{i}: Use the effect of The Twins to reroll die 2")
            case Game.Move.TWINS_CHOOSE_RESOURCE:
                if option[2][0] == "vp":
                    print(f"{i}: Use the effect of The Twins to gain 1 vp")
                else:
                    print(f"{i}: Use the effect of The Twins to gain 1 moon")
            case Game.Move.USE_CERBERUS:
                if option[2][0]:
                    print(f"{i}: Spend a Cerberus Token")
                else:
                    print(f"{i}: Do not spend a Cerberus Token")
            case Game.Move.CHOOSE_DIE:
                if option[2][0]:
                    print(f"{i}: Roll die 1")
                else:
                    print(f"{i}: Roll die 2")
            case Game.Move.CHOOSE_USE_SENTINEL:
                if boardState.phase == Game.Phase.DIE_1_CHOOSE_SENTINEL:
                    die = 1
                else:
                    die = 2
                if option[2][0]:
                    print(f"{i}: Use the effect of Sentinel on the result of die {die} (convert sun and moon into vp)")
                else:
                    print(f"{i}: Do not use the effect of Sentinel on the result of die {die}")
            case Game.Move.CHOOSE_USE_CYCLOPS:
                if option[2][0]:
                    print(f"{i}: Use the effect of Cyclops (convert gold into vp)")
                else:
                    print(f"{i}: Do not use the effect of Cyclops")
            case Game.Move.CHOOSE_ADD_HAMMER_SCEPTER:
                print(
                    f"{i}: Spend {option[2][0]} gold on The Blacksmith's Hammer/Scepter track and gain {boardState.players[option[1]].goldToGain - option[2][0]} gold")
            case Game.Move.SATYRS_CHOOSE_DIE:
                if option[2][0] % 2 == 0:
                    print(
                        f"{i}: Use the effect of the Satyrs to resolve the die face {boardState.players[option[2][0] // 2].getDie1UpFace()}")
                else:
                    print(
                        f"{i}: Use the effect of the Satyrs to resolve the die face {boardState.players[option[2][0] // 2].getDie2UpFace()}")
            case Game.Move.USE_TRITON_TOKEN:
                print(f"{i}: Spend a Triton token to gain {option[2][0]}")
            case Game.Move.USE_COMPANION:
                print(f"{i}: Use The Companion to gain {option[2][0]} sun and vp")
            case Game.Move.USE_LIGHT:
                if option[2][0]:
                    print(f"{i}: Use the effect of The Light to gain the effect of {option[2][1]} (spend 3 gold)")
                else:
                    print(f"{i}: Do not use the effect of The Light")
            case Game.Move.SPEND_GOLD:
                print(
                    f"{i}: Spend {option[2][0]} gold from The Blacksmith's Scepters and {boardState.players[option[1]].goldToSpend - option[2][0]} from the main gold reserve")
            case Game.Move.SPEND_SUN:
                print(
                    f"{i}: Spend {option[2][0]} sun from The Blacksmith's Scepters, {option[2][1]} ancient shards, and {boardState.players[option[1]].sunToSpend - option[2][0] - option[2][1]} from the main sun reserve")
            case Game.Move.SPEND_MOON:
                print(
                    f"{i}: Spend {option[2][0]} moon from The Blacksmith's Scepters, {option[2][1]} ancient shards, and {boardState.players[option[1]].moonToSpend - option[2][0] - option[2][1]} from the main moon reserve")
            case Game.Move.CHOOSE_FACES:
                print(f"{i}: Place the faces {option[2][0]} and {option[2][1]} face up and gain their effects")
            case Game.Move.RIGHTHAND_SPEND:
                print(f"{i}: Use the effect of The Right Hand to spend {option[2][0]} gold and gain {option[2][0]} vp")
            case Game.Move.CHOOSE_RESOURCE:
                match option[2][0]:
                    case 0:
                        type = "gold"
                    case 1:
                        type = "sun"
                    case 2:
                        type = "moon"
                    case 3:
                        type = "vp"
                    case 4:
                        type = "ancient shards"
                    case _:
                        type = "loyalty"
                print(f"{i}: Use the effect of The Wind to gain all of the {type} shown on dice")
            case Game.Move.MERCHANT_UPGRADE:
                if len(option[2]) == 1:
                    print(f"{i}: Use the effect of The Merchant to gain {option[2][0]} vp")
                else:
                    if option[2][1]:
                        print(
                            f"{i}: Use the effect of The Merchant to gain {option[2][0]} vp and upgrade the face {option[2][2]} on die 1 to the face {option[2][3]}")
                    else:
                        print(
                            f"{i}: Use the effect of The Merchant to gain {option[2][0]} vp and upgrade the face {option[2][2]} on die 2 to the face {option[2][3]}")
            case Game.Move.CHOOSE_MAZE_ORDER:
                if option[2][0]:
                    print(f"{i}: Roll celestial die then do maze moves")
                else:
                    print(f"{i}: Do maze moves then roll celestial die")
            case Game.Move.CHOOSE_CELESTIAL_DIE_OR:
                if option[2][0] == 0:
                    type = "3 gold"
                elif option[2][0] == 1:
                    type = "1 sun"
                else:
                    type = "1 moon"
                print(f"{i}: Use the effect of the celestial die to gain {type}")
            case Game.Move.CHOOSE_TREASURE_HALL:
                print(f"{i}: Choose the treasure hall {option[2][0]}")
            case Game.Move.MAZE_MOVE:
                print(f"{i}: Move to space {option[2][0]} in the maze")
            case Game.Move.MAZE_SPEND:
                if option[2][0]:
                    if boardState.phase == Game.Phase.MAZE_EFFECT_SPEND_GOLD:
                        print(f"{i}: Spend 6 gold to gain 6 vp")
                    else:
                        print(f"{i}: Spend 2 moon to gain 8 vp")
                else:
                    print(f"{i}: Do not spend")
            case Game.Move.CHOOSE_MAZE_OR:
                resource = "gold"
                match option[2][0]:
                    case 1:
                        resource = "sun"
                    case 2:
                        resource = "moon"
                    case 3:
                        resource = "vp"
                print(f"{i}: Gain {resource} from the effect of a maze space")
            case Game.Move.CELESTIAL_UPGRADE:
                if option[2][0]:
                    print(
                        f"{i}: Use the effect of The Celestial Die to upgrade the face {option[2][1]} on die 1 to the face {option[2][2]}")
                else:
                    print(
                        f"{i}: Use the effect of The Celestial Die to upgrade the face {option[2][1]} on die 2 to the face {option[2][2]}")
            case Game.Move.CELESTIAL_GODDESS:
                if option[2][0]:
                    print(
                        f"{i}: Use the effect of The Celestial Die to set die 1 to the face {option[2][1]} and gain its effect")
                else:
                    print(
                        f"{i}: Use the effect of The Celestial Die to set die 2 to the face {option[2][1]} and gain its effect")
            case Game.Move.CELESTIAL_MIRROR_CHOICE:
                print(f"{i}: Use the effect of The Celestial Die to gain the effect of the die face {option[2][0]}")
            case Game.Move.CHOOSE_MEMORY:
                if option[2][0]:
                    token1 = "ancient shard"
                else:
                    token1 = "loyalty"
                if option[2][1]:
                    token2 = "ancient shard"
                else:
                    token2 = "loyalty"
                print(
                    f"{i}: Place a(n) {token1} memory token on island {option[2][1]} and a {token2} memory token on island {option[2][3]}")
            case Game.Move.GUARDIAN_CHOICE:
                print(f"{i}: Gain one {option[2][0]} from the effect of The Guardian")
            case Game.Move.CHOOSE_RESOLVE_ORDER:
                if option[2][0]:
                    print(f"{i}: Resolve die 1 then die 2")
                else:
                    print(f"{i}: Resolve die 2 then die 1")
            case _:
                print(f"{i}: Unhandled move type {option[0]}")
        i += 1


def printMove(move):
    print(f"making move: {move}")  # todo: more detail


def generateData(numGames):
    print(f"playing {numGames} games")
    i = 0
    startTime = time.time()
    cutoff = 60 * 60 * 8 # 8 hours
    while i < numGames:

        gameStartTime = time.time()
        module = 1 # i % 3  # 0 is no module, 1 is goddess maze, 2 is titans
        players = [Game.Player(0, True, module), Game.Player(1, True, module)]
        theBoard = Game.LoggingBoardState(players, True, module, True)
        theBoard.startLogging()
        undoState = theBoard.copyState()
        mcts = twoPlayerNetwork.NeuralMCTS(twoPlayerNetwork.build2pModel(), num_simulations=200)

        while not theBoard.isOver():
            options = theBoard.getOptions()
            if theBoard.printingEnabled:
                printOptions(options, theBoard)
            if theBoard.players[options[0][1]].ai:
                if options[0][0] == Game.Move.ROLL:
                    if theBoard.printingEnabled:
                        printMove(options[len(options) - 1])
                    theBoard.makeMove(options[len(options) - 1])  # always do random roll
                    if theBoard.printingEnabled:
                        print(
                        f"After rolling, player {options[0][1]} has the faces {theBoard.players[options[0][1]].getDie1UpFace()} and {theBoard.players[options[0][1]].getDie2UpFace()}")
                elif options[0][1] == 0:
                    move = MCTS.mctsWithHeuristic(theBoard.copyState(), 500, theBoard.printingEnabled)
                    if theBoard.printingEnabled:
                        printMove(move)
                    theBoard.makeMove(move)
                elif options[0][1] == 1:
                    policy = mcts.run(theBoard.copyState())
                    print(policy)
                    selection = np.random.choice(range(len(theBoard.getOptions())), p=policy)
                    move = theBoard.getOptions()[selection]
                    if theBoard.printingEnabled:
                        printMove(move)
                    theBoard.makeMove(move)
                else:
                    move = random.choice(options)
                    if theBoard.printingEnabled:
                        printMove(move)
                    theBoard.makeMove(move)
            else:
                # theBoard.makeMove(options[0])
                while True:
                    choice = input("select from the above options: ")
                    if choice == "print":
                        theBoard.printBoardState()
                        printOptions(options, theBoard)
                        continue
                    if choice == "undo":
                        theBoard = undoState
                        options = theBoard.getOptions()
                        printOptions(options, theBoard)
                        continue
                    if not choice.isdigit():
                        print("invalid choice")
                        printOptions(options, theBoard)
                        continue
                    choice = int(choice)
                    if choice in list(range(1, len(options) + 1)):
                        break
                    print("invalid choice")
                    printOptions(options, theBoard)
                undoState = theBoard.copyLoggingState()
                printMove(options[choice - 1])
                theBoard.makeMove(options[choice - 1])

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

generateData(3)