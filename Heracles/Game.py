import copy
from enum import Enum
import random
import Data


class Phase(Enum):
    TURN_START = 1
    ROLL_DIE_1 = 2
    ROLL_DIE_2 = 3
    RESOLVE_DIE_1 = 4
    RESOLVE_DIE_2 = 5
    USE_TWINS_CHOICE = 6
    TWINS_REROLL_CHOICE = 7
    TWINS_RESOURCE_CHOICE = 8
    TWINS_REROLL_1 = 9
    TWINS_REROLL_2 = 10
    USE_CERBERUS_CHOICE = 11
    MIRROR_1_CHOICE = 12
    MIRROR_2_CHOICE = 13
    DIE_1_CHOOSE_OR = 14
    DIE_2_CHOOSE_OR = 15
    APPLY_DICE_EFFECTS = 16
    RESOLVE_MAZE_MOVES = 17
    RESOLVE_SHIPS = 18
    RESOLVE_SHIPS_FORGE = 19
    BOAR_CHOICE_1 = 20
    BOAR_CHOICE_2 = 21
    MISFORTUNE_1 = 22  # die number (blessing player), die number being resolved by misfortune player
    MISFORTUNE_1_MIRROR = 23
    MISFORTUNE_1_CHOOSE_OR = 24
    MISFORTUNE_1_APPLY_EFFECTS = 25
    MISFORTUNE_1_RESOLVE_MAZE_MOVES = 26
    MISFORTUNE_1_RESOLVE_SHIPS = 27
    MISFORTUNE_1_RESOLVE_SHIPS_FORGE = 28
    MISFORTUNE_2 = 29  # these go in reverse order since the misfortune face is on die 2
    MISFORTUNE_2_MIRROR = 30
    MISFORTUNE_2_CHOOSE_OR = 31
    MISFORTUNE_2_APPLY_EFFECTS = 32
    MISFORTUNE_2_RESOLVE_MAZE_MOVES = 33
    MISFORTUNE_2_RESOLVE_SHIPS = 34
    MISFORTUNE_2_RESOLVE_SHIPS_FORGE = 35
    CERBERUS_DECISION = 36  # if used cerberus token, return to mirror 1 choice
    MINOR_CHOOSE_DIE = 37  # minor blessing states
    MINOR_ROLL_DIE = 38
    MINOR_TWINS_CHOICE = 39
    MINOR_TWINS_REROLL = 40
    MINOR_TWINS_RESOURCE = 41
    MINOR_USE_CERBERUS = 42
    MINOR_MIRROR_CHOICE = 43
    MINOR_CHOOSE_OR = 44
    MINOR_MAZE_MOVES = 45
    MINOR_RESOLVE_SHIPS = 46
    MINOR_RESOLVE_SHIPS_FORGE = 47
    MINOR_BOAR_CHOICE = 48
    MINOR_MISFORTUNE = 49
    MINOR_MISFORTUNE_1_MIRROR = 50
    MINOR_MISFORTUNE_1_OR = 51
    MINOR_MISFORTUNE_2_MIRROR = 52
    MINOR_MISFORTUNE_2_OR = 53
    MINOR_MISFORTUNE_RESOLVE = 54
    MINOR_MISFORTUNE_MAZE = 55
    MINOR_MISFORTUNE_SHIPS = 56
    MINOR_MISFORTUNE_SHIPS_FORGE = 57
    MINOR_CERBERUS_DECISION = 58
    CHOOSE_REINF_EFFECT = 59
    RESOLVE_ELDER_REINF = 60
    RESOLVE_OWL_REINF = 61
    RESOLVE_HIND_REINF = 62
    RESOLVE_TREE_REINF = 63
    RESOLVE_MERCHANT_REINF = 64
    RESOLVE_LIGHT_REINF = 65
    RESOLVE_COMPANION_REINF = 66
    ACTIVE_PLAYER_CHOICE_1 = 67
    ACTIVE_PLAYER_BUY_FACES_1 = 68
    ACTIVE_PLAYER_PERFORM_FEAT_1 = 69
    EXTRA_TURN_DECISION = 70
    ACTIVE_PLAYER_CHOICE_2 = 71
    ACTIVE_PLAYER_BUY_FACES_2 = 72
    ACTIVE_PLAYER_PERFORM_FEAT_2 = 73
    FORGE_SHIP_FACE_1 = 74
    FORGE_SHIP_FACE_2 = 75
    CHOOSE_SHIELD_FACE_1 = 76
    CHOOSE_SHIELD_FACE_2 = 77
    FORGE_HELMET_FACE_1 = 78
    FORGE_HELMET_FACE_2 = 79
    FORGE_MIRROR_FACE_1 = 80
    FORGE_MIRROR_FACE_2 = 81
    CHOOSE_BOAR_MISFORTUNE_PLAYER_1 = 82
    CHOOSE_BOAR_MISFORTUNE_PLAYER_2 = 83
    FORGE_BOAR_MISFORTUNE_1 = 84
    FORGE_BOAR_MISFORTUNE_2 = 85
    ROLL_CELESTIAL_DIE = 88
    BLESSING_ROLL_DIE_1 = 89
    BLESSING_ROLL_DIE_2 = 90
    END_TURN = 91
    DIE_1_CHOOSE_SENTINEL = 92
    DIE_2_CHOOSE_SENTINEL = 93
    CHOOSE_CYCLOPS = 94



class Move(Enum):
    PASS = 1
    TAKE_EXTRA_TURN = 2
    CHOOSE_BUY_FACES = 3
    CHOOSE_PERFORM_FEAT = 4
    BUY_FACES = 5
    PERFORM_FEAT = 6
    FORGE_FACE = 7
    CHOOSE_DIE_OR = 8
    RETURN_TO_FEAT = 9
    CHOOSE_REINF_EFFECT = 10
    USE_ELDER = 11
    OWL_CHOICE = 12
    CHOOSE_BOAR_PLAYER = 13
    BOAR_CHOICE = 14
    ROLL = 15
    RANDOM_ROLL = 16
    MIRROR_CHOICE = 17
    USE_TWINS = 18
    TWINS_CHOOSE_DIE = 19
    TWINS_CHOOSE_RESOURCE = 20
    USE_CERBERUS = 21
    CHOOSE_DIE = 22
    CHOOSE_USE_SENTINEL = 23
    CHOOSE_USE_CYCLOPS = 24


