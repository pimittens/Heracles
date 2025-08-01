import copy
from enum import Enum
import random
import Data


class HeroicFeat(Enum):
    THE_BLACKSMITHS_HAMMER = 1
    THE_BLACKSMITHS_CHEST = 2
    THE_SILVER_HIND = 3
    GREAT_BEAR = 4
    SATYRS = 5
    TENACIOUS_BOAR = 6
    TENACIOUS_BOAR_RED = 7
    TENACIOUS_BOAR_BLUE = 8
    TENACIOUS_BOAR_GREEN = 9
    TENACIOUS_BOAR_YELLOW = 10
    FERRYMAN = 11
    CERBERUS = 12
    HELMET_OF_INVISIBILITY = 13
    CANCER = 14
    SENTINEL = 15
    HYDRA = 16
    TYPHON = 17
    SPHINX = 18
    CYCLOPS = 19
    MIRROR_OF_THE_ABYSS = 20
    GORGON = 21
    TRITON = 22
    MINOTAUR = 23
    THE_GUARDIANS_SHIELD = 24
    THE_GUARDIANS_OWL = 25
    CELESTIAL_SHIP = 26
    WILD_SPIRITS = 27
    THE_ELDER = 28
    THE_TREE = 29
    THE_MERCHANT = 30
    THE_WOOD_NYMPH = 31
    THE_LIGHT = 32
    THE_OMNISCIENT = 33
    THE_GOLDSMITH = 34
    THE_ABYSSAL_TRIDENT = 35
    THE_LEFT_HAND = 36
    THE_ETERNAL_FIRE = 37
    THE_FIRST_TITAN = 38
    THE_GODDESS = 39
    THE_RIGHT_HAND = 40
    THE_ETERNAL_NIGHT = 41
    THE_MISTS = 42
    THE_ANCESTOR = 43
    THE_WIND = 44
    THE_CELESTIAL_DIE = 45
    THE_COMPANION = 46
    THE_BLACKSMITHS_SCEPTER = 47
    THE_TWINS = 48


class DieFace(Enum):
    GOLD1 = 1
    SUN1 = 2
    MOON1 = 3
    VP2 = 4
    GOLD3 = 5
    GOLD4 = 6
    GOLD6 = 7
    GOLD2MOON1 = 8
    VP1SUN1 = 9
    GOLD1SUN1MOON1OR = 10
    GOLD3VP2OR = 11
    MOON2 = 12
    SUN2 = 13
    VP3 = 14
    VP4 = 15
    GOLD1SUN1MOON1VP1 = 16
    MOON2VP2 = 17
    GOLD2SUN2MOON2OR = 18
    MIRROR = 19
    REDSHIELD = 20
    YELLOWSHIELD = 21
    GREENSHIELD = 22
    BLUESHIELD = 23
    REDBOAR = 24
    YELLOWBOAR = 25
    GREENBOAR = 26
    BLUEBOAR = 27
    TIMES3 = 28
    SHIP = 29


class Phase(Enum):
    TURN_START = 1
    RESOLVE_DIE_0_1 = 2
    RESOLVE_DIE_0_2 = 3
    RESOLVE_DIE_1_1 = 4
    RESOLVE_DIE_1_2 = 5
    RESOLVE_DIE_2_1 = 6
    RESOLVE_DIE_2_2 = 7
    RESOLVE_DIE_3_1 = 8
    RESOLVE_DIE_3_2 = 9
    CHOOSE_REINF_EFFECT = 10
    RESOLVE_ELDER_REINF = 11
    RESOLVE_OWL_REINF = 12
    RESOLVE_HIND_REINF = 13
    RESOLVE_TREE_REINF = 14
    RESOLVE_MERCHANT_REINF = 15
    RESOLVE_LIGHT_REINF = 16
    RESOLVE_COMPANION_REINF = 17
    ACTIVE_PLAYER_CHOICE_1 = 18
    ACTIVE_PLAYER_BUY_FACES_1 = 19
    ACTIVE_PLAYER_PERFORM_FEAT_1 = 20
    EXTRA_TURN_DECISION = 21
    ACTIVE_PLAYER_CHOICE_2 = 22
    ACTIVE_PLAYER_BUY_FACES_2 = 23
    ACTIVE_PLAYER_PERFORM_FEAT_2 = 24
    FORGE_SHIP_FACE_1 = 25
    FORGE_SHIP_FACE_2 = 26
    CHOOSE_SHIELD_FACE_1 = 27
    CHOOSE_SHIELD_FACE_2 = 28
    FORGE_HELMET_FACE_1 = 29
    FORGE_HELMET_FACE_2 = 30
    FORGE_MIRROR_FACE_1 = 31
    FORGE_MIRROR_FACE_2 = 32
    OUST_1_0_1 = 33  # action number, player ID, die number
    OUST_1_0_2 = 34
    OUST_1_1_1 = 35
    OUST_1_1_2 = 36
    OUST_1_2_1 = 37
    OUST_1_2_2 = 38
    OUST_1_3_1 = 39
    OUST_1_3_2 = 40
    OUST_2_0_1 = 41
    OUST_2_0_2 = 42
    OUST_2_1_1 = 43
    OUST_2_1_2 = 44
    OUST_2_2_1 = 45
    OUST_2_2_2 = 46
    OUST_2_3_1 = 47
    OUST_2_3_2 = 48
    RESOLVE_SHIPS_0 = 49
    RESOLVE_SHIPS_1 = 50
    RESOLVE_SHIPS_2 = 51
    RESOLVE_SHIPS_3 = 52
    CHOOSE_BOAR_PLAYER_RED_1 = 53
    CHOOSE_BOAR_PLAYER_BLUE_1 = 54
    CHOOSE_BOAR_PLAYER_YELLOW_1 = 55
    CHOOSE_BOAR_PLAYER_GREEN_1 = 56
    CHOOSE_BOAR_PLAYER_RED_2 = 57
    CHOOSE_BOAR_PLAYER_BLUE_2 = 58
    CHOOSE_BOAR_PLAYER_YELLOW_2 = 59
    CHOOSE_BOAR_PLAYER_GREEN_2 = 60
    FORGE_RED_BOAR_0_1 = 61  # player id, action number
    FORGE_RED_BOAR_1_1 = 62
    FORGE_RED_BOAR_2_1 = 63
    FORGE_RED_BOAR_3_1 = 64
    FORGE_BLUE_BOAR_0_1 = 65
    FORGE_BLUE_BOAR_1_1 = 66
    FORGE_BLUE_BOAR_2_1 = 67
    FORGE_BLUE_BOAR_3_1 = 68
    FORGE_YELLOW_BOAR_0_1 = 69
    FORGE_YELLOW_BOAR_1_1 = 70
    FORGE_YELLOW_BOAR_2_1 = 71
    FORGE_YELLOW_BOAR_3_1 = 72
    FORGE_GREEN_BOAR_0_1 = 73
    FORGE_GREEN_BOAR_1_1 = 74
    FORGE_GREEN_BOAR_2_1 = 75
    FORGE_GREEN_BOAR_3_1 = 76
    FORGE_RED_BOAR_0_2 = 77
    FORGE_RED_BOAR_1_2 = 78
    FORGE_RED_BOAR_2_2 = 79
    FORGE_RED_BOAR_3_2 = 80
    FORGE_BLUE_BOAR_0_2 = 81
    FORGE_BLUE_BOAR_1_2 = 82
    FORGE_BLUE_BOAR_2_2 = 83
    FORGE_BLUE_BOAR_3_2 = 84
    FORGE_YELLOW_BOAR_0_2 = 85
    FORGE_YELLOW_BOAR_1_2 = 86
    FORGE_YELLOW_BOAR_2_2 = 87
    FORGE_YELLOW_BOAR_3_2 = 88
    FORGE_GREEN_BOAR_0_2 = 89
    FORGE_GREEN_BOAR_1_2 = 90
    FORGE_GREEN_BOAR_2_2 = 91
    FORGE_GREEN_BOAR_3_2 = 92
    BOAR_CHOICE_0_1 = 93
    BOAR_CHOICE_0_2 = 94
    BOAR_CHOICE_1_1 = 95
    BOAR_CHOICE_1_2 = 96
    BOAR_CHOICE_2_1 = 97
    BOAR_CHOICE_2_2 = 98
    BOAR_CHOICE_3_1 = 99
    BOAR_CHOICE_3_2 = 100


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


