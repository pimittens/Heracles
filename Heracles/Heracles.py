import random
import Game
import MCTS

players = [Game.Player(0, False), Game.Player(1, False)]
theBoard = Game.BoardState(players, True)
undoState = theBoard.copyState()
theBoard.printBoardState()


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
                print(f"{i}: Forge face {option[2][1]} over face {option[2][2]} on die {option[2][0]}")
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
            case Game.Move.CHOOSE_ADD_HAMMER:
                print(
                    f"{i}: Spend {option[2][0]} gold on The Blacksmith's Hammer track and gain {boardState.players[option[1]].goldToGain - option[2][0]} gold")
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

        i += 1


def printMove(move):
    print(f"making move: {move}")  # todo: more detail


while not theBoard.isOver():
    options = theBoard.getOptions()
    printOptions(options, theBoard)
    if theBoard.players[options[0][1]].ai:
        if options[0][0] == Game.Move.ROLL:
            printMove(options[len(options) - 1])
            theBoard.makeMove(options[len(options) - 1])  # always do random roll
            print(
                f"After rolling, player {options[0][1]} has the faces {theBoard.players[options[0][1]].getDie1UpFace()} and {theBoard.players[options[0][1]].getDie2UpFace()}")
        elif options[0][1] == 1:
            move = MCTS.mcts(theBoard.copyState(), 5000)
            printMove(move)
            theBoard.makeMove(move)
        elif options[0][1] == 0:
            move = MCTS.mctsWithHeuristic(theBoard.copyState(), 5000)
            printMove(move)
            theBoard.makeMove(move)
        else:
            move = random.choice(options)
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
        undoState = theBoard.copyState()
        printMove(options[choice - 1])
        theBoard.makeMove(options[choice - 1])

theBoard.printBoardState()
theBoard.printPoints()