class BoardState:
    def __init__(self, players, initialState):
        self.players = players
        self.temple = ([Data.DieFace.GOLD3, Data.DieFace.GOLD3, Data.DieFace.GOLD3, Data.DieFace.GOLD3],
                       [Data.DieFace.MOON1, Data.DieFace.MOON1, Data.DieFace.MOON1, Data.DieFace.MOON1],
                       [Data.DieFace.GOLD4, Data.DieFace.GOLD4, Data.DieFace.GOLD4, Data.DieFace.GOLD4],
                       [Data.DieFace.SUN1, Data.DieFace.SUN1, Data.DieFace.SUN1, Data.DieFace.SUN1],
                       [Data.DieFace.GOLD6, Data.DieFace.VP1SUN1, Data.DieFace.GOLD2MOON1,
                        Data.DieFace.GOLD1SUN1MOON1OR],
                       [Data.DieFace.GOLD3VP2OR, Data.DieFace.GOLD3VP2OR, Data.DieFace.GOLD3VP2OR,
                        Data.DieFace.GOLD3VP2OR],
                       [Data.DieFace.MOON2, Data.DieFace.MOON2, Data.DieFace.MOON2, Data.DieFace.MOON2],
                       [Data.DieFace.SUN2, Data.DieFace.SUN2, Data.DieFace.SUN2, Data.DieFace.SUN2],
                       [Data.DieFace.VP3, Data.DieFace.VP3, Data.DieFace.VP3, Data.DieFace.VP3],
                       [Data.DieFace.VP4, Data.DieFace.MOON2VP2, Data.DieFace.GOLD1SUN1MOON1VP1,
                        Data.DieFace.GOLD2SUN2MOON2OR])
        self.shields = [Data.DieFace.REDSHIELD, Data.DieFace.YELLOWSHIELD, Data.DieFace.GREENSHIELD,
                        Data.DieFace.BLUESHIELD]
        self.islands = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        self.cerberus = False
        self.islandChoice = 0  # used to remember choice for ousting
        self.selectRandomFeats()
        self.round = 1
        self.activePlayer = 0
        self.blessingPlayer = 0  # player currently resolving a blessing
        self.misfortunePlayer = 0  # player currently using misfortune effect
        self.faceToForge = None  # boar or misfortune face
        self.cyclops = False
        self.sentinel = False
        self.extraRolls = 0
        self.lastPlayer = 0 # player who last made a move
        self.phase = Phase.TURN_START
        self.returnPhase = Phase.TURN_START  # phase to return to after resolving dice effects
        if initialState:
            self.makeMove((Move.PASS, 0, ()))

    def copyState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = BoardState(copyPlayers, False)
        ret.temple = copy.deepcopy(self.temple)
        ret.shields = copy.deepcopy(self.shields)
        ret.islands = copy.deepcopy(self.islands)
        ret.cerberus = self.cerberus
        ret.islandChoice = self.islandChoice
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.blessingPlayer = self.blessingPlayer
        ret.misfortunePlayer = self.misfortunePlayer
        ret.faceToForge = self.faceToForge
        ret.phase = self.phase
        ret.returnPhase = self.returnPhase
        ret.sentinel = self.sentinel
        ret.cyclops = self.cyclops
        ret.extraRolls = self.extraRolls
        ret.lastPlayer = self.lastPlayer
        return ret

    """def copyLoggingState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = LoggingBoardState(copyPlayers, False)
        ret.temple = copy.deepcopy(self.temple)
        ret.shields = copy.deepcopy(self.shields)
        ret.islands = copy.deepcopy(self.islands)
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
        ret.lastPlayer = self.lastPlayer
        return ret"""

    def isOver(self):
        return self.round > 10

    def makeMove(self, move):
        #print(f"Round: {self.round}, Phase: {self.phase}. Making move: {move}. Islands: {self.islands}. Island Choice: {self.islandChoice}")
        #self.printBoardState()
        self.lastPlayer = move[1]
        match self.phase:
            case Phase.TURN_START:
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.ROLL_DIE_1
                self.returnPhase = Phase.USE_TWINS_CHOICE
            case Phase.ROLL_DIE_1:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    self.phase = Phase.ROLL_DIE_2
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die1.roll()
                    self.phase = Phase.ROLL_DIE_2
            case Phase.ROLL_DIE_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.players[self.blessingPlayer].populateTwins()
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.ROLL_DIE_1
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.players[self.blessingPlayer].populateTwins()
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.ROLL_DIE_1
            case Phase.BLESSING_ROLL_DIE_1:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    self.phase = Phase.BLESSING_ROLL_DIE_2
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die1.roll()
                    self.phase = Phase.BLESSING_ROLL_DIE_2
            case Phase.BLESSING_ROLL_DIE_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    self.players[self.blessingPlayer].populateTwins()
                    self.phase = Phase.USE_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    self.players[self.blessingPlayer].populateTwins()
                    self.phase = Phase.USE_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.USE_TWINS_CHOICE:  # call populateTwins() before entering this state for the first time
                if move[0] == Move.USE_TWINS:
                    if move[2][0]:
                        self.players[self.blessingPlayer].gainGold(-3)
                        self.players[self.blessingPlayer].twinsToUse -= 1
                        self.phase = Phase.TWINS_REROLL_CHOICE
                    else:
                        self.phase = Phase.USE_CERBERUS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].twinsToUse == 0 or self.players[self.blessingPlayer].gold < 3:
                    self.phase = Phase.USE_CERBERUS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.TWINS_REROLL_CHOICE:
                if move[0] == Move.USE_TWINS:
                    if move[2][0] == 1:
                        self.phase = Phase.TWINS_REROLL_1
                    else:
                        self.phase = Phase.TWINS_REROLL_2
            case Phase.TWINS_REROLL_1:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    if self.players[self.blessingPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.blessingPlayer].gainVP(1)
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.TWINS_RESOURCE_CHOICE
            case Phase.TWINS_REROLL_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    if self.players[self.blessingPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.blessingPlayer].gainVP(1)
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.TWINS_RESOURCE_CHOICE
            case Phase.TWINS_RESOURCE_CHOICE:
                if move[0] == Move.USE_TWINS:
                    if move[2][0] == "vp":
                        self.players[self.blessingPlayer].gainVP(1)
                    else:
                        self.players[self.blessingPlayer].gainMoon(1)
                    self.phase = Phase.USE_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.USE_CERBERUS_CHOICE:
                if move[0] == Move.USE_CERBERUS:
                    if move[2][0]:
                        self.players[self.blessingPlayer].cerberusTokens -= 1
                        self.cerberus = True
                    self.players[self.blessingPlayer].setBuffers()
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].cerberusTokens == 0:
                    self.players[self.blessingPlayer].setBuffers()
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MIRROR_1_CHOICE:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.blessingPlayer].mirrorChoice1 = move[2][0]
                    self.phase = Phase.MIRROR_2_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].getDie1UpFace() != Data.DieFace.MIRROR:
                    self.phase = Phase.MIRROR_2_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MIRROR_2_CHOICE:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.blessingPlayer].mirrorChoice2 = move[2][0]
                    self.phase = Phase.DIE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].getDie2UpFace() != Data.DieFace.MIRROR:
                    self.phase = Phase.DIE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.DIE_1_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.blessingPlayer].orChoice1 = move[2][0]
                    self.phase = Phase.DIE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.blessingPlayer].getDie1Result()):
                    self.phase = Phase.DIE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.DIE_2_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.blessingPlayer].orChoice2 = move[2][0]
                    if self.sentinel:
                        self.phase = Phase.DIE_1_CHOOSE_SENTINEL
                    else:
                        self.phase = Phase.APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.blessingPlayer].getDie2Result()):
                    if self.sentinel:
                        self.phase = Phase.DIE_1_CHOOSE_SENTINEL
                    else:
                        self.phase = Phase.APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.DIE_1_CHOOSE_SENTINEL:
                if move[0] == Move.CHOOSE_USE_SENTINEL:
                    self.players[self.blessingPlayer].sentinel1Choice = move[2][0]
                    self.phase = Phase.DIE_2_CHOOSE_SENTINEL
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].canUseSentinel(True):
                    self.phase = Phase.DIE_2_CHOOSE_SENTINEL
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.DIE_2_CHOOSE_SENTINEL:
                if move[0] == Move.CHOOSE_USE_SENTINEL:
                    self.players[self.blessingPlayer].sentinel2Choice = move[2][0]
                    self.phase = Phase.APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].canUseSentinel(False):
                    self.phase = Phase.APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.APPLY_DICE_EFFECTS:
                self.players[self.blessingPlayer].gainDiceEffects(self.sentinel)
                self.phase = Phase.RESOLVE_MAZE_MOVES
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.ROLL_CELESTIAL_DIE:
                # todo: roll celestial die
                self.phase = Phase.RESOLVE_MAZE_MOVES
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_MAZE_MOVES:
                # todo: make maze moves, just go to next phase until implemented
                if self.players[self.blessingPlayer].shipsToResolve == 0:
                    self.phase = Phase.BOAR_CHOICE_1
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.RESOLVE_SHIPS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.blessingPlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face)
                    self.phase = Phase.RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.blessingPlayer].shipsToResolve -= 1
                    if self.players[self.blessingPlayer].shipsToResolve == 0:
                        self.phase = Phase.BOAR_CHOICE_1
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeFace(move[2])
                    if self.players[self.blessingPlayer].shipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS
                    else:
                        self.phase = Phase.BOAR_CHOICE_1
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.BOAR_CHOICE_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.BOAR_CHOICE_2
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die1IsBoar():
                    self.phase = Phase.BOAR_CHOICE_2
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.BOAR_CHOICE_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.MISFORTUNE_1
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die2IsBoar():
                    self.phase = Phase.MISFORTUNE_1
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice1 = move[2][0]
                    self.phase = Phase.MISFORTUNE_1_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die1IsMisfortune():
                    self.phase = Phase.MISFORTUNE_2  # note: do 2 first since it will always be the misfortune face
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_MIRROR:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.misfortunePlayer].mirrorChoice2 = move[2][0]
                    self.phase = Phase.MISFORTUNE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.misfortunePlayer].die2ResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MISFORTUNE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice2 = move[2][0]
                    self.phase = Phase.MISFORTUNE_1_APPLY_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.misfortunePlayer].getDie2Result()):
                    self.phase = Phase.MISFORTUNE_1_APPLY_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_APPLY_EFFECTS:
                self.players[self.misfortunePlayer].gainDiceEffects(False)
                self.phase = Phase.MISFORTUNE_1_RESOLVE_MAZE_MOVES
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_RESOLVE_MAZE_MOVES:
                # todo: implement maze
                if self.players[self.misfortunePlayer].shipsToResolve == 0:
                    self.phase = Phase.MISFORTUNE_2
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face)
                    self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MISFORTUNE_2
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.misfortunePlayer].forgeFace(move[2])
                    if self.players[self.misfortunePlayer].shipsToResolve > 0:
                        self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.MISFORTUNE_2
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice2 = move[2][0]
                    self.phase = Phase.MISFORTUNE_2_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die1IsMisfortune():
                    self.phase = Phase.CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_MIRROR:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.misfortunePlayer].mirrorChoice1 = move[2][0]
                    self.phase = Phase.MISFORTUNE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.misfortunePlayer].die1ResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MISFORTUNE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice1 = move[2][0]
                    self.phase = Phase.MISFORTUNE_2_APPLY_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.misfortunePlayer].getDie1Result()):
                    self.phase = Phase.MISFORTUNE_2_APPLY_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_APPLY_EFFECTS:
                self.players[self.misfortunePlayer].gainDiceEffects(False)
                self.phase = Phase.MISFORTUNE_2_RESOLVE_MAZE_MOVES
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_RESOLVE_MAZE_MOVES:
                # todo: implement maze
                if self.players[self.misfortunePlayer].shipsToResolve == 0:
                    self.phase = Phase.CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.MISFORTUNE_2_RESOLVE_SHIPS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face)
                    self.phase = Phase.MISFORTUNE_2_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.CERBERUS_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.misfortunePlayer].forgeFace(move[2])
                    if self.players[self.misfortunePlayer].shipsToResolve > 0:
                        self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.CERBERUS_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CERBERUS_DECISION:
                if self.cerberus:
                    self.cerberus = False
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.returnPhase == Phase.USE_TWINS_CHOICE:  # start of turn divine blessings
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.players[self.blessingPlayer].populateTwins()
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.extraRolls > 0:
                    self.extraRolls -= 1
                    self.phase = Phase.BLESSING_ROLL_DIE_1
                else:
                    self.phase = self.returnPhase
                    self.makeReturnMove(move[1])
            case Phase.MINOR_CHOOSE_DIE:
                if move[0] == Move.CHOOSE_DIE:
                    self.players[self.blessingPlayer].dieChoice = move[2][0]
                    self.phase = Phase.MINOR_ROLL_DIE
            case Phase.MINOR_ROLL_DIE:
                if move[0] == Move.ROLL:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    else:
                        self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    self.players[self.blessingPlayer].populateTwins()
                    self.phase = Phase.MINOR_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.RANDOM_ROLL:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.players[self.blessingPlayer].die1.roll()
                    else:
                        self.players[self.blessingPlayer].die2.roll()
                    self.players[self.blessingPlayer].populateTwins()
                    self.phase = Phase.MINOR_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_TWINS_CHOICE:
                if move[0] == Move.USE_TWINS:
                    if move[2][0]:
                        self.players[self.blessingPlayer].gainGold(-3)
                        self.players[self.blessingPlayer].twinsToUse -= 1
                        self.phase = Phase.MINOR_TWINS_REROLL
                    else:
                        self.phase = Phase.MINOR_USE_CERBERUS
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].twinsToUse == 0 or self.players[self.blessingPlayer].gold < 3:
                    self.phase = Phase.MINOR_USE_CERBERUS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_TWINS_REROLL:
                if move[0] == Move.ROLL:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    else:
                        self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    if self.players[self.blessingPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.blessingPlayer].gainVP(1)
                        self.phase = Phase.MINOR_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.MINOR_TWINS_RESOURCE
            case Phase.MINOR_TWINS_RESOURCE:
                if move[0] == Move.USE_TWINS:
                    if move[2][0] == "vp":
                        self.players[self.blessingPlayer].gainVP(1)
                    else:
                        self.players[self.blessingPlayer].gainMoon(1)
                    self.phase = Phase.MINOR_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_USE_CERBERUS:
                if move[0] == Move.USE_CERBERUS:
                    if move[2][0]:
                        self.players[self.blessingPlayer].cerberusTokens -= 1
                        self.cerberus = True
                    self.players[self.blessingPlayer].setBuffers()
                    self.phase = Phase.MINOR_MIRROR_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].cerberusTokens == 0:
                    self.players[self.blessingPlayer].setBuffers()
                    self.phase = Phase.MINOR_MIRROR_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MIRROR_CHOICE:
                if self.players[self.blessingPlayer].dieChoice:
                    if move[0] == Move.MIRROR_CHOICE:
                        self.players[self.blessingPlayer].mirrorChoice1 = move[2][0]
                        self.phase = Phase.MINOR_CHOOSE_OR
                        self.makeMove((Move.PASS, move[1], ()))
                    elif self.players[self.blessingPlayer].getDie1UpFace() != Data.DieFace.MIRROR:
                        self.phase = Phase.MINOR_CHOOSE_OR
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    if move[0] == Move.MIRROR_CHOICE:
                        self.players[self.blessingPlayer].mirrorChoice2 = move[2][0]
                        self.phase = Phase.MINOR_CHOOSE_OR
                        self.makeMove((Move.PASS, move[1], ()))
                    elif self.players[self.blessingPlayer].getDie2UpFace() != Data.DieFace.MIRROR:
                        self.phase = Phase.MINOR_CHOOSE_OR
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_CHOOSE_OR:
                if self.players[self.blessingPlayer].dieChoice:
                    if move[0] == Move.CHOOSE_DIE_OR:
                        self.players[self.blessingPlayer].orChoice1 = move[2][0]
                        self.phase = Phase.APPLY_DICE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                    elif not Data.getIsOr(self.players[self.blessingPlayer].getDie1Result()):
                        self.phase = Phase.APPLY_DICE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    if move[0] == Move.CHOOSE_DIE_OR:
                        self.players[self.blessingPlayer].orChoice2 = move[2][0]
                        self.phase = Phase.APPLY_DICE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                    elif not Data.getIsOr(self.players[self.blessingPlayer].getDie2Result()):
                        self.phase = Phase.APPLY_DICE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.APPLY_DICE_EFFECTS:
                self.players[self.blessingPlayer].gainMinorBlessingEffect()
                self.phase = Phase.MINOR_MAZE_MOVES
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MAZE_MOVES:
                # todo: implement maze
                if self.players[self.blessingPlayer].shipsToResolve == 0:
                    self.phase = Phase.MINOR_BOAR_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.MINOR_RESOLVE_SHIPS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.blessingPlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face)
                    self.phase = Phase.MINOR_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.blessingPlayer].shipsToResolve -= 1
                    if self.players[self.blessingPlayer].shipsToResolve == 0:
                        self.phase = Phase.MINOR_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeFace(move[2])
                    if self.players[self.blessingPlayer].shipsToResolve > 0:
                        self.phase = Phase.MINOR_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.MINOR_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_BOAR_CHOICE:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.MINOR_MISFORTUNE
                    self.makeMove((Move.PASS, move[1], ()))
                elif (self.players[self.blessingPlayer].dieChoice and not self.players[
                    self.blessingPlayer].die1IsBoar()) or (
                        not self.players[self.blessingPlayer].dieChoice and not self.players[
                    self.blessingPlayer].die2IsBoar()):
                    self.phase = Phase.MINOR_MISFORTUNE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE:
                if (self.players[self.blessingPlayer].dieChoice and not self.players[
                    self.blessingPlayer].die1IsMisfortune()) or (
                        not self.players[self.blessingPlayer].dieChoice and not self.players[
                    self.blessingPlayer].die2IsMisfortune()):
                    self.phase = Phase.MINOR_CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.misfortunePlayer = self.decideMisfortunePlayer(
                            self.players[self.blessingPlayer].getDie1Result())
                    else:
                        self.misfortunePlayer = self.decideMisfortunePlayer(
                            self.players[self.blessingPlayer].getDie2Result())
                    self.phase = Phase.MINOR_MISFORTUNE_1_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_1_MIRROR:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.misfortunePlayer].mirrorChoice1 = move[2][0]
                    self.phase = Phase.MINOR_MISFORTUNE_1_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.misfortunePlayer].die1ResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MINOR_MISFORTUNE_1_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_1_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice1 = move[2][0]
                    self.phase = Phase.MINOR_MISFORTUNE_2_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.misfortunePlayer].getDie1Result()):
                    self.phase = Phase.MINOR_MISFORTUNE_2_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_2_MIRROR:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.misfortunePlayer].mirrorChoice2 = move[2][0]
                    self.phase = Phase.MINOR_MISFORTUNE_2_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.misfortunePlayer].die2ResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MINOR_MISFORTUNE_2_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_2_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice2 = move[2][0]
                    self.phase = Phase.MINOR_MISFORTUNE_RESOLVE
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.misfortunePlayer].getDie2Result()):
                    self.phase = Phase.MINOR_MISFORTUNE_RESOLVE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_RESOLVE:
                self.players[self.misfortunePlayer].gainDiceEffects(False)
                self.phase = Phase.MINOR_MISFORTUNE_MAZE
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_MAZE:
                # todo: implement maze
                if self.players[self.misfortunePlayer].shipsToResolve == 0:
                    self.phase = Phase.MINOR_CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.MINOR_MISFORTUNE_SHIPS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face)
                    self.phase = Phase.MINOR_MISFORTUNE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MINOR_CERBERUS_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.misfortunePlayer].forgeFace(move[2])
                    if self.players[self.misfortunePlayer].shipsToResolve > 0:
                        self.phase = Phase.MINOR_MISFORTUNE_SHIPS
                    else:
                        self.phase = Phase.MINOR_CERBERUS_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_CERBERUS_DECISION:
                if self.cerberus:
                    self.cerberus = False
                    self.phase = Phase.MINOR_MIRROR_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = self.returnPhase
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_REINF_EFFECT:
                if not self.players[self.activePlayer].unusedReinfEffects:
                    self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                elif move[0] == Move.CHOOSE_REINF_EFFECT:
                    self.players[self.activePlayer].unusedReinfEffects.remove(move[2][0])
                    self.selectReinfState(move[2][0])
            case Phase.RESOLVE_ELDER_REINF:
                if move[0] == Move.USE_ELDER:
                    if move[2][0]:
                        if self.players[self.activePlayer].gold >= 3:
                            self.players[self.activePlayer].gainGold(-3)
                            self.players[self.activePlayer].gainVP(4)
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove(move)
            case Phase.RESOLVE_OWL_REINF:
                if move[0] == Move.OWL_CHOICE:
                    match move[2][0]:
                        case "gold":
                            self.players[self.activePlayer].gainGold(1)
                        case "sun":
                            self.players[self.activePlayer].gainSun(1)
                        case "moon":
                            self.players[self.activePlayer].gainMoon(1)
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove(move)
            case Phase.RESOLVE_HIND_REINF:
                self.phase = Phase.MINOR_CHOOSE_DIE
                self.blessingPlayer = self.activePlayer
                self.returnPhase = Phase.CHOOSE_REINF_EFFECT
            case Phase.RESOLVE_TREE_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, move[1], ()))  # todo: effect
            case Phase.RESOLVE_MERCHANT_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, move[1], ()))  # todo: effect
            case Phase.RESOLVE_LIGHT_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, move[1], ()))  # todo: effect
            case Phase.RESOLVE_COMPANION_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, move[1], ()))  # todo: effect
            case Phase.ACTIVE_PLAYER_CHOICE_1:
                if move[0] == Move.CHOOSE_BUY_FACES:
                    self.phase = Phase.ACTIVE_PLAYER_BUY_FACES_1
                elif move[0] == Move.CHOOSE_PERFORM_FEAT:
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
            case Phase.ACTIVE_PLAYER_CHOICE_2:
                if move[0] == Move.CHOOSE_BUY_FACES:
                    self.phase = Phase.ACTIVE_PLAYER_BUY_FACES_2
                elif move[0] == Move.CHOOSE_PERFORM_FEAT:
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
            case Phase.EXTRA_TURN_DECISION:
                if move[0] == Move.TAKE_EXTRA_TURN:
                    if move[2][0]:
                        self.players[self.activePlayer].gainSun(-2)
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_2
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                elif self.players[self.activePlayer].sun < 2:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(face)
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    if not self.players[self.activePlayer].unforgedFaces:
                        self.phase = Phase.EXTRA_TURN_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(face)
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    if not self.players[self.activePlayer].unforgedFaces:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                if move[0] == Move.PERFORM_FEAT:
                    island = Data.getIsland(move[2][0])
                    ousted = False
                    for player in self.players:
                        if player.location == island and player.playerID != self.activePlayer:
                            ousted = True
                            self.oust(player, 1)
                            break
                    self.players[self.activePlayer].location = island
                    if ousted:
                        self.islandChoice = Data.getPosition(move[2][0])
                    else:
                        self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                        self.players[self.activePlayer].performFeat(move[2][0])
                        effect = Data.getEffect(move[2][0])
                        if "INST" in effect:
                            self.resolveInstEffect(effect)
                        else:
                            self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.RETURN_TO_FEAT:
                    feat = self.islands[self.islandChoice][0]
                    self.islands[self.islandChoice].remove(feat)
                    self.players[self.activePlayer].performFeat(feat)
                    effect = Data.getEffect(feat)
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                if move[0] == Move.PERFORM_FEAT:
                    island = Data.getIsland(move[2][0])
                    ousted = False
                    for player in self.players:
                        if player.location == island and player.playerID != self.activePlayer:
                            ousted = True
                            self.oust(player, 2)
                            break
                    if ousted:
                        self.islandChoice = Data.getPosition(move[2][0])
                    else:
                        self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                        self.players[self.activePlayer].performFeat(move[2][0])
                        effect = Data.getEffect(move[2][0])
                        if "INST" in effect:
                            self.resolveInstEffect(effect)
                        else:
                            self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.RETURN_TO_FEAT:
                    feat = self.islands[self.islandChoice][0]
                    self.islands[self.islandChoice].remove(feat)
                    self.players[self.activePlayer].performFeat(feat)
                    effect = Data.getEffect(feat)
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_SHIP_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.FORGE_SHIP_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.CHOOSE_SHIELD_FACE_1:
                if move[0] == Move.BUY_FACES:
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_SHIELD_FACE_2:
                if move[0] == Move.BUY_FACES:
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_MIRROR_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.FORGE_MIRROR_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_HELMET_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.FORGE_HELMET_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    self.blessingPlayer = move[2][0]  # use blessing player variable for boar face player
                    self.phase = Phase.FORGE_BOAR_MISFORTUNE_1
            case Phase.FORGE_BOAR_MISFORTUNE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeBoarMisfortuneFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    self.blessingPlayer = move[2][0]  # use blessing player variable for boar face player
                    self.phase = Phase.FORGE_BOAR_MISFORTUNE_2
            case Phase.FORGE_BOAR_MISFORTUNE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeBoarMisfortuneFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.END_TURN:
                self.phase = Phase.TURN_START
                self.advanceActivePlayer()

        # todo: finish

    def getOptions(self):
        # print(self.phase)
        # self.printBoardState()
        ret = ((Move.PASS, self.activePlayer, ()),)
        match self.phase:
            case Phase.ROLL_DIE_1 | Phase.BLESSING_ROLL_DIE_1 | Phase.TWINS_REROLL_1:
                ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die1)
            case Phase.ROLL_DIE_2 | Phase.BLESSING_ROLL_DIE_2 | Phase.TWINS_REROLL_2:
                ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die2)
            case Phase.USE_TWINS_CHOICE | Phase.MINOR_TWINS_CHOICE:
                ret = ((Move.USE_TWINS, self.blessingPlayer, (True,)), (Move.USE_TWINS, self.blessingPlayer, (False,)))
            case Phase.TWINS_REROLL_CHOICE:
                ret = (
                    (Move.TWINS_CHOOSE_DIE, self.blessingPlayer, (1,)),
                    (Move.TWINS_CHOOSE_DIE, self.blessingPlayer, (2,)))
            case Phase.TWINS_RESOURCE_CHOICE | Phase.MINOR_TWINS_RESOURCE:
                ret = ((Move.TWINS_CHOOSE_RESOURCE, self.blessingPlayer, ("vp",)),
                       (Move.TWINS_CHOOSE_RESOURCE, self.blessingPlayer, ("moon",)))
            case Phase.USE_CERBERUS_CHOICE | Phase.MINOR_USE_CERBERUS:
                ret = (
                    (Move.USE_CERBERUS, self.blessingPlayer, (True,)),
                    (Move.USE_CERBERUS, self.blessingPlayer, (False,)))
            case Phase.MIRROR_1_CHOICE | Phase.MIRROR_2_CHOICE | Phase.MINOR_MIRROR_CHOICE:
                ret = self.getMirrorChoices(self.blessingPlayer)
            case Phase.DIE_1_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getDieOptions(True)
            case Phase.DIE_2_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getDieOptions(False)
            case Phase.BOAR_CHOICE_1:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie1Result())
            case Phase.BOAR_CHOICE_2:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie2Result())
            case Phase.MISFORTUNE_1:
                ret = self.generateMisfortune1Choice()
            case Phase.MISFORTUNE_1_CHOOSE_OR | Phase.MINOR_MISFORTUNE_1_OR:
                ret = self.players[self.misfortunePlayer].getDieOptions(False)
            case Phase.MISFORTUNE_2:
                ret = self.generateMisfortune2Choice()
            case Phase.MISFORTUNE_2_CHOOSE_OR | Phase.MINOR_MISFORTUNE_2_OR:
                ret = self.players[self.misfortunePlayer].getDieOptions(True)
            case Phase.MISFORTUNE_1_MIRROR | Phase.MISFORTUNE_2_MIRROR | Phase.MINOR_MISFORTUNE_1_MIRROR | Phase.MINOR_MISFORTUNE_2_MIRROR:
                ret = self.getMirrorChoices(
                    self.blessingPlayer)  # use blessing player since we are copying their effect, todo: do we even need to pass a player?
            case Phase.DIE_1_CHOOSE_SENTINEL | Phase.DIE_2_CHOOSE_SENTINEL:
                ret = (Move.CHOOSE_USE_SENTINEL, self.blessingPlayer, (True, )), (Move.CHOOSE_USE_SENTINEL, self.blessingPlayer, (False, ))
            case Phase.MINOR_CHOOSE_DIE:
                ret = (Move.CHOOSE_DIE, self.blessingPlayer, (True,)), (Move.CHOOSE_DIE, self.blessingPlayer, (False,))
            case Phase.MINOR_ROLL_DIE:
                if self.players[self.blessingPlayer].dieChoice:
                    ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die1)
                else:
                    ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die2)
            case Phase.MINOR_TWINS_REROLL:
                if self.players[self.blessingPlayer].dieChoice:
                    ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die1)
                else:
                    ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die2)
            case Phase.MINOR_CHOOSE_OR:
                if self.players[self.blessingPlayer].dieChoice:
                    ret = self.players[self.blessingPlayer].getDieOptions(True)
                else:
                    ret = self.players[self.blessingPlayer].getDieOptions(False)
            case Phase.MINOR_BOAR_CHOICE:
                if self.players[self.blessingPlayer].dieChoice:
                    ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie1Result())
                else:
                    ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie2Result())
            case Phase.CHOOSE_REINF_EFFECT:
                ret = self.players[self.activePlayer].getReinfOptions()
            case Phase.RESOLVE_ELDER_REINF:
                ret = (Move.USE_ELDER, self.activePlayer, (True,)), (Move.USE_ELDER, self.activePlayer, (False,))
            case Phase.RESOLVE_OWL_REINF:
                ret = ((Move.OWL_CHOICE, self.activePlayer, ("gold",)), (Move.OWL_CHOICE, self.activePlayer, ("sun",)),
                       (Move.OWL_CHOICE, self.activePlayer, ("moon",)))
            case Phase.RESOLVE_HIND_REINF:
                pass  # todo
            case Phase.RESOLVE_TREE_REINF:
                pass  # todo
            case Phase.RESOLVE_MERCHANT_REINF:
                pass  # todo
            case Phase.RESOLVE_LIGHT_REINF:
                pass  # todo
            case Phase.RESOLVE_COMPANION_REINF:
                pass  # todo
            case Phase.ACTIVE_PLAYER_CHOICE_1 | Phase.ACTIVE_PLAYER_CHOICE_2:
                ret = (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ())
            case Phase.ACTIVE_PLAYER_BUY_FACES_1 | Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateBuyFaces(self.players[self.activePlayer].gold)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 | Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                ret = self.generatePerformFeats()
            case Phase.EXTRA_TURN_DECISION:
                ret = (
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (True,)),
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (False,)))
            case Phase.FORGE_SHIP_FACE_1 | Phase.FORGE_SHIP_FACE_2:
                ret = self.generateForgeFace(self.activePlayer)
            case Phase.CHOOSE_SHIELD_FACE_1 | Phase.CHOOSE_SHIELD_FACE_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateChooseShield()
            case Phase.FORGE_MIRROR_FACE_1 | Phase.FORGE_MIRROR_FACE_2:
                ret = self.generateForgeFace(self.activePlayer)
            case Phase.FORGE_HELMET_FACE_1 | Phase.FORGE_HELMET_FACE_2:
                ret = self.generateForgeFace(self.activePlayer)
            case Phase.RESOLVE_SHIPS | Phase.MINOR_RESOLVE_SHIPS:
                ret = self.generateShipBuyFace(self.blessingPlayer)
            case Phase.RESOLVE_SHIPS_FORGE | Phase.MINOR_RESOLVE_SHIPS_FORGE:
                ret = self.generateForgeFace(self.blessingPlayer)
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS | Phase.MISFORTUNE_2_RESOLVE_SHIPS | Phase.MINOR_MISFORTUNE_SHIPS:
                ret = self.generateShipBuyFace(self.misfortunePlayer)
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS_FORGE | Phase.MISFORTUNE_2_RESOLVE_SHIPS_FORGE | Phase.MINOR_MISFORTUNE_SHIPS_FORGE:
                ret = self.generateForgeFace(self.misfortunePlayer)
            case Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1 | Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2:
                ret = []
                for player in self.players:
                    if player.playerID != self.activePlayer:
                        ret.append((Move.CHOOSE_BOAR_PLAYER, self.activePlayer, (player.playerID,)))
                ret = tuple(ret)
            case Phase.FORGE_BOAR_MISFORTUNE_1 | Phase.FORGE_BOAR_MISFORTUNE_2:
                ret = self.generateForgeBoarFace()
            # todo: other actions
        return ret

    def generateBuyFaces(self, gold):
        ret = []
        if gold >= 2:
            if self.temple[0]:
                ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0],)))
            if self.temple[1]:
                ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[1][0],)))
            if gold >= 3:
                if self.temple[2]:
                    ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[2][0],)))
                if self.temple[3]:
                    ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[3][0],)))
                if gold >= 4:
                    for face in self.temple[4]:
                        ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
                    if self.temple[0] and self.temple[1]:
                        ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[1][0])))
                    if gold >= 5:
                        if self.temple[5]:
                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[5][0],)))
                        if self.temple[0] and self.temple[2]:
                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[2][0])))
                        if self.temple[1] and self.temple[2]:
                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[1][0], self.temple[2][0])))
                        if self.temple[0] and self.temple[3]:
                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[3][0])))
                        if self.temple[1] and self.temple[3]:
                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[1][0], self.temple[3][0])))
                        if gold >= 6:
                            if self.temple[6]:
                                ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[6][0],)))
                            if self.temple[2] and self.temple[3]:
                                ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[2][0], self.temple[3][0])))
                            if self.temple[0] and self.temple[4]:
                                for face in self.temple[4]:
                                    ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], face)))
                            if self.temple[1] and self.temple[4]:
                                for face in self.temple[4]:
                                    ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[1][0], face)))
                            if gold >= 7:
                                if self.temple[2] and self.temple[4]:
                                    for face in self.temple[4]:
                                        ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[2][0], face)))
                                if self.temple[3] and self.temple[4]:
                                    for face in self.temple[4]:
                                        ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[3][0], face)))
                                if self.temple[0] and self.temple[5]:
                                    ret.append(
                                        (Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[5][0])))
                                if self.temple[1] and self.temple[5]:
                                    ret.append(
                                        (Move.BUY_FACES, self.activePlayer, (self.temple[1][0], self.temple[5][0])))
                                if self.temple[0] and self.temple[1] and self.temple[2]:
                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                (self.temple[0][0], self.temple[1][0], self.temple[2][0])))
                                if self.temple[0] and self.temple[1] and self.temple[3]:
                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                (self.temple[0][0], self.temple[1][0], self.temple[3][0])))
                                if gold >= 8:
                                    if self.temple[7]:
                                        ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[7][0],)))
                                    if self.temple[8]:
                                        ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[8][0],)))
                                    if len(self.temple[4]) > 1:
                                        i = 0
                                        while i < len(self.temple[4]) - 1:
                                            j = i + 1
                                            while j < len(self.temple[4]):
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[4][i], self.temple[4][j])))
                                                j += 1
                                            i += 1
                                    if self.temple[0] and self.temple[6]:
                                        ret.append(
                                            (Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[6][0])))
                                    if self.temple[1] and self.temple[6]:
                                        ret.append(
                                            (Move.BUY_FACES, self.activePlayer, (self.temple[1][0], self.temple[6][0])))
                                    if self.temple[2] and self.temple[5]:
                                        ret.append(
                                            (Move.BUY_FACES, self.activePlayer, (self.temple[2][0], self.temple[5][0])))
                                    if self.temple[3] and self.temple[5]:
                                        ret.append(
                                            (Move.BUY_FACES, self.activePlayer, (self.temple[3][0], self.temple[5][0])))
                                    if self.temple[0] and self.temple[2] and self.temple[3]:
                                        ret.append((Move.BUY_FACES, self.activePlayer,
                                                    (self.temple[0][0], self.temple[2][0], self.temple[3][0])))
                                    if self.temple[1] and self.temple[2] and self.temple[3]:
                                        ret.append((Move.BUY_FACES, self.activePlayer,
                                                    (self.temple[1][0], self.temple[2][0], self.temple[3][0])))
                                    if self.temple[0] and self.temple[1] and self.temple[4]:
                                        for face in self.temple[4]:
                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                        (self.temple[0][0], self.temple[1][0], face)))
                                    if gold >= 9:
                                        if self.temple[0] and self.temple[1] and self.temple[5]:
                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                        (self.temple[0][0], self.temple[1][0], self.temple[5][0])))
                                        if self.temple[0] and self.temple[2] and self.temple[4]:
                                            for face in self.temple[4]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[2][0], face)))
                                        if self.temple[0] and self.temple[3] and self.temple[4]:
                                            for face in self.temple[4]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[3][0], face)))
                                        if self.temple[1] and self.temple[2] and self.temple[4]:
                                            for face in self.temple[4]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[2][0], face)))
                                        if self.temple[1] and self.temple[3] and self.temple[4]:
                                            for face in self.temple[4]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[3][0], face)))
                                        if self.temple[4] and self.temple[5]:
                                            for face in self.temple[4]:
                                                ret.append(
                                                    (Move.BUY_FACES, self.activePlayer, (face, self.temple[5][0])))
                                        if self.temple[2] and self.temple[6]:
                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                        (self.temple[2][0], self.temple[6][0])))
                                        if self.temple[3] and self.temple[6]:
                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                        (self.temple[3][0], self.temple[6][0])))
                                        if gold >= 10:
                                            if self.temple[0] and self.temple[7]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[7][0])))
                                            if self.temple[1] and self.temple[7]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[7][0])))
                                            if self.temple[0] and self.temple[8]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[8][0])))
                                            if self.temple[1] and self.temple[8]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[8][0])))
                                            if self.temple[0] and self.temple[1] and self.temple[6]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[1][0], self.temple[6][0])))
                                            if self.temple[4] and self.temple[6]:
                                                for face in self.temple[4]:
                                                    ret.append(
                                                        (Move.BUY_FACES, self.activePlayer, (face, self.temple[6][0])))
                                            if self.temple[0] and self.temple[1] and self.temple[2] and self.temple[3]:
                                                ret.append((Move.BUY_FACES, self.activePlayer, (
                                                    self.temple[0][0], self.temple[1][0], self.temple[2][0],
                                                    self.temple[3][0])))
                                            if self.temple[0] and self.temple[2] and self.temple[5]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[2][0], self.temple[5][0])))
                                            if self.temple[1] and self.temple[2] and self.temple[5]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[2][0], self.temple[5][0])))
                                            if self.temple[0] and self.temple[3] and self.temple[5]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[0][0], self.temple[3][0], self.temple[5][0])))
                                            if self.temple[1] and self.temple[3] and self.temple[5]:
                                                ret.append((Move.BUY_FACES, self.activePlayer,
                                                            (self.temple[1][0], self.temple[3][0], self.temple[5][0])))
                                            if self.temple[0] and len(self.temple[4]) > 1:
                                                i = 0
                                                while i < len(self.temple[4]) - 1:
                                                    j = i + 1
                                                    while j < len(self.temple[4]):
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[4][i], self.temple[4][j])))
                                                        j += 1
                                                    i += 1
                                            if self.temple[1] and len(self.temple[4]) > 1:
                                                i = 0
                                                while i < len(self.temple[4]) - 1:
                                                    j = i + 1
                                                    while j < len(self.temple[4]):
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[1][0], self.temple[4][i], self.temple[4][j])))
                                                        j += 1
                                                    i += 1
                                            if self.temple[2] and self.temple[3] and self.temple[4]:
                                                for face in self.temple[4]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[2][0], self.temple[3][0], face)))
                                            if gold >= 11:
                                                if self.temple[2] and self.temple[7]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[2][0], self.temple[7][0])))
                                                if self.temple[3] and self.temple[7]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[3][0], self.temple[7][0])))
                                                if self.temple[2] and self.temple[8]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[2][0], self.temple[8][0])))
                                                if self.temple[3] and self.temple[8]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[3][0], self.temple[8][0])))
                                                if self.temple[2] and len(self.temple[4]) > 1:
                                                    i = 0
                                                    while i < len(self.temple[4]) - 1:
                                                        j = i + 1
                                                        while j < len(self.temple[4]):
                                                            ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                self.temple[2][0], self.temple[4][i],
                                                                self.temple[4][j])))
                                                            j += 1
                                                        i += 1
                                                if self.temple[3] and len(self.temple[4]) > 1:
                                                    i = 0
                                                    while i < len(self.temple[4]) - 1:
                                                        j = i + 1
                                                        while j < len(self.temple[4]):
                                                            ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                self.temple[3][0], self.temple[4][i],
                                                                self.temple[4][j])))
                                                            j += 1
                                                        i += 1
                                                if self.temple[0] and self.temple[2] and self.temple[6]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                        self.temple[0][0], self.temple[2][0], self.temple[6][0])))
                                                if self.temple[1] and self.temple[2] and self.temple[6]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                        self.temple[1][0], self.temple[2][0], self.temple[6][0])))
                                                if self.temple[0] and self.temple[3] and self.temple[6]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                        self.temple[0][0], self.temple[3][0], self.temple[6][0])))
                                                if self.temple[1] and self.temple[3] and self.temple[6]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                        self.temple[1][0], self.temple[3][0], self.temple[6][0])))
                                                if self.temple[5] and self.temple[6]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer,
                                                                (self.temple[5][0], self.temple[6][0])))
                                                if self.temple[0] and len(self.temple[4]) > 1 and self.temple[5]:
                                                    for face in self.temple[4]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer,
                                                                    (self.temple[0][0], face, self.temple[5][0])))
                                                if self.temple[1] and len(self.temple[4]) > 1 and self.temple[5]:
                                                    for face in self.temple[4]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer,
                                                                    (self.temple[1][0], face, self.temple[5][0])))
                                                if self.temple[2] and self.temple[3] and self.temple[5]:
                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                        self.temple[2][0], self.temple[3][0], self.temple[5][0])))
                                                if self.temple[0] and self.temple[1] and self.temple[2] and self.temple[
                                                    4]:
                                                    for face in self.temple[4]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[2][0],
                                                            face)))
                                                if self.temple[0] and self.temple[1] and self.temple[3] and self.temple[
                                                    4]:
                                                    for face in self.temple[4]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[3][0],
                                                            face)))
                                                if gold >= 12:
                                                    for face in self.temple[9]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
                                                    if self.temple[4] and self.temple[7]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (face, self.temple[7][0])))
                                                    if self.temple[4] and self.temple[8]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (face, self.temple[8][0])))
                                                    if self.temple[0] and self.temple[1] and self.temple[7]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[7][0])))
                                                    if self.temple[0] and self.temple[1] and self.temple[8]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[8][0])))
                                                    if self.temple[0] and self.temple[4] and self.temple[6]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (self.temple[0][0], face, self.temple[6][0])))
                                                    if self.temple[1] and self.temple[4] and self.temple[6]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (self.temple[1][0], face, self.temple[6][0])))
                                                    if self.temple[2] and self.temple[3] and self.temple[6]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[2][0], self.temple[3][0], self.temple[6][0])))
                                                    if self.temple[2] and self.temple[4] and self.temple[5]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (self.temple[2][0], face, self.temple[5][0])))
                                                    if self.temple[3] and self.temple[4] and self.temple[5]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer,
                                                                        (self.temple[3][0], face, self.temple[5][0])))
                                                    if self.temple[0] and self.temple[1] and self.temple[2] and \
                                                            self.temple[5]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[2][0],
                                                            self.temple[5][0])))
                                                    if self.temple[0] and self.temple[1] and self.temple[3] and \
                                                            self.temple[5]:
                                                        ret.append((Move.BUY_FACES, self.activePlayer, (
                                                            self.temple[0][0], self.temple[1][0], self.temple[3][0],
                                                            self.temple[5][0])))
                                                    if len(self.temple[4]) > 2:
                                                        i = 0
                                                        while i < len(self.temple[4]) - 2:
                                                            j = i + 1
                                                            while j < len(self.temple[4]) - 1:
                                                                k = j + 1
                                                                while k < len(self.temple[4]):
                                                                    ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                        self.temple[4][i], self.temple[4][j],
                                                                        self.temple[4][k])))
                                                                    k += 1
                                                                j += 1
                                                            i += 1
                                                    if self.temple[0] and self.temple[2] and self.temple[3] and \
                                                            self.temple[4]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                self.temple[0][0], self.temple[2][0], self.temple[3][0],
                                                                face)))
                                                    if self.temple[1] and self.temple[2] and self.temple[3] and \
                                                            self.temple[4]:
                                                        for face in self.temple[4]:
                                                            ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                self.temple[1][0], self.temple[2][0], self.temple[3][0],
                                                                face)))
                                                    if self.temple[0] and self.temple[1] and len(self.temple[4]) > 1:
                                                        i = 0
                                                        while i < len(self.temple[4]) - 1:
                                                            j = i + 1
                                                            while j < len(self.temple[4]):
                                                                ret.append((Move.BUY_FACES, self.activePlayer, (
                                                                    self.temple[0][0], self.temple[1][0],
                                                                    self.temple[4][i],
                                                                    self.temple[4][j])))
                                                                j += 1
                                                            i += 1

        # todo, etc
        ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def generateShipBuyFace(self, player):
        ret = []
        gold = self.players[player].gold + 2
        if gold >= 2:
            if self.temple[0]:
                ret.append((Move.BUY_FACES, player, (self.temple[0][0],)))
            if self.temple[1]:
                ret.append((Move.BUY_FACES, player, (self.temple[1][0],)))
            if gold >= 3:
                if self.temple[2]:
                    ret.append((Move.BUY_FACES, player, (self.temple[2][0],)))
                if self.temple[3]:
                    ret.append((Move.BUY_FACES, player, (self.temple[3][0],)))
                if gold >= 4:
                    for face in self.temple[4]:
                        ret.append((Move.BUY_FACES, player, (face,)))
                    if gold >= 5:
                        if self.temple[5]:
                            ret.append((Move.BUY_FACES, player, (self.temple[5][0],)))
                        if gold >= 6:
                            if self.temple[6]:
                                ret.append((Move.BUY_FACES, player, (self.temple[6][0],)))
                            if gold >= 8:
                                if self.temple[7]:
                                    ret.append((Move.BUY_FACES, player, (self.temple[7][0],)))
                                if self.temple[8]:
                                    ret.append((Move.BUY_FACES, player, (self.temple[8][0],)))
                                if gold >= 12:
                                    for face in self.temple[9]:
                                        ret.append((Move.BUY_FACES, player, (face,)))
        ret.append((Move.PASS, player, ()))
        return tuple(ret)

    def generatePerformFeats(self):
        ret = []
        sun = self.players[self.activePlayer].sun
        moon = self.players[self.activePlayer].moon
        if sun >= 1:
            if self.islands[0]:
                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[0][0],)))
            if self.islands[1]:
                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[1][0],)))
            if sun >= 2:
                if self.islands[2]:
                    ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[2][0],)))
                if sun >= 3:
                    if self.islands[3]:
                        ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[3][0],)))
                    if sun >= 4:
                        if self.islands[4]:
                            ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[4][0],)))
                        if sun >= 5:
                            if self.islands[5]:
                                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[5][0],)))
                            if sun >= 6:
                                if self.islands[6]:
                                    ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[6][0],)))
        if moon >= 1:
            if self.islands[14]:
                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[14][0],)))
            if self.islands[13]:
                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[13][0],)))
            if moon >= 2:
                if self.islands[12]:
                    ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[12][0],)))
                if moon >= 3:
                    if self.islands[11]:
                        ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[11][0],)))
                    if moon >= 4:
                        if self.islands[10]:
                            ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[10][0],)))
                        if moon >= 5:
                            if self.islands[9]:
                                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[9][0],)))
                            if moon >= 6:
                                if self.islands[8]:
                                    ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[8][0],)))
        if sun >= 5 and moon >= 5:
            if self.islands[7]:
                ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[7][0],)))
        ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def generateForgeFace(self, player):
        ret = []
        face = self.players[player].unforgedFaces[0]
        for existingFace in self.players[player].die1.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (1, face, existingFace)))
        for existingFace in self.players[player].die2.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (2, face, existingFace)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def generateForgeBoarFace(self):
        ret = []
        for existingFace in self.players[self.blessingPlayer].die1.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, self.blessingPlayer, (1, self.faceToForge, existingFace)))
        for existingFace in self.players[self.blessingPlayer].die2.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, self.blessingPlayer, (2, self.faceToForge, existingFace)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def generateBoarChoice(self, face):
        match face:
            case Data.DieFace.REDBOAR:
                feat = Data.HeroicFeat.TENACIOUS_BOAR_RED
            case Data.DieFace.BLUEBOAR:
                feat = Data.HeroicFeat.TENACIOUS_BOAR_BLUE
            case Data.DieFace.YELLOWBOAR:
                feat = Data.HeroicFeat.TENACIOUS_BOAR_YELLOW
            case _:
                feat = Data.HeroicFeat.TENACIOUS_BOAR_GREEN
        for p in self.players:
            if p.hasFeat(feat):
                player = p.playerID
                break
        ret = [(Move.BOAR_CHOICE, player, ("vp",))]
        if not self.players[player].hasMaxSun():
            ret.append((Move.BOAR_CHOICE, player, ("sun",)))
        if not self.players[player].hasMaxMoon():
            ret.append((Move.BOAR_CHOICE, player, ("moon",)))
        return tuple(ret)

    def decideMisfortunePlayer(self, face):
        match face:
            case Data.DieFace.REDMISFORTUNE:
                feat = Data.HeroicFeat.MIRROR_OF_MISFORTUNE_RED
            case Data.DieFace.BLUEMISFORTUNE:
                feat = Data.HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE
            case Data.DieFace.YELLOWMISFORTUNE:
                feat = Data.HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW
            case _:
                feat = Data.HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN
        for p in self.players:
            if p.hasFeat(feat):
                return p.playerID

    def generateMisfortune1Choice(self):  # misfortune face on die 1
        self.misfortunePlayer = self.decideMisfortunePlayer(self.players[self.blessingPlayer].getDie1Result())
        self.players[self.misfortunePlayer].die1ResultBuffer = self.players[self.blessingPlayer].getDie1Result()
        self.players[self.misfortunePlayer].die2ResultBuffer = self.players[self.blessingPlayer].getDie2Result()
        return self.players[self.misfortunePlayer].getDieOptions(True)

    def generateMisfortune2Choice(self):  # misfortune face on die 2
        self.misfortunePlayer = self.decideMisfortunePlayer(self.players[self.blessingPlayer].getDie2Result())
        self.players[self.misfortunePlayer].die1ResultBuffer = self.players[self.blessingPlayer].getDie1Result()
        self.players[self.misfortunePlayer].die2ResultBuffer = self.players[self.blessingPlayer].getDie2Result()
        return self.players[self.misfortunePlayer].getDieOptions(False)

    def generateChooseShield(self):
        ret = []
        for face in self.shields:
            ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
        return tuple(ret)

    def resolveShield(self, player, die):
        if die == 1:
            result = self.players[player].getDie2UpFace()
            other = self.players[player].getDie1UpFace()
        else:
            result = self.players[player].getDie1UpFace()
            other = self.players[player].getDie2UpFace()
        if result == Data.DieFace.REDSHIELD:
            if other == Data.DieFace.TIMES3:
                self.players[player].gainSun(6)
            elif Data.getResourceValues(other)[1] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainSun(2)
        elif result == Data.DieFace.BLUESHIELD:
            if other == Data.DieFace.TIMES3:
                self.players[player].gainMoon(6)
            elif Data.getResourceValues(other)[2] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif result == Data.DieFace.YELLOWSHIELD:
            if other == Data.DieFace.TIMES3:
                self.players[player].gainGold(9)
            elif Data.getResourceValues(other)[0] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif result == Data.DieFace.GREENSHIELD:
            if other == Data.DieFace.TIMES3:
                self.players[player].gainVP(9)
            elif Data.getResourceValues(other)[3] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainVP(3)

    def resolveShieldOr(self, player, die, orGain):
        if die == Data.DieFace.REDSHIELD:
            if orGain == "sun":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainSun(2)
        elif die == Data.DieFace.BLUESHIELD:
            if orGain == "moon":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif die == Data.DieFace.YELLOWSHIELD:
            if orGain == "gold":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif die == Data.DieFace.GREENSHIELD:
            if orGain == "vp":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainVP(3)

    def generateRollDieOptions(self, player, die):
        faces = {}
        for face in die.faces:
            if face in faces:
                faces[face] = faces[face] + 1
            else:
                faces[face] = 1
        ret = []
        for face, freq in faces.items():
            ret.append((Move.ROLL, player, (face, freq)))
        ret.append((Move.RANDOM_ROLL, player, ()))
        # ret.append((Move.EV_ROLL, player, ())) todo: expected value roll
        return tuple(ret)

    def getMirrorChoices(self, choicePlayer):
        ret = []
        for player in self.players:
            if player.playerID == choicePlayer:
                continue
            if player.getDie1UpFace() == Data.DieFace.MIRROR:
                if self.players[choicePlayer].getDie1UpFace() != Data.DieFace.MIRROR:
                    ret.append(
                        (Move.MIRROR_CHOICE, choicePlayer, (self.players[choicePlayer].getDie1UpFace(),)))
                if self.players[choicePlayer].getDie2UpFace() != Data.DieFace.MIRROR:
                    ret.append(
                        (Move.MIRROR_CHOICE, choicePlayer, (self.players[choicePlayer].getDie2UpFace(),)))
            else:
                ret.append((Move.MIRROR_CHOICE, choicePlayer, (player.getDie1UpFace(),)))
            if player.getDie2UpFace() == Data.DieFace.MIRROR:
                if self.players[choicePlayer].getDie1UpFace() != Data.DieFace.MIRROR:
                    ret.append(
                        (Move.MIRROR_CHOICE, choicePlayer, (self.players[choicePlayer].getDie1UpFace(),)))
                if self.players[choicePlayer].getDie2UpFace() != Data.DieFace.MIRROR:
                    ret.append(
                        (Move.MIRROR_CHOICE, choicePlayer, (self.players[choicePlayer].getDie2UpFace(),)))
            else:
                ret.append((Move.MIRROR_CHOICE, choicePlayer, (player.getDie2UpFace(),)))
        if not ret:  # possible in 2p if both players roll 2 mirrors
            ret.append((Move.MIRROR_CHOICE, choicePlayer, (Data.DieFace.MIRROR,)))  # will give no resources
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def makeReturnMove(self, player):
        self.sentinel = False
        self.cyclops = False
        match self.returnPhase:
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 | Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                self.makeMove((Move.RETURN_TO_FEAT, player, ()))
            case _:
                self.makeMove((Move.PASS, player, ()))

    def selectReinfState(self, effect):
        match effect:
            case "ELDER_REINF":
                self.phase = Phase.RESOLVE_ELDER_REINF
            case "OWL_REINF":
                self.phase = Phase.RESOLVE_OWL_REINF
            case "HIND_REINF":
                self.phase = Phase.RESOLVE_HIND_REINF
            case "TREE_REINF":
                self.phase = Phase.RESOLVE_TREE_REINF
            case "MERCHANT_REINF":
                self.phase = Phase.RESOLVE_MERCHANT_REINF
            case "LIGHT_REINF":
                self.phase = Phase.RESOLVE_LIGHT_REINF
            case "COMPANION_INST_REINF":
                self.phase = Phase.RESOLVE_COMPANION_REINF

    def resolveInstEffect(self, effect):
        match effect:
            case "SPRITS_INST":
                self.players[self.activePlayer].gainGold(3)
                self.players[self.activePlayer].gainMoon(3)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SHIP_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.SHIP)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_SHIP_FACE_1
                else:
                    self.phase = Phase.FORGE_SHIP_FACE_2
            case "SHIELD_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_SHIELD_FACE_1
                else:
                    self.phase = Phase.CHOOSE_SHIELD_FACE_2
            case "MINOTAUR_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "TRITON_INST":  # todo: using triton tokens
                self.players[self.activePlayer].tritonTokens += 1
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "MIRROR_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.MIRROR)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_MIRROR_FACE_1
                else:
                    self.phase = Phase.FORGE_MIRROR_FACE_2
            case "CYCLOPS_INST":
                self.extraRolls = 3
                self.cyclops = True
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.MINOR_CHOOSE_DIE
            case "SPHINX_INST":
                self.extraRolls = 3
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.MINOR_CHOOSE_DIE
            case "TYPHON_INST":
                self.players[self.activePlayer].gainVP(self.players[self.activePlayer].numForged)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SENTINEL_INST":
                self.extraRolls = 1
                self.sentinel = True
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.BLESSING_ROLL_DIE_1
            case "CANCER_INST":
                self.extraRolls = 1
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.BLESSING_ROLL_DIE_1
            case "HELMET_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.TIMES3)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_HELMET_FACE_1
                else:
                    self.phase = Phase.FORGE_HELMET_FACE_2
            case "CERBERUS_INST":
                self.players[self.activePlayer].cerberusTokens += 1
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "BOAR_INST_AUTO_RED":
                self.faceToForge = Data.DieFace.REDBOAR
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "BOAR_INST_AUTO_BLUE":
                self.faceToForge = Data.DieFace.BLUEBOAR
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "BOAR_INST_AUTO_YELLOW":
                self.faceToForge = Data.DieFace.YELLOWBOAR
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "BOAR_INST_AUTO_GREEN":
                self.faceToForge = Data.DieFace.GREENBOAR
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "SATYRS_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "CHEST_INST":
                self.players[self.activePlayer].chestEffect()
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "HAMMER_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "NYMPH_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "OMNISCIENT_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "GOLDSMITH_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "TRIDENT_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "LEFTHAND_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "FIRE_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "TITAN_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "GODDESS_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "RIGHTHAND_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "NIGHT_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "MISTS_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "ANCESTOR_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "WIND_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "DIE_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "COMPANION_INST_REINF":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "SCEPTER_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "MOONGOLEM_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "GREATGOLEM_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "SUNGOLEM_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "TIMEGOLEM_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "MEMORY_INST_AUTO":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "CHAOS_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "DOGGED_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "MISFORTUNE_INST_AUTO_RED":
                self.faceToForge = Data.DieFace.REDMISFORTUNE
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "MISFORTUNE_INST_AUTO_BLUE":
                self.faceToForge = Data.DieFace.BLUEMISFORTUNE
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "MISFORTUNE_INST_AUTO_YELLOW":
                self.faceToForge = Data.DieFace.YELLOWMISFORTUNE
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2
            case "MISFORTUNE_INST_AUTO_GREEN":
                self.faceToForge = Data.DieFace.GREENMISFORTUNE
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_MISFORTUNE_PLAYER_2

    def oust(self, player, actionNum):
        player.location = 0
        self.phase = Phase.BLESSING_ROLL_DIE_1
        self.blessingPlayer = player.playerID
        if actionNum == 1:
            self.returnPhase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
        else:
            self.returnPhase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
        player.checkBears()
        self.players[self.activePlayer].checkBears()

    def advanceActivePlayer(self):
        prevPlayer = self.activePlayer
        self.activePlayer += 1
        if self.activePlayer >= len(self.players):
            self.activePlayer = 0
            self.round += 1
        if not self.isOver():
            self.makeMove((Move.PASS, prevPlayer, ()))

    def getWinners(self):
        ret = []
        scores = self.getScores()
        bestScore = max(scores)
        for player in self.players:
            if player.vp == bestScore:
                ret.append(1)
            else:
                ret.append(0)
        return tuple(ret)

    def getScores(self):
        scores = []
        for player in self.players:
            scores.append(player.vp)
        return tuple(scores)

    def printBoardState(self):
        print(f"Round: {self.round}")
        print(f"Player {self.activePlayer} is the active player.")
        print("Players:")
        for p in self.players:
            p.printPlayerInfo()
        print("Temple Pools:")
        i = 1
        for pool in self.temple:
            print(f"Pool {i}:")
            for face in pool:
                print(face)
            i += 1
        print("Islands:")
        i = 1
        for featPool in self.islands:
            print(f"Feat {i}:")
            if featPool:
                print(f"{featPool[0]} (x{len(featPool)})")
            else:
                print("Empty")
            i += 1

    def printPoints(self):
        print("Victory Points:")
        for player in self.players:
            print(f"Player {player.playerID}: {player.vp}")

    def selectRandomFeats(self):
        i = 0
        while i < 15:
            feats = Data.getFeatsByPosition(i)
            self.addFeat(i, feats[random.randrange(len(feats))])
            i += 1

    def addFeat(self, island, feat):
        if feat == Data.HeroicFeat.TENACIOUS_BOAR:
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_RED)
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_BLUE)
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_GREEN)
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_YELLOW)
        else:
            j = 0
            while j < len(self.players):
                self.islands[island].append(feat)
                j += 1