class BoardState:
    def __init__(self, players, initialState):
        self.players = players
        self.temple = ([DieFace.GOLD3, DieFace.GOLD3, DieFace.GOLD3, DieFace.GOLD3],
                       [DieFace.MOON1, DieFace.MOON1, DieFace.MOON1, DieFace.MOON1],
                       [DieFace.GOLD4, DieFace.GOLD4, DieFace.GOLD4, DieFace.GOLD4],
                       [DieFace.SUN1, DieFace.SUN1, DieFace.SUN1, DieFace.SUN1],
                       [DieFace.GOLD6, DieFace.VP1SUN1, DieFace.GOLD2MOON1, DieFace.GOLD1SUN1MOON1OR],
                       [DieFace.GOLD3VP2OR, DieFace.GOLD3VP2OR, DieFace.GOLD3VP2OR, DieFace.GOLD3VP2OR],
                       [DieFace.MOON2, DieFace.MOON2, DieFace.MOON2, DieFace.MOON2],
                       [DieFace.SUN2, DieFace.SUN2, DieFace.SUN2, DieFace.SUN2],
                       [DieFace.VP3, DieFace.VP3, DieFace.VP3, DieFace.VP3],
                       [DieFace.VP4, DieFace.MOON2VP2, DieFace.GOLD1SUN1MOON1VP1, DieFace.GOLD2SUN2MOON2OR])
        self.shields = [DieFace.REDSHIELD, DieFace.YELLOWSHIELD, DieFace.GREENSHIELD, DieFace.BLUESHIELD]
        self.islands = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        self.shipsToResolve = 0
        self.islandChoice = 0  # used to remember choice for ousting
        self.selectRandomFeats()
        self.round = 1
        self.activePlayer = 0
        self.lastPlayer = 0
        self.phase = Phase.TURN_START
        if initialState:
            self.makeMove((Move.PASS, self.activePlayer, ()))

    def copyState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = BoardState(copyPlayers, False)
        ret.temple = copy.deepcopy(self.temple)
        ret.shields = copy.deepcopy(self.shields)
        ret.islands = copy.deepcopy(self.islands)
        ret.shipsToResolve = self.shipsToResolve
        ret.islandChoice = self.islandChoice
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
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
        print(f"Phase: {self.phase}. Making move: {move}. Islands: {self.islands}. Island Choice: {self.islandChoice}")
        self.printBoardState()
        self.lastPlayer = move[1]
        match self.phase:
            case Phase.TURN_START:
                for player in self.players:
                    player.divineBlessing()
                self.phase = Phase.RESOLVE_DIE_0_1
                self.makeMove(move)
            case Phase.RESOLVE_DIE_0_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie2Result(), move[2][0])
                    if Data.isBoarFace(self.players[0].getDie1Result()):
                        self.phase = Phase.BOAR_CHOICE_0_1
                    else:
                        self.phase = Phase.RESOLVE_DIE_0_2
                        self.makeMove((Move.PASS, 0, ()))
                elif not Data.getIsOr(self.players[0].getDie1Result()):
                    self.players[0].gainDieEffect(1, True)
                    self.resolveShield(0, 2)
                    if self.players[0].getDie1Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    self.phase = Phase.RESOLVE_DIE_0_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_0_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie1Result(), move[2][0])
                    if Data.isBoarFace(self.players[0].getDie2Result()):
                        self.phase = Phase.BOAR_CHOICE_0_2
                    else:
                        self.phase = Phase.RESOLVE_DIE_1_1
                        self.makeMove((Move.PASS, 0, ()))
                elif not Data.getIsOr(self.players[0].getDie2Result()):
                    self.players[0].gainDieEffect(2, True)
                    self.resolveShield(0, 1)
                    if self.players[0].getDie2Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    if self.shipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS_0
                    else:
                        self.phase = Phase.RESOLVE_DIE_1_1
                        self.makeMove(move)
            case Phase.RESOLVE_SHIPS_0:
                pass  # todo
            case Phase.RESOLVE_DIE_1_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie2Result(), move[2][0])
                    if Data.isBoarFace(self.players[1].getDie1Result()):
                        self.phase = Phase.BOAR_CHOICE_1_1
                    else:
                        self.phase = Phase.RESOLVE_DIE_1_2
                        self.makeMove((Move.PASS, 1, ()))
                elif not Data.getIsOr(self.players[1].getDie1Result()):
                    self.players[1].gainDieEffect(1, True)
                    self.resolveShield(1, 2)
                    if self.players[1].getDie1Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    self.phase = Phase.RESOLVE_DIE_1_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_1_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie1Result(), move[2][0])
                    if Data.isBoarFace(self.players[1].getDie2Result()):
                        self.phase = Phase.BOAR_CHOICE_1_2
                    else:
                        if len(self.players) > 2:
                            self.phase = Phase.RESOLVE_DIE_2_1
                            self.makeMove(move)
                        elif self.players[self.activePlayer].hasReinfEffects():
                            self.players[self.activePlayer].populateReinfEffects()
                            self.phase = Phase.CHOOSE_REINF_EFFECT
                        else:
                            self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                        self.makeMove((Move.PASS, 1, ()))
                elif not Data.getIsOr(self.players[1].getDie2Result()):
                    self.players[1].gainDieEffect(2, True)
                    self.resolveShield(1, 1)
                    if self.players[1].getDie2Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    if self.shipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS_1
                    elif len(self.players) > 2:
                        self.phase = Phase.RESOLVE_DIE_2_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_SHIPS_1:
                pass  # todo
            case Phase.RESOLVE_DIE_2_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie2Result(), move[2][0])
                    if Data.isBoarFace(self.players[2].getDie1Result()):
                        self.phase = Phase.BOAR_CHOICE_2_1
                    else:
                        self.phase = Phase.RESOLVE_DIE_2_2
                        self.makeMove((Move.PASS, 2, ()))
                elif not Data.getIsOr(self.players[2].getDie1Result()):
                    self.players[2].gainDieEffect(1, True)
                    self.resolveShield(2, 2)
                    if self.players[2].getDie1Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    self.phase = Phase.RESOLVE_DIE_2_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_2_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie1Result(), move[2][0])
                    if Data.isBoarFace(self.players[2].getDie2Result()):
                        self.phase = Phase.BOAR_CHOICE_2_2
                    else:
                        if len(self.players) > 3:
                            self.phase = Phase.RESOLVE_DIE_3_1
                            self.makeMove(move)
                        elif self.players[self.activePlayer].hasReinfEffects():
                            self.players[self.activePlayer].populateReinfEffects()
                            self.phase = Phase.CHOOSE_REINF_EFFECT
                        else:
                            self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                        self.makeMove((Move.PASS, 2, ()))
                elif not Data.getIsOr(self.players[2].getDie2Result()):
                    self.players[2].gainDieEffect(2, True)
                    self.resolveShield(2, 1)
                    if self.players[2].getDie2Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    if self.shipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS_2
                    elif len(self.players) > 3:
                        self.phase = Phase.RESOLVE_DIE_3_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_SHIPS_2:
                pass  # todo
            case Phase.RESOLVE_DIE_3_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[2].getDie2Result(), move[2][0])
                    if Data.isBoarFace(self.players[3].getDie1Result()):
                        self.phase = Phase.BOAR_CHOICE_3_1
                    else:
                        self.phase = Phase.RESOLVE_DIE_3_2
                        self.makeMove((Move.PASS, 3, ()))
                elif not Data.getIsOr(self.players[3].getDie1Result()):
                    self.players[3].gainDieEffect(1, True)
                    self.resolveShield(3, 2)
                    if self.players[3].getDie1Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    self.phase = Phase.RESOLVE_DIE_3_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_3_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[2].getDie1Result(), move[2][0])
                    if Data.isBoarFace(self.players[3].getDie2Result()):
                        self.phase = Phase.BOAR_CHOICE_3_2
                    else:
                        if self.players[self.activePlayer].hasReinfEffects():
                            self.players[self.activePlayer].populateReinfEffects()
                            self.phase = Phase.CHOOSE_REINF_EFFECT
                        else:
                            self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                        self.makeMove((Move.PASS, 3, ()))
                elif not Data.getIsOr(self.players[3].getDie2Result()):
                    self.players[3].gainDieEffect(2, True)
                    self.resolveShield(3, 1)
                    if self.players[3].getDie2Result() == DieFace.SHIP:
                        self.shipsToResolve += 1
                    if self.shipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS_3
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_SHIPS_3:
                pass  # todo
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
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo: recieve minor blessing
            case Phase.RESOLVE_TREE_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo: effect
            case Phase.RESOLVE_MERCHANT_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo: effect
            case Phase.RESOLVE_LIGHT_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo: effect
            case Phase.RESOLVE_COMPANION_REINF:
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo: effect
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
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(face)
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    if not self.players[self.activePlayer].unforgedFaces:
                        if self.players[self.activePlayer].sun >= 2:
                            self.phase = Phase.EXTRA_TURN_DECISION
                        else:
                            self.phase = Phase.TURN_START
                            self.advanceActivePlayer()
                elif move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
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
                        self.makeMove((Move.PASS, self.activePlayer, ()))
                    else:
                        self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                        self.players[self.activePlayer].performFeat(move[2][0])
                        effect = Data.getEffect(move[2][0])
                        if "INST" in effect:
                            self.resolveInstEffect(effect)
                        else:
                            self.makeMove((Move.PASS, self.activePlayer, ()))
                elif move[0] == Move.RETURN_TO_FEAT:
                    feat = self.islands[self.islandChoice][0]
                    self.islands[self.islandChoice].remove(feat)
                    self.players[self.activePlayer].performFeat(feat)
                    effect = Data.getEffect(feat)
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, self.activePlayer, ()))
                elif move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
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
                        self.makeMove((Move.PASS, self.activePlayer, ()))
                    else:
                        self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                        self.players[self.activePlayer].performFeat(move[2][0])
                        effect = Data.getEffect(move[2][0])
                        if "INST" in effect:
                            self.resolveInstEffect(effect)
                        else:
                            self.makeMove((Move.PASS, self.activePlayer, ()))
                elif move[0] == Move.RETURN_TO_FEAT:
                    feat = self.islands[self.islandChoice][0]
                    self.islands[self.islandChoice].remove(feat)
                    self.players[self.activePlayer].performFeat(feat)
                    effect = Data.getEffect(feat)
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, self.activePlayer, ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_SHIP_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
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
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
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
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.FORGE_MIRROR_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_HELMET_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.FORGE_HELMET_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.OUST_1_0_1:  # todo: ship die face effect
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_1_0_2
                    self.makeMove((Move.PASS, 0, ()))
                elif not Data.getIsOr(self.players[0].getDie1Result()):
                    self.players[0].gainDieEffect(1, True)
                    self.resolveShield(0, 2)
                    self.phase = Phase.OUST_1_0_2
                    self.makeMove(move)
            case Phase.OUST_1_0_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[0].getDie2Result()):
                    self.players[0].gainDieEffect(2, True)
                    self.resolveShield(0, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_2_0_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_2_0_2
                    self.makeMove((Move.PASS, 0, ()))
                elif not Data.getIsOr(self.players[0].getDie1Result()):
                    self.players[0].gainDieEffect(1, True)
                    self.resolveShield(0, 2)
                    self.phase = Phase.OUST_2_0_2
                    self.makeMove(move)
            case Phase.OUST_2_0_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(0, self.players[0].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[0].getDie2Result()):
                    self.players[0].gainDieEffect(2, True)
                    self.resolveShield(0, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_1_1_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_1_1_2
                    self.makeMove((Move.PASS, 1, ()))
                elif not Data.getIsOr(self.players[1].getDie1Result()):
                    self.players[1].gainDieEffect(1, True)
                    self.resolveShield(1, 2)
                    self.phase = Phase.OUST_1_1_2
                    self.makeMove(move)
            case Phase.OUST_1_1_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[1].getDie2Result()):
                    self.players[1].gainDieEffect(2, True)
                    self.resolveShield(1, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_2_1_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_2_1_2
                    self.makeMove((Move.PASS, 1, ()))
                elif not Data.getIsOr(self.players[1].getDie1Result()):
                    self.players[1].gainDieEffect(1, True)
                    self.resolveShield(1, 2)
                    self.phase = Phase.OUST_2_1_2
                    self.makeMove(move)
            case Phase.OUST_2_1_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(1, self.players[1].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[1].getDie2Result()):
                    self.players[1].gainDieEffect(2, True)
                    self.resolveShield(1, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_1_2_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_1_2_2
                    self.makeMove((Move.PASS, 2, ()))
                elif not Data.getIsOr(self.players[2].getDie1Result()):
                    self.players[2].gainDieEffect(1, True)
                    self.resolveShield(2, 2)
                    self.phase = Phase.OUST_1_2_2
                    self.makeMove(move)
            case Phase.OUST_1_2_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[2].getDie2Result()):
                    self.players[2].gainDieEffect(2, True)
                    self.resolveShield(2, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_2_2_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_2_2_2
                    self.makeMove((Move.PASS, 2, ()))
                elif not Data.getIsOr(self.players[2].getDie1Result()):
                    self.players[2].gainDieEffect(1, True)
                    self.resolveShield(2, 2)
                    self.phase = Phase.OUST_2_2_2
                    self.makeMove(move)
            case Phase.OUST_2_2_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(2, self.players[2].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[2].getDie2Result()):
                    self.players[2].gainDieEffect(2, True)
                    self.resolveShield(2, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_1_3_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[3].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_1_3_2
                    self.makeMove((Move.PASS, 3, ()))
                elif not Data.getIsOr(self.players[3].getDie1Result()):
                    self.players[3].gainDieEffect(1, True)
                    self.resolveShield(3, 2)
                    self.phase = Phase.OUST_1_3_2
                    self.makeMove(move)
            case Phase.OUST_1_3_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[3].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[3].getDie2Result()):
                    self.players[3].gainDieEffect(2, True)
                    self.resolveShield(3, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_1
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.OUST_2_3_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[3].getDie2Result(), move[2][0])
                    self.phase = Phase.OUST_2_3_2
                    self.makeMove((Move.PASS, 3, ()))
                elif not Data.getIsOr(self.players[3].getDie1Result()):
                    self.players[3].gainDieEffect(1, True)
                    self.resolveShield(3, 2)
                    self.phase = Phase.OUST_2_3_2
                    self.makeMove(move)
            case Phase.OUST_2_3_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                    self.resolveShieldOr(3, self.players[3].getDie1Result(), move[2][0])
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
                elif not Data.getIsOr(self.players[3].getDie2Result()):
                    self.players[3].gainDieEffect(2, True)
                    self.resolveShield(3, 1)
                    self.phase = Phase.ACTIVE_PLAYER_PERFORM_FEAT_2
                    self.makeMove((Move.RETURN_TO_FEAT, self.activePlayer, ()))
            case Phase.CHOOSE_BOAR_PLAYER_RED_1:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_RED_BOAR_0_1
                        case 1:
                            self.phase = Phase.FORGE_RED_BOAR_1_1
                        case 2:
                            self.phase = Phase.FORGE_RED_BOAR_2_1
                        case 3:
                            self.phase = Phase.FORGE_RED_BOAR_3_1
            case Phase.CHOOSE_BOAR_PLAYER_BLUE_1:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_BLUE_BOAR_0_1
                        case 1:
                            self.phase = Phase.FORGE_BLUE_BOAR_1_1
                        case 2:
                            self.phase = Phase.FORGE_BLUE_BOAR_2_1
                        case 3:
                            self.phase = Phase.FORGE_BLUE_BOAR_3_1
            case Phase.CHOOSE_BOAR_PLAYER_YELLOW_1:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_YELLOW_BOAR_0_1
                        case 1:
                            self.phase = Phase.FORGE_YELLOW_BOAR_1_1
                        case 2:
                            self.phase = Phase.FORGE_YELLOW_BOAR_2_1
                        case 3:
                            self.phase = Phase.FORGE_YELLOW_BOAR_3_1
            case Phase.CHOOSE_BOAR_PLAYER_GREEN_1:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_GREEN_BOAR_0_1
                        case 1:
                            self.phase = Phase.FORGE_GREEN_BOAR_1_1
                        case 2:
                            self.phase = Phase.FORGE_GREEN_BOAR_2_1
                        case 3:
                            self.phase = Phase.FORGE_GREEN_BOAR_3_1
            case Phase.FORGE_RED_BOAR_0_1 | Phase.FORGE_BLUE_BOAR_0_1 | Phase.FORGE_YELLOW_BOAR_0_1 | Phase.FORGE_GREEN_BOAR_0_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[0].forgeBoarFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_1_1 | Phase.FORGE_BLUE_BOAR_1_1 | Phase.FORGE_YELLOW_BOAR_1_1 | Phase.FORGE_GREEN_BOAR_1_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[1].forgeBoarFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_2_1 | Phase.FORGE_BLUE_BOAR_2_1 | Phase.FORGE_YELLOW_BOAR_2_1 | Phase.FORGE_GREEN_BOAR_2_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[2].forgeBoarFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_3_1 | Phase.FORGE_BLUE_BOAR_3_1 | Phase.FORGE_YELLOW_BOAR_3_1 | Phase.FORGE_GREEN_BOAR_3_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[3].forgeBoarFace(move[2])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
            case Phase.CHOOSE_BOAR_PLAYER_RED_2:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_RED_BOAR_0_2
                        case 1:
                            self.phase = Phase.FORGE_RED_BOAR_1_2
                        case 2:
                            self.phase = Phase.FORGE_RED_BOAR_2_2
                        case 3:
                            self.phase = Phase.FORGE_RED_BOAR_3_2
            case Phase.CHOOSE_BOAR_PLAYER_BLUE_2:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_BLUE_BOAR_0_2
                        case 1:
                            self.phase = Phase.FORGE_BLUE_BOAR_1_2
                        case 2:
                            self.phase = Phase.FORGE_BLUE_BOAR_2_2
                        case 3:
                            self.phase = Phase.FORGE_BLUE_BOAR_3_2
            case Phase.CHOOSE_BOAR_PLAYER_YELLOW_2:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_YELLOW_BOAR_0_2
                        case 1:
                            self.phase = Phase.FORGE_YELLOW_BOAR_1_2
                        case 2:
                            self.phase = Phase.FORGE_YELLOW_BOAR_2_2
                        case 3:
                            self.phase = Phase.FORGE_YELLOW_BOAR_3_2
            case Phase.CHOOSE_BOAR_PLAYER_GREEN_2:
                if move[0] == Move.CHOOSE_BOAR_PLAYER:
                    match move[2][0]:
                        case 0:
                            self.phase = Phase.FORGE_GREEN_BOAR_0_2
                        case 1:
                            self.phase = Phase.FORGE_GREEN_BOAR_1_2
                        case 2:
                            self.phase = Phase.FORGE_GREEN_BOAR_2_2
                        case 3:
                            self.phase = Phase.FORGE_GREEN_BOAR_3_2
            case Phase.FORGE_RED_BOAR_0_2 | Phase.FORGE_BLUE_BOAR_0_2 | Phase.FORGE_YELLOW_BOAR_0_2 | Phase.FORGE_GREEN_BOAR_0_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[0].forgeBoarFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_1_2 | Phase.FORGE_BLUE_BOAR_1_2 | Phase.FORGE_YELLOW_BOAR_1_2 | Phase.FORGE_GREEN_BOAR_1_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[1].forgeBoarFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_2_2 | Phase.FORGE_BLUE_BOAR_2_2 | Phase.FORGE_YELLOW_BOAR_2_2 | Phase.FORGE_GREEN_BOAR_2_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[2].forgeBoarFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.FORGE_RED_BOAR_3_2 | Phase.FORGE_BLUE_BOAR_3_2 | Phase.FORGE_YELLOW_BOAR_3_2 | Phase.FORGE_GREEN_BOAR_3_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[3].forgeBoarFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
            case Phase.BOAR_CHOICE_0_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_DIE_0_2
                    self.makeMove((Move.PASS, 0, ()))
            case Phase.BOAR_CHOICE_0_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_DIE_1_1
                    self.makeMove((Move.PASS, 0, ()))
            case Phase.BOAR_CHOICE_1_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_DIE_1_2
                    self.makeMove((Move.PASS, 1, ()))
            case Phase.BOAR_CHOICE_1_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    if len(self.players) > 2:
                        self.phase = Phase.RESOLVE_DIE_2_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                    self.makeMove((Move.PASS, 1, ()))
            case Phase.BOAR_CHOICE_2_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_DIE_2_2
                    self.makeMove((Move.PASS, 2, ()))
            case Phase.BOAR_CHOICE_2_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    if len(self.players) > 3:
                        self.phase = Phase.RESOLVE_DIE_3_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                    self.makeMove((Move.PASS, 2, ()))
            case Phase.BOAR_CHOICE_3_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_DIE_3_2
                    self.makeMove((Move.PASS, 3, ()))
            case Phase.BOAR_CHOICE_3_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1)
                        case "moon":
                            self.players[move[1]].gainMoon(1)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    if self.players[self.activePlayer].hasReinfEffects():
                        self.players[self.activePlayer].populateReinfEffects()
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
                    self.makeMove((Move.PASS, 3, ()))
        # todo: finish

    def getOptions(self):
        print(self.phase)
        # self.printBoardState()
        ret = ((Move.PASS, self.activePlayer, ()),)
        match self.phase:
            case Phase.RESOLVE_DIE_0_1:
                ret = self.players[0].getDieOptions(True)
            case Phase.RESOLVE_DIE_0_2:
                ret = self.players[0].getDieOptions(False)
            case Phase.RESOLVE_DIE_1_1:
                ret = self.players[1].getDieOptions(True)
            case Phase.RESOLVE_DIE_1_2:
                ret = self.players[1].getDieOptions(False)
            case Phase.RESOLVE_DIE_2_1:
                ret = self.players[2].getDieOptions(True)
            case Phase.RESOLVE_DIE_2_2:
                ret = self.players[2].getDieOptions(False)
            case Phase.RESOLVE_DIE_3_1:
                ret = self.players[3].getDieOptions(True)
            case Phase.RESOLVE_DIE_3_2:
                ret = self.players[3].getDieOptions(False)
            case Phase.CHOOSE_REINF_EFFECT:
                ret = self.players[self.activePlayer].getReinfOptions()
            case Phase.RESOLVE_ELDER_REINF:
                ret = ((Move.USE_ELDER, self.activePlayer, (True,)), (Move.USE_ELDER, self.activePlayer, (False,)))
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
                ret = (
                    (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ()))
            case Phase.ACTIVE_PLAYER_BUY_FACES_1 | Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.players[self.activePlayer].unforgedFaces[0])
                else:
                    ret = self.generateBuyFaces(self.players[self.activePlayer].gold)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 | Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                ret = self.generatePerformFeats()
            case Phase.EXTRA_TURN_DECISION:
                ret = (
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (True,)),
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (False,)))
            case Phase.FORGE_SHIP_FACE_1 | Phase.FORGE_SHIP_FACE_2:
                ret = self.generateForgeFace(self.players[self.activePlayer].unforgedFaces[0])
            case Phase.CHOOSE_SHIELD_FACE_1 | Phase.CHOOSE_SHIELD_FACE_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.players[self.activePlayer].unforgedFaces[0])
                else:
                    ret = self.generateChooseShield()
            case Phase.FORGE_MIRROR_FACE_1 | Phase.FORGE_MIRROR_FACE_2:
                ret = self.generateForgeFace(self.players[self.activePlayer].unforgedFaces[0])
            case Phase.FORGE_HELMET_FACE_1 | Phase.FORGE_HELMET_FACE_2:
                ret = self.generateForgeFace(self.players[self.activePlayer].unforgedFaces[0])
            case Phase.RESOLVE_SHIPS_0:
                ret = self.generateShipBuyFace(0)
            case Phase.RESOLVE_SHIPS_1:
                ret = self.generateShipBuyFace(1)
            case Phase.RESOLVE_SHIPS_2:
                ret = self.generateShipBuyFace(2)
            case Phase.RESOLVE_SHIPS_3:
                ret = self.generateShipBuyFace(3)
            case Phase.OUST_1_0_1:
                ret = self.players[0].getDieOptions(True)
            case Phase.OUST_1_0_2:
                ret = self.players[0].getDieOptions(False)
            case Phase.OUST_1_1_1:
                ret = self.players[1].getDieOptions(True)
            case Phase.OUST_1_1_2:
                ret = self.players[1].getDieOptions(False)
            case Phase.OUST_1_2_1:
                ret = self.players[2].getDieOptions(True)
            case Phase.OUST_1_2_2:
                ret = self.players[2].getDieOptions(False)
            case Phase.OUST_1_3_1:
                ret = self.players[3].getDieOptions(True)
            case Phase.OUST_1_3_2:
                ret = self.players[3].getDieOptions(False)
            case Phase.OUST_2_0_1:
                ret = self.players[0].getDieOptions(True)
            case Phase.OUST_2_0_2:
                ret = self.players[0].getDieOptions(False)
            case Phase.OUST_2_1_1:
                ret = self.players[1].getDieOptions(True)
            case Phase.OUST_2_1_2:
                ret = self.players[1].getDieOptions(False)
            case Phase.OUST_2_2_1:
                ret = self.players[2].getDieOptions(True)
            case Phase.OUST_2_2_2:
                ret = self.players[2].getDieOptions(False)
            case Phase.OUST_2_3_1:
                ret = self.players[3].getDieOptions(True)
            case Phase.OUST_2_3_2:
                ret = self.players[3].getDieOptions(False)
            case Phase.CHOOSE_BOAR_PLAYER_RED_1 | Phase.CHOOSE_BOAR_PLAYER_BLUE_1 | Phase.CHOOSE_BOAR_PLAYER_YELLOW_1 | Phase.CHOOSE_BOAR_PLAYER_GREEN_1 | Phase.CHOOSE_BOAR_PLAYER_RED_2 | Phase.CHOOSE_BOAR_PLAYER_BLUE_2 | Phase.CHOOSE_BOAR_PLAYER_YELLOW_2 | Phase.CHOOSE_BOAR_PLAYER_GREEN_2:
                ret = []
                for player in self.players:
                    if player.playerID != self.activePlayer:
                        ret.append((Move.CHOOSE_BOAR_PLAYER, self.activePlayer, (player.playerID,)))
                ret = tuple(ret)
            case Phase.FORGE_RED_BOAR_0_1 | Phase.FORGE_RED_BOAR_0_2:
                ret = self.generateForgeBoarFace(0, DieFace.REDBOAR)
            case Phase.FORGE_RED_BOAR_1_1 | Phase.FORGE_RED_BOAR_1_2:
                ret = self.generateForgeBoarFace(1, DieFace.REDBOAR)
            case Phase.FORGE_RED_BOAR_2_1 | Phase.FORGE_RED_BOAR_2_2:
                ret = self.generateForgeBoarFace(2, DieFace.REDBOAR)
            case Phase.FORGE_RED_BOAR_3_1 | Phase.FORGE_RED_BOAR_3_2:
                ret = self.generateForgeBoarFace(3, DieFace.REDBOAR)
            case Phase.FORGE_BLUE_BOAR_0_1 | Phase.FORGE_BLUE_BOAR_0_2:
                ret = self.generateForgeBoarFace(0, DieFace.BLUEBOAR)
            case Phase.FORGE_BLUE_BOAR_1_1 | Phase.FORGE_BLUE_BOAR_1_2:
                ret = self.generateForgeBoarFace(1, DieFace.BLUEBOAR)
            case Phase.FORGE_BLUE_BOAR_2_1 | Phase.FORGE_BLUE_BOAR_2_2:
                ret = self.generateForgeBoarFace(2, DieFace.BLUEBOAR)
            case Phase.FORGE_BLUE_BOAR_3_1 | Phase.FORGE_BLUE_BOAR_3_2:
                ret = self.generateForgeBoarFace(3, DieFace.BLUEBOAR)
            case Phase.FORGE_YELLOW_BOAR_0_1 | Phase.FORGE_YELLOW_BOAR_0_2:
                ret = self.generateForgeBoarFace(0, DieFace.YELLOWBOAR)
            case Phase.FORGE_YELLOW_BOAR_1_1 | Phase.FORGE_YELLOW_BOAR_1_2:
                ret = self.generateForgeBoarFace(1, DieFace.YELLOWBOAR)
            case Phase.FORGE_YELLOW_BOAR_2_1 | Phase.FORGE_YELLOW_BOAR_2_2:
                ret = self.generateForgeBoarFace(2, DieFace.YELLOWBOAR)
            case Phase.FORGE_YELLOW_BOAR_3_1 | Phase.FORGE_YELLOW_BOAR_3_2:
                ret = self.generateForgeBoarFace(3, DieFace.YELLOWBOAR)
            case Phase.FORGE_GREEN_BOAR_0_1 | Phase.FORGE_GREEN_BOAR_0_2:
                ret = self.generateForgeBoarFace(0, DieFace.GREENBOAR)
            case Phase.FORGE_GREEN_BOAR_1_1 | Phase.FORGE_GREEN_BOAR_1_2:
                ret = self.generateForgeBoarFace(1, DieFace.GREENBOAR)
            case Phase.FORGE_GREEN_BOAR_2_1 | Phase.FORGE_GREEN_BOAR_2_2:
                ret = self.generateForgeBoarFace(2, DieFace.GREENBOAR)
            case Phase.FORGE_GREEN_BOAR_3_1 | Phase.FORGE_GREEN_BOAR_3_2:
                ret = self.generateForgeBoarFace(3, DieFace.GREENBOAR)
            case Phase.BOAR_CHOICE_0_1:
                ret = self.generateBoarChoice(self.players[0].getDie1Result())
            case Phase.BOAR_CHOICE_0_2:
                ret = self.generateBoarChoice(self.players[0].getDie2Result())
            case Phase.BOAR_CHOICE_1_1:
                ret = self.generateBoarChoice(self.players[1].getDie1Result())
            case Phase.BOAR_CHOICE_1_2:
                ret = self.generateBoarChoice(self.players[1].getDie2Result())
            case Phase.BOAR_CHOICE_2_1:
                ret = self.generateBoarChoice(self.players[2].getDie1Result())
            case Phase.BOAR_CHOICE_2_2:
                ret = self.generateBoarChoice(self.players[2].getDie2Result())
            case Phase.BOAR_CHOICE_3_1:
                ret = self.generateBoarChoice(self.players[3].getDie1Result())
            case Phase.BOAR_CHOICE_3_2:
                ret = self.generateBoarChoice(self.players[3].getDie2Result())
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

    def generateForgeFace(self, face):
        ret = []
        for existingFace in self.players[self.activePlayer].die1.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, self.activePlayer, (1, face, existingFace)))
        for existingFace in self.players[self.activePlayer].die2.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, self.activePlayer, (2, face, existingFace)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def generateForgeBoarFace(self, player, face):
        ret = []
        for existingFace in self.players[player].die1.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (1, face, existingFace)))
        for existingFace in self.players[player].die2.faces:
            if not Data.isBoarFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (2, face, existingFace)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def generateBoarChoice(self, face):
        match face:
            case DieFace.REDBOAR:
                feat = HeroicFeat.TENACIOUS_BOAR_RED
            case DieFace.BLUEBOAR:
                feat = HeroicFeat.TENACIOUS_BOAR_BLUE
            case DieFace.YELLOWBOAR:
                feat = HeroicFeat.TENACIOUS_BOAR_YELLOW
            case DieFace.GREENBOAR:
                feat = HeroicFeat.TENACIOUS_BOAR_GREEN
        for p in self.players:
            if p.hasFeat(feat):
                player = p.playerID
                break
        return (Move.BOAR_CHOICE, player, ("sun",)), (Move.BOAR_CHOICE, player, ("moon",)), (
            Move.BOAR_CHOICE, player, ("vp",))

    def generateChooseShield(self):
        ret = []
        for face in self.shields:
            ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
        return tuple(ret)

    def resolveShield(self, player, die):
        if die == 1:
            result = self.players[player].getDie2Result()
            other = self.players[player].getDie1Result()
        else:
            result = self.players[player].getDie1Result()
            other = self.players[player].getDie2Result()
        if result == DieFace.REDSHIELD:
            if other == DieFace.TIMES3:
                self.players[player].gainSun(6)
            elif Data.getResourceValues(other)[1] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainSun(2)
        elif result == DieFace.BLUESHIELD:
            if other == DieFace.TIMES3:
                self.players[player].gainMoon(6)
            elif Data.getResourceValues(other)[2] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif result == DieFace.YELLOWSHIELD:
            if other == DieFace.TIMES3:
                self.players[player].gainGold(9)
            elif Data.getResourceValues(other)[0] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif result == DieFace.GREENSHIELD:
            if other == DieFace.TIMES3:
                self.players[player].gainVP(9)
            elif Data.getResourceValues(other)[3] > 0:
                self.players[player].gainVP(5)
            else:
                self.players[player].gainVP(3)

    def resolveShieldOr(self, player, die, orGain):
        if die == DieFace.REDSHIELD:
            if orGain == "sun":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainSun(2)
        elif die == DieFace.BLUESHIELD:
            if orGain == "moon":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif die == DieFace.YELLOWSHIELD:
            if orGain == "gold":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainMoon(2)
        elif die == DieFace.GREENSHIELD:
            if orGain == "vp":
                self.players[player].gainVP(5)
            else:
                self.players[player].gainVP(3)

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
                self.players[self.activePlayer].unforgedFaces.append(DieFace.SHIP)
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
            case "MIRROR_INST":  # todo: mirror face effect
                self.players[self.activePlayer].unforgedFaces.append(DieFace.MIRROR)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_MIRROR_FACE_1
                else:
                    self.phase = Phase.FORGE_MIRROR_FACE_2
            case "CYCLOPS_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "SPHINX_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "TYPHON_INST":
                self.players[self.activePlayer].gainVP(self.players[self.activePlayer].numForged)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SENTINEL_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "CANCER_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "HELMET_INST":
                self.players[self.activePlayer].unforgedFaces.append(DieFace.TIMES3)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_HELMET_FACE_1
                else:
                    self.phase = Phase.FORGE_HELMET_FACE_2
            case "CERBERUS_INST":  # todo: using cerberus tokens
                self.players[self.activePlayer].cerberusTokens += 1
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "BOAR_INST_AUTO_RED":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_RED_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_RED_2
            case "BOAR_INST_AUTO_BLUE":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_BLUE_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_BLUE_2
            case "BOAR_INST_AUTO_YELLOW":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_YELLOW_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_YELLOW_2
            case "BOAR_INST_AUTO_GREEN":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_GREEN_1
                else:
                    self.phase = Phase.CHOOSE_BOAR_PLAYER_GREEN_2  # todo: will need more cases here
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

    def oust(self, player, actionNum):
        player.location = 0
        player.divineBlessing()  # todo: change all divine blessings when implementing dice rolls as decisions
        if actionNum == 1:
            match player.playerID:
                case 0:
                    self.phase = Phase.OUST_1_0_1
                case 1:
                    self.phase = Phase.OUST_1_1_1
                case 2:
                    self.phase = Phase.OUST_1_2_1
                case 3:
                    self.phase = Phase.OUST_1_3_1
        else:
            match player.playerID:
                case 0:
                    self.phase = Phase.OUST_2_0_1
                case 1:
                    self.phase = Phase.OUST_2_1_1
                case 2:
                    self.phase = Phase.OUST_2_2_1
                case 3:
                    self.phase = Phase.OUST_2_3_1

    def advanceActivePlayer(self):
        self.activePlayer += 1
        if self.activePlayer >= len(self.players):
            self.activePlayer = 0
            self.round += 1
        if not self.isOver():
            self.makeMove((Move.PASS, self.activePlayer, ()))

    def getWinners(self):
        ret = []
        scores = []
        for player in self.players:
            scores.append(player.vp)
        bestScore = max(scores)
        for player in self.players:
            if player.vp == bestScore:
                ret.append(1)
            else:
                ret.append(0)
        return tuple(ret)

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
            self.addFeat(i, feats[random.randrange(len(feats))])  # todo: boars should be distinct
            i += 1

    def addFeat(self, island, feat):
        if feat == HeroicFeat.TENACIOUS_BOAR:
            self.islands[island].append(HeroicFeat.TENACIOUS_BOAR_RED)
            self.islands[island].append(HeroicFeat.TENACIOUS_BOAR_BLUE)
            self.islands[island].append(HeroicFeat.TENACIOUS_BOAR_GREEN)
            self.islands[island].append(HeroicFeat.TENACIOUS_BOAR_YELLOW)
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
        self.cerberusTokens = 0
        self.tritonTokens = 0
        self.feats = []
        self.unforgedFaces = []
        self.unusedReinfEffects = []
        self.die1 = createLightDie()
        self.die2 = createDarkDie()
        self.location = 0  # 0 is portal, 1-7 are islands
        self.numForged = 0  # number of faces forged
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
        ret.cerberusTokens = self.cerberusTokens
        ret.tritonTokens = self.tritonTokens
        ret.feats = copy.deepcopy(self.feats)
        ret.die1 = self.die1.copyDie()
        ret.die2 = self.die2.copyDie()
        ret.location = self.location
        ret.numForged = self.numForged
        ret.unforgedFaces = copy.deepcopy(self.unforgedFaces)
        ret.unusedReinfEffects = copy.deepcopy(self.unusedReinfEffects)
        return ret

    def chestEffect(self):
        self.maxGold += 4
        self.maxSun += 3
        self.maxMoon += 3

    def divineBlessing(self):
        self.die1.roll()
        self.die2.roll()

    def getDie1Result(self):
        return self.die1.getUpFace()

    def getDie2Result(self):
        return self.die2.getUpFace()

    def gainGold(self, amount):
        self.gold += amount
        if self.gold > self.maxGold:
            self.gold = self.maxGold

    def gainSun(self, amount):
        self.sun += amount
        if self.sun > self.maxSun:
            self.sun = self.maxSun

    def gainMoon(self, amount):
        self.moon += amount
        if self.moon > self.maxMoon:
            self.moon = self.maxMoon

    def gainVP(self, amount):
        self.vp += amount

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

    def gainDieEffect(self, dieNum, useOtherDie):
        if dieNum == 1:
            activeFace = self.die1.getUpFace()
            inactiveFace = self.die2.getUpFace()
        else:
            activeFace = self.die2.getUpFace()
            inactiveFace = self.die1.getUpFace()
        mult = 1
        if useOtherDie and inactiveFace == DieFace.TIMES3:
            mult = 3
        gains = Data.getResourceValues(activeFace)
        self.gainGold(gains[0] * mult)
        self.gainSun(gains[1] * mult)
        self.gainMoon(gains[2] * mult)
        self.gainVP(gains[3] * mult)
        match activeFace:
            case DieFace.REDSHIELD:
                if not useOtherDie:
                    self.gainSun(2)
            case DieFace.BLUESHIELD:
                if not useOtherDie:
                    self.gainMoon(2)
            case DieFace.GREENSHIELD:
                if not useOtherDie:
                    self.gainVP(3)
            case DieFace.YELLOWSHIELD:
                if not useOtherDie:
                    self.gainGold(3)
        # todo: other effects

    def buyFace(self, face):
        self.gainGold(-Data.getGoldValue(face))
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

    def forgeBoarFace(self, forgeInfo):
        if forgeInfo[0] == 1:
            die = self.die1
        else:
            die = self.die2
        die.faces.remove(forgeInfo[2])
        die.faces.append(forgeInfo[1])
        die.upFace = 5
        self.numForged += 1

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
            face = self.die1.getUpFace()
        else:
            face = self.die2.getUpFace()
        resources = Data.getResourceValues(face)
        ret = []
        if resources[0] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, ("gold", resources[0])))
        if resources[1] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, ("sun", resources[1])))
        if resources[2] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, ("moon", resources[2])))
        if resources[3] > 0:
            ret.append((Move.CHOOSE_DIE_OR, self.playerID, ("vp", resources[3])))
        return tuple(ret)

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
            if effect not in ret:
                ret.append((Move.CHOOSE_REINF_EFFECT, self.playerID, (effect,)))
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
    return Die(DieFace.GOLD1, DieFace.GOLD1, DieFace.GOLD1, DieFace.GOLD1, DieFace.GOLD1, DieFace.SUN1)


def createDarkDie():
    return Die(DieFace.GOLD1, DieFace.GOLD1, DieFace.GOLD1, DieFace.GOLD1, DieFace.VP2, DieFace.MOON1)