class Player:
    def __init__(self, playerID, ai):
        self.playerID = playerID
        self.maxGold = 12
        self.maxSun = 6
        self.maxMoon = 6
        self.gold = 0
        self.sun = 0
        self.moon = 0
        self.vp = 0
        self.ancientShards = 0
        self.cerberusTokens = 0
        self.twinsToUse = 0
        self.tritonTokens = 0
        self.die1ResultBuffer = None
        self.die2ResultBuffer = None
        self.mirrorChoice1 = None
        self.mirrorChoice2 = None
        self.orChoice1 = 0
        self.orChoice2 = 0
        self.dieChoice = True
        self.sentinel1Choice = False
        self.sentinel2Choice = False
        self.feats = []
        self.unforgedFaces = []
        self.unusedReinfEffects = []
        self.die1 = createLightDie()
        self.die2 = createDarkDie()
        self.location = 0  # 0 is portal, 1-7 are islands
        self.numForged = 0  # number of faces forged
        self.companions = [0, 0, 0, 0]
        self.hammer = 0
        self.allegiance = 0
        self.mazePosition = 0
        self.mazeMoves = 0
        self.shipsToResolve = 0
        self.celestialRolls = 0
        self.ai = ai

    def copyPlayer(self):
        ret = Player(self.playerID, self.ai)
        ret.maxGold = self.maxGold
        ret.maxSun = self.maxSun
        ret.maxMoon = self.maxMoon
        ret.gold = self.gold
        ret.sun = self.sun
        ret.moon = self.moon
        ret.vp = self.vp
        ret.ancientShards = self.ancientShards
        ret.cerberusTokens = self.cerberusTokens
        ret.twinsToUse = self.twinsToUse
        ret.tritonTokens = self.tritonTokens
        ret.die1ResultBuffer = self.die1ResultBuffer
        ret.die2ResultBuffer = self.die2ResultBuffer
        ret.mirrorChoice1 = self.mirrorChoice1
        ret.mirrorChoice2 = self.mirrorChoice2
        ret.orChoice1 = self.orChoice1
        ret.orChoice2 = self.orChoice2
        ret.dieChoice = self.dieChoice
        ret.sentinel1Choice = self.sentinel2Choice
        ret.sentinel2Choice = self.sentinel2Choice
        ret.feats = copy.deepcopy(self.feats)
        ret.die1 = self.die1.copyDie()
        ret.die2 = self.die2.copyDie()
        ret.location = self.location
        ret.numForged = self.numForged
        ret.unforgedFaces = copy.deepcopy(self.unforgedFaces)
        ret.unusedReinfEffects = copy.deepcopy(self.unusedReinfEffects)
        ret.companions = copy.deepcopy(self.companions)
        ret.hammer = self.hammer
        ret.allegiance = self.allegiance
        ret.mazePosition = self.mazePosition
        ret.mazeMoves = self.mazeMoves
        ret.shipsToResolve = self.shipsToResolve
        ret.celestialRolls = self.celestialRolls
        ret.ai = self.ai
        return ret

    def chestEffect(self):
        self.maxGold += 4
        self.maxSun += 3
        self.maxMoon += 3

    def getDie1UpFace(self):
        return self.die1.getUpFace()

    def getDie2UpFace(self):
        return self.die2.getUpFace()

    def getDie1Result(self):
        if self.die1ResultBuffer == Data.DieFace.MIRROR:
            return self.mirrorChoice1
        return self.die1ResultBuffer

    def getDie2Result(self):
        if self.die2ResultBuffer == Data.DieFace.MIRROR:
            return self.mirrorChoice2
        return self.die2ResultBuffer

    def gainGold(self, amount):
        self.gold = min(self.gold + amount, self.maxGold)

    def gainSun(self, amount):
        self.sun = min(self.sun + amount, self.maxSun)

    def gainMoon(self, amount):
        self.moon = min(self.moon + amount, self.maxMoon)

    def gainVP(self, amount):
        self.vp += amount

    def hasMaxSun(self):
        return self.sun == self.maxSun

    def hasMaxMoon(self):
        return self.moon == self.maxMoon

    def gainAncientShards(self, amount):
        self.ancientShards = min(self.ancientShards + amount, 6)
        # todo: advance on loyalty track

    def gainLoyalty(self, amount):
        pass  # todo: advance on loyalty track

    def getMaxHammer(self):
        ret = 0
        for feat in self.feats:
            if feat == Data.HeroicFeat.THE_BLACKSMITHS_HAMMER:
                ret += 30
        return ret

    def addHammer(self, amount):
        self.hammer = min(self.hammer + amount, self.getMaxHammer())

    def die1IsBoar(self):
        if self.die1ResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorChoice1)
        return Data.isBoarFace(self.die1ResultBuffer)

    def die2IsBoar(self):
        if self.die2ResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorChoice2)
        return Data.isBoarFace(self.die2ResultBuffer)

    def die1IsMisfortune(self):
        if self.die1ResultBuffer == Data.DieFace.MIRROR:
            return Data.isMisfortuneFace(self.mirrorChoice1)
        return Data.isMisfortuneFace(self.die1ResultBuffer)

    def die2IsMisfortune(self):
        if self.die2ResultBuffer == Data.DieFace.MIRROR:
            return Data.isMisfortuneFace(self.mirrorChoice2)
        return Data.isMisfortuneFace(self.die2ResultBuffer)

    def populateTwins(self):
        self.twinsToUse = 0
        for feat in self.feats:
            if feat == Data.HeroicFeat.THE_TWINS:
                self.twinsToUse += 1

    def setBuffers(self):
        self.die1ResultBuffer = self.die1.getUpFace()
        self.die2ResultBuffer = self.die2.getUpFace()

    def gainResource(self, type, amt):
        match type:
            case "gold":
                self.gainGold(amt)
            case "sun":
                self.gainSun(amt)
            case "moon":
                self.gainMoon(amt)
            case "vp":
                self.gainVP(amt)

    def gainMinorBlessingEffect(self): # todo: cyclops
        if self.dieChoice:
            face = self.getDie1Result()
        else:
            face = self.getDie2Result()
        gains = Data.getResourceValues(face)
        if Data.getIsOr(face):
            match self.orChoice1:
                case 0:
                    self.gainGold(gains[0])
                case 1:
                    self.gainSun(gains[1])
                case 2:
                    self.gainMoon(gains[2])
                case 3:
                    self.gainVP(gains[3])
                case 4:
                    self.gainAncientShards(gains[4])
                case 5:
                    self.gainLoyalty(gains[5])
        else:
            self.gainGold(gains[0])
            self.gainSun(gains[1])
            self.gainMoon(gains[2])
            self.gainVP(gains[3])
            self.gainAncientShards(gains[4])
            self.gainLoyalty(gains[5])
        match face:
            case Data.DieFace.REDSHIELD:
                self.gainSun(2)
            case Data.DieFace.BLUESHIELD:
                self.gainMoon(2)
            case Data.DieFace.GREENSHIELD:
                self.gainVP(3)
            case Data.DieFace.YELLOWSHIELD:
                self.gainGold(3)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2)

    def gainDiceEffects(self, sentinel):
        die1 = self.getDie1Result()
        die2 = self.getDie2Result()
        mult = 1
        if die1 == Data.DieFace.TIMES3 or die2 == Data.DieFace.TIMES3:
            mult = 3
        if die1 == Data.DieFace.SHIP:
            self.shipsToResolve += 1
        if die2 == Data.DieFace.SHIP:
            self.shipsToResolve += 1
        if die1 == Data.DieFace.MAZERED or die1 == Data.DieFace.MAZEBLUE:
            self.mazeMoves += 1
        if die2 == Data.DieFace.MAZERED or die2 == Data.DieFace.MAZEBLUE:
            self.mazeMoves += 1
        if (die1 == Data.DieFace.MAZERED and die2 == Data.DieFace.MAZEBLUE) or (
                die2 == Data.DieFace.MAZERED and die1 == Data.DieFace.MAZEBLUE):
            self.celestialRolls += 1
        die1gains = Data.getResourceValues(die1)
        die2gains = Data.getResourceValues(die2)
        gains1 = (0, 0, 0, 0)
        gains2 = (0, 0, 0, 0)
        if Data.getIsOr(die1):
            match self.orChoice1:
                case 0:
                    self.gainGold(die1gains[0] * mult)
                    gains1 = (die1gains[0], 0, 0, 0)
                case 1:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(die1gains[1] * mult * 2)
                    else:
                        self.gainSun(die1gains[1] * mult)
                    gains1 = (0, die1gains[1], 0, 0)
                case 2:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(die1gains[2] * mult * 2)
                    else:
                        self.gainMoon(die1gains[2] * mult)
                    gains1 = (0, 0, die1gains[2], 0)
                case 3:
                    self.gainVP(die1gains[3])
                    gains1 = (0, 0, 0, die1gains[3] * mult)
                case 4:
                    self.gainAncientShards(die1gains[4] * mult)
                case 5:
                    self.gainLoyalty(die1gains[5] * mult)
        else:
            gains1 = die1gains
            self.gainGold(die1gains[0] * mult)
            if sentinel and self.sentinel1Choice:
                self.gainVP(die1gains[1] * mult * 2 + die1gains[2] * mult * 2)
            else:
                self.gainSun(die1gains[1] * mult)
                self.gainMoon(die1gains[2] * mult)
            self.gainVP(die1gains[3] * mult)
            self.gainAncientShards(die1gains[4] * mult)
            self.gainLoyalty(die1gains[5] * mult)
        if Data.getIsOr(die2):
            match self.orChoice2:
                case 0:
                    self.gainGold(die2gains[0] * mult)
                    gains2 = (die2gains[0], 0, 0, 0)
                case 1:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(die2gains[1] * mult * 2)
                    else:
                        self.gainSun(die2gains[1] * mult)
                    gains2 = (0, die2gains[1], 0, 0)
                case 2:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(die2gains[2] * mult * 2)
                    else:
                        self.gainMoon(die2gains[2] * mult)
                    gains2 = (0, 0, die2gains[2], 0)
                case 3:
                    self.gainVP(die2gains[3] * mult)
                    gains2 = (0, 0, 0, die2gains[3])
                case 4:
                    self.gainAncientShards(die2gains[4] * mult)
                case 5:
                    self.gainLoyalty(die2gains[5] * mult)
        else:
            gains2 = die2gains
            self.gainGold(die2gains[0] * mult)
            if sentinel and self.sentinel2Choice:
                self.gainVP(die2gains[1] * mult * 2 + die2gains[2] * mult * 2)
            else:
                self.gainSun(die2gains[1] * mult)
                self.gainMoon(die2gains[2] * mult)
            self.gainVP(die2gains[3] * mult)
            self.gainAncientShards(die2gains[4] * mult)
            self.gainLoyalty(die2gains[5] * mult)
        match die1:
            case Data.DieFace.REDSHIELD:
                if gains2[1] == 0:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainSun(2 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.BLUESHIELD:
                if gains2[2] == 0:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainMoon(2 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.GREENSHIELD:
                if gains2[3] == 0:
                    self.gainVP(3 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.YELLOWSHIELD:
                if gains2[0] == 0:
                    self.gainGold(3 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2 * mult)
                if gains2[1] > 0:
                    self.gainVP(3)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2 * mult)
                if gains2[2] > 0:
                    self.gainVP(3)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2 * mult)
                if gains2[3] > 0:
                    self.gainVP(3)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2 * mult)
                if gains2[0] > 0:
                    self.gainVP(3)
        match die2:
            case Data.DieFace.REDSHIELD:
                if gains1[1] == 0:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainSun(2 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.BLUESHIELD:
                if gains1[2] == 0:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainMoon(2 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.GREENSHIELD:
                if gains1[3] == 0:
                    self.gainVP(3 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.YELLOWSHIELD:
                if gains1[0] == 0:
                    self.gainGold(3 * mult)
                else:
                    self.gainVP(5)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2 * mult)
                if gains1[1] > 0:
                    self.gainVP(3)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2 * mult)
                if gains1[2] > 0:
                    self.gainVP(3)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2 * mult)
                if gains1[3] > 0:
                    self.gainVP(3)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2 * mult)
                if gains1[0] > 0:
                    self.gainVP(3)

    def buyFace(self, face):
        self.gainGold(-Data.getGoldValue(face))
        self.unforgedFaces.append(face)

    def buyFaceShip(self, face):
        self.gainGold(-(Data.getGoldValue(face) - 2))
        self.unforgedFaces.append(face)

    def forgeFace(self, forgeInfo):
        if forgeInfo[0] == 1:
            die = self.die1
        else:
            die = self.die2
        die.faces.remove(forgeInfo[2])
        die.faces.append(forgeInfo[1])
        die.upFace = 5
        self.unforgedFaces.remove(forgeInfo[1])
        self.numForged += 1

    def forgeBoarMisfortuneFace(self, forgeInfo):
        if forgeInfo[0] == 1:
            die = self.die1
        else:
            die = self.die2
        die.faces.remove(forgeInfo[2])
        die.faces.append(forgeInfo[1])
        die.upFace = 5
        self.numForged += 1

    def checkBears(self):
        for feat in self.feats:
            if feat == Data.HeroicFeat.GREAT_BEAR:
                self.gainVP(3)

    def hasFeat(self, feat):
        for myFeat in self.feats:
            if myFeat == feat:
                return True
        return False

    def performFeat(self, feat):
        self.gainSun(-Data.getSunCost(feat))
        self.gainMoon(-Data.getMoonCost(feat))
        self.feats.append(feat)
        self.gainVP(Data.getPoints(feat))
        # todo: instant actions

    def getDieOptions(self, die1):
        # True for die 1, False for die 2
        if die1:
            face = self.getDie1Result()
        else:
            face = self.getDie2Result()
        resources = Data.getResourceValues(face)
        ret = []
        if resources[0] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (0,)))
        if resources[1] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (1,)))
        if resources[2] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (2,)))
        if resources[3] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (3,)))
        if resources[4] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (4,)))
        if resources[5] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, (5,)))
        return tuple(ret)

    def canUseSentinel(self, die1):
        if die1:
            activeDie = self.getDie1Result()
            inactiveDie = self.getDie2Result()
            activeOrChoice = self.orChoice1
            inactiveOrChoice = self.orChoice2
        else:
            activeDie = self.getDie2Result()
            inactiveDie = self.getDie1Result()
            activeOrChoice = self.orChoice2
            inactiveOrChoice = self.orChoice1
        resources = Data.getResourceValues(activeDie)
        if Data.getIsOr(activeDie):
            if (activeOrChoice == 1 and resources[1] > 0) or (activeOrChoice == 2 and resources[2] > 0):
                return True
            return False
        if resources[1] > 0 or resources[2] > 0:
            return True
        match activeDie:
            case Data.DieFace.REDSHIELD:
                if Data.getIsOr(inactiveDie):
                    return not (inactiveOrChoice == 1 and Data.getResourceValues(inactiveDie)[1] > 0)
                else:
                    return Data.getResourceValues(inactiveDie)[1] == 0
            case Data.DieFace.BLUESHIELD:
                if Data.getIsOr(inactiveDie):
                    return not (inactiveOrChoice == 2 and Data.getResourceValues(inactiveDie)[2] > 0)
                else:
                    return Data.getResourceValues(inactiveDie)[2] == 0
        return False

    def hasReinfEffects(self):
        for feat in self.feats:
            if "REINF" in Data.getEffect(feat):
                return True
        return False

    def populateReinfEffects(self):
        for feat in self.feats:
            effect = Data.getEffect(feat)
            if "REINF" in effect:
                self.unusedReinfEffects.append(effect)

    def getReinfOptions(self):
        ret = []
        for effect in self.unusedReinfEffects:
            ret.append((Move.CHOOSE_REINF_EFFECT, self.playerID, (effect,)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def printPlayerInfo(self):
        print(f"Player {self.playerID}:\nGold: {self.gold}/{self.maxGold}\nSun: {self.sun}/{self.maxSun}")
        print(f"Moon: {self.moon}/{self.maxMoon}\nVictory Points: {self.vp}")
        print("Heroic Feats:")
        for feat in self.feats:
            print(feat.name)
        print("Dice:")
        print(self.die1)
        print(self.die2)
        if self.location == 0:
            print("Location: portal")
        else:
            print(f"Location: Island {self.location}")
        print(f"Number of faces forged: {self.numForged}")
        print("Unforged Faces:")
        for face in self.unforgedFaces:
            print(face)


class Die:
    def __init__(self, face1, face2, face3, face4, face5, face6):
        self.faces = [face1, face2, face3, face4, face5, face6]
        self.upFace = 0

    def copyDie(self):
        ret = Die(self.faces[0], self.faces[1], self.faces[2], self.faces[3], self.faces[4], self.faces[5])
        ret.upFace = self.upFace
        return ret

    def getUpFace(self):
        return self.faces[self.upFace]

    def roll(self):
        self.upFace = random.choice(range(0, 6))

    def setToFace(self, face):
        self.upFace = self.faces.index(face)

    def __str__(self):
        ret = ""
        i = 0
        while i <= 5:
            ret += str(self.faces[i]) + " "
            if i == self.upFace:
                ret += "(up) "
            i += 1
        return ret


def createLightDie():
    return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1,
               Data.DieFace.SUN1)


def createDarkDie():
    return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.VP2,
               Data.DieFace.MOON1)
