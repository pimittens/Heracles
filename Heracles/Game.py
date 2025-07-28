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
    FERRYMAN = 7
    CERBERUS = 8
    HELMET_OF_INVISIBILITY = 9
    CANCER = 10
    SENTINEL = 11
    HYDRA = 12
    TYPHON = 13
    SPHINX = 14
    CYCLOPS = 15
    MIRROR_OF_THE_ABYSS = 16
    GORGON = 17
    TRITON = 18
    MINOTAUR = 19
    THE_GUARDIANS_SHIELD = 20
    THE_GUARDIANS_OWL = 21
    CELESTIAL_SHIP = 22
    WILD_SPIRITS = 23
    THE_ELDER = 24
    THE_TREE = 25
    THE_MERCHANT = 26
    THE_WOOD_NYMPH = 27
    THE_LIGHT = 28
    THE_OMNISCIENT = 29
    THE_GOLDSMITH = 30
    THE_ABYSSAL_TRIDENT = 31
    THE_LEFT_HAND = 32
    THE_ETERNAL_FIRE = 33
    THE_FIRST_TITAN = 34
    THE_GODDESS = 35
    THE_RIGHT_HAND = 36
    THE_ETERNAL_NIGHT = 37
    THE_MISTS = 38
    THE_ANCESTOR = 39
    THE_WIND = 40
    THE_CELESTIAL_DIE = 41
    THE_COMPANION = 42
    THE_BLACKSMITHS_SCEPTER = 43
    THE_TWINS = 44


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
    RESOLVE_DIE_1_1 = 2
    RESOLVE_DIE_1_2 = 3
    RESOLVE_DIE_2_1 = 4
    RESOLVE_DIE_2_2 = 5
    RESOLVE_DIE_3_1 = 6
    RESOLVE_DIE_3_2 = 7
    RESOLVE_DIE_4_1 = 8
    RESOLVE_DIE_4_2 = 9
    RESOLVE_REINF_EFFECTS = 10
    ACTIVE_PLAYER_CHOICE_1 = 11
    ACTIVE_PLAYER_BUY_FACES_1 = 12
    ACTIVE_PLAYER_PERFORM_FEAT_1 = 13
    EXTRA_TURN_DECISION = 14
    ACTIVE_PLAYER_CHOICE_2 = 15
    ACTIVE_PLAYER_BUY_FACES_2 = 16
    ACTIVE_PLAYER_PERFORM_FEAT_2 = 17
    OUST = 18


class Move(Enum):
    PASS = 1
    TAKE_EXTRA_TURN = 2
    CHOOSE_BUY_FACES = 3
    CHOOSE_PERFORM_FEAT = 4
    BUY_FACES = 5
    PERFORM_FEAT = 6
    FORGE_FACES = 7
    CHOOSE_DIE_OR = 8


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
        self.islands = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
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
        ret.islands = copy.deepcopy(self.islands)
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
        ret.lastPlayer = self.lastPlayer
        return ret

    def copyLoggingState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = LoggingBoardState(copyPlayers, False)
        ret.temple = copy.deepcopy(self.temple)
        ret.islands = copy.deepcopy(self.islands)
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
        ret.lastPlayer = self.lastPlayer
        return ret

    def isOver(self):
        return self.round > 10

    def makeMove(self, move):
        self.lastPlayer = move[1]
        match self.phase:
            case Phase.TURN_START:
                for player in self.players:
                    player.divineBlessing()
                self.phase = Phase.RESOLVE_DIE_1_1
                self.makeMove(move)
            case Phase.RESOLVE_DIE_1_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[0].getDie1Result()):
                    self.players[0].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_1_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_1_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[0].getDie2Result()):
                    self.players[0].gainDieEffect(2, True)
                    self.phase = Phase.RESOLVE_DIE_2_1
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_2_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[1].getDie1Result()):
                    self.players[1].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_2_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_2_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[1].getDie2Result()):
                    self.players[1].gainDieEffect(2, True)
                    if len(self.players) > 2:
                        self.phase = Phase.RESOLVE_DIE_3_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_DIE_3_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[2].getDie1Result()):
                    self.players[2].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_3_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_3_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[2].getDie2Result()):
                    self.players[2].gainDieEffect(2, True)
                    if len(self.players) > 3:
                        self.phase = Phase.RESOLVE_DIE_4_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_DIE_4_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[3].getDie1Result()):
                    self.players[3].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_4_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_4_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[3].getDie2Result()):
                    self.players[3].gainDieEffect(2, True)
                    if self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_REINF_EFFECTS:
                self.phase = Phase.ACTIVE_PLAYER_CHOICE_1  # todo: implement reinf effects. just go to next phase for now
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
                        if not self.isOver():
                            self.makeMove(move)
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(
                            face)  # todo: right now there is no option to forge the newly bought faces
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        if not self.isOver():
                            self.makeMove(move)
                if move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        if not self.isOver():
                            self.makeMove(move)
            case Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(
                            face)  # todo: right now there is no option to forge the newly bought faces
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFeat(move[2][0])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFeat(move[2][0])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)

        # todo: finish

    def getOptions(self):
        ret = ((Move.PASS, self.activePlayer, ()), )
        match self.phase:
            case Phase.RESOLVE_DIE_1_1:
                ret = self.players[0].getDieOptions(True)
            case Phase.RESOLVE_DIE_1_2:
                ret = self.players[0].getDieOptions(False)
            case Phase.RESOLVE_DIE_2_1:
                ret = self.players[1].getDieOptions(True)
            case Phase.RESOLVE_DIE_2_2:
                ret = self.players[1].getDieOptions(False)
            case Phase.RESOLVE_DIE_3_1:
                ret = self.players[2].getDieOptions(True)
            case Phase.RESOLVE_DIE_3_2:
                ret = self.players[2].getDieOptions(False)
            case Phase.RESOLVE_DIE_4_1:
                ret = self.players[3].getDieOptions(True)
            case Phase.RESOLVE_DIE_4_2:
                ret = self.players[3].getDieOptions(False)
            case Phase.RESOLVE_REINF_EFFECTS:
                ret = self.players[self.activePlayer].getReinfOptions()
            case Phase.ACTIVE_PLAYER_CHOICE_1:
                ret = (
                    (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ()))
            case Phase.ACTIVE_PLAYER_CHOICE_2:
                ret = (
                    (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ()))
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                ret = self.generateBuyFaces()
            case Phase.ACTIVE_PLAYER_BUY_FACES_2:
                ret = self.generateBuyFaces()
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                ret = self.generatePerformFeats()
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                ret = self.generatePerformFeats()
            case Phase.EXTRA_TURN_DECISION:
                ret = (
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (True,)),
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (False,)))
            # todo: other actions
        return ret

    def generateBuyFaces(self):
        # should generate options for every possible face buy or feat
        gold = self.players[self.activePlayer].gold
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
                                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[1][0], face)))
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
        if not ret:
            ret.append((Move.PASS, self.activePlayer, ()))
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
        if not ret:
            ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def advanceActivePlayer(self):
        self.activePlayer += 1
        if self.activePlayer >= len(self.players):
            self.activePlayer = 0
            self.round += 1

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
            self.addFeat(i, feats[random.randrange(len(feats))])
            i += 1

    def addFeat(self, island, feat):
        j = 0
        while j < len(self.players):
            self.islands[island].append(feat)
            j += 1


class LoggingBoardState:
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
        self.islands = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
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
        ret.islands = copy.deepcopy(self.islands)
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
        ret.lastPlayer = self.lastPlayer
        return ret

    def copyLoggingState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = LoggingBoardState(copyPlayers, False)
        ret.temple = copy.deepcopy(self.temple)
        ret.islands = copy.deepcopy(self.islands)
        ret.round = self.round
        ret.activePlayer = self.activePlayer
        ret.phase = self.phase
        ret.lastPlayer = self.lastPlayer
        return ret

    def isOver(self):
        return self.round > 10

    def makeMove(self, move):
        print(f"Current Phase: {self.phase}. Making move: {move}")
        self.printBoardState()
        self.lastPlayer = move[1]
        match self.phase:
            case Phase.TURN_START:
                for player in self.players:
                    player.divineBlessing()
                self.phase = Phase.RESOLVE_DIE_1_1
                self.makeMove(move)
            case Phase.RESOLVE_DIE_1_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[0].getDie1Result()):
                    self.players[0].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_1_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_1_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[0].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[0].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[0].getDie2Result()):
                    self.players[0].gainDieEffect(2, True)
                    self.phase = Phase.RESOLVE_DIE_2_1
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_2_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[1].getDie1Result()):
                    self.players[1].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_2_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_2_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[1].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[1].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[1].getDie2Result()):
                    self.players[1].gainDieEffect(2, True)
                    if len(self.players) > 2:
                        self.phase = Phase.RESOLVE_DIE_3_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_DIE_3_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[2].getDie1Result()):
                    self.players[2].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_3_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_3_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[2].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[2].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[2].getDie2Result()):
                    self.players[2].gainDieEffect(2, True)
                    if len(self.players) > 3:
                        self.phase = Phase.RESOLVE_DIE_4_1
                        self.makeMove(move)
                    elif self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_DIE_4_1:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie2Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[3].getDie1Result()):
                    self.players[3].gainDieEffect(1, True)
                    self.phase = Phase.RESOLVE_DIE_4_2
                    self.makeMove(move)
            case Phase.RESOLVE_DIE_4_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    mult = 1
                    if self.players[3].getDie1Result() == DieFace.TIMES3:
                        mult = 3
                    self.players[3].gainResource(move[2][0], move[2][1] * mult)
                elif not Data.getIsOr(self.players[3].getDie2Result()):
                    self.players[3].gainDieEffect(2, True)
                    if self.players[self.activePlayer].hasReinfEffects():
                        self.phase = Phase.RESOLVE_REINF_EFFECTS
                    else:
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_1
            case Phase.RESOLVE_REINF_EFFECTS:
                self.phase = Phase.ACTIVE_PLAYER_CHOICE_1  # todo: implement reinf effects. just go to next phase for now
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
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(
                            face)  # todo: right now there is no option to forge the newly bought faces
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if move[0] == Move.BUY_FACES:
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.activePlayer].buyFace(
                            face)  # todo: right now there is no option to forge the newly bought faces
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFeat(move[2][0])
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    if self.players[self.activePlayer].sun >= 2:
                        self.phase = Phase.EXTRA_TURN_DECISION
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer()
                        self.makeMove(move)
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFeat(move[2][0])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)
                if move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer()
                    if not self.isOver():
                        self.makeMove(move)

        # todo: finish

    def getOptions(self):
        ret = ((Move.PASS, self.activePlayer, ()), )
        match self.phase:
            case Phase.RESOLVE_DIE_1_1:
                ret = self.players[0].getDieOptions(True)
            case Phase.RESOLVE_DIE_1_2:
                ret = self.players[0].getDieOptions(False)
            case Phase.RESOLVE_DIE_2_1:
                ret = self.players[1].getDieOptions(True)
            case Phase.RESOLVE_DIE_2_2:
                ret = self.players[1].getDieOptions(False)
            case Phase.RESOLVE_DIE_3_1:
                ret = self.players[2].getDieOptions(True)
            case Phase.RESOLVE_DIE_3_2:
                ret = self.players[2].getDieOptions(False)
            case Phase.RESOLVE_DIE_4_1:
                ret = self.players[3].getDieOptions(True)
            case Phase.RESOLVE_DIE_4_2:
                ret = self.players[3].getDieOptions(False)
            case Phase.RESOLVE_REINF_EFFECTS:
                ret = self.players[self.activePlayer].getReinfOptions()
            case Phase.ACTIVE_PLAYER_CHOICE_1:
                ret = (
                    (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ()))
            case Phase.ACTIVE_PLAYER_CHOICE_2:
                ret = (
                    (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ()))
            case Phase.ACTIVE_PLAYER_BUY_FACES_1:
                ret = self.generateBuyFaces()
            case Phase.ACTIVE_PLAYER_BUY_FACES_2:
                ret = self.generateBuyFaces()
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                ret = self.generatePerformFeats()
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                ret = self.generatePerformFeats()
            case Phase.EXTRA_TURN_DECISION:
                ret = (
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (True,)),
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (False,)))
            # todo: other actions
        return ret

    def generateBuyFaces(self):
        # should generate options for every possible face buy or feat
        gold = self.players[self.activePlayer].gold
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
                                            ret.append((Move.BUY_FACES, self.activePlayer, (self.temple[0][0], self.temple[1][0], face)))
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
        if not ret:
            ret.append((Move.PASS, self.activePlayer, ()))
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
        if not ret:
            ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def advanceActivePlayer(self):
        self.activePlayer += 1
        if self.activePlayer >= len(self.players):
            self.activePlayer = 0
            self.round += 1

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
            self.addFeat(i, feats[random.randrange(len(feats))])
            i += 1

    def addFeat(self, island, feat):
        j = 0
        while j < len(self.players):
            self.islands[island].append(feat)
            j += 1


class Player:
    def __init__(self, playerID, ai):
        self.playerID = playerID
        self.gold = 0
        self.sun = 0
        self.moon = 0
        self.vp = 0
        self.feats = []
        self.unforgedFaces = []
        self.die1 = createLightDie()
        self.die2 = createDarkDie()
        self.location = 0  # 0 is portal, 1-7 are islands
        self.numForged = 0  # number of faces forged
        self.ai = ai

    def copyPlayer(self):
        ret = Player(self.playerID, self.ai)
        ret.gold = self.gold
        ret.sun = self.sun
        ret.moon = self.moon
        ret.vp = self.vp
        ret.feats = copy.deepcopy(self.feats)
        ret.die1 = self.die1.copyDie()
        ret.die2 = self.die2.copyDie()
        ret.location = self.location
        ret.numForged = self.numForged
        ret.unforgedFaces = copy.deepcopy(self.unforgedFaces)
        return ret

    def divineBlessing(self):
        self.die1.roll()
        self.die2.roll()

    def getDie1Result(self):
        return self.die1.getUpFace()

    def getDie2Result(self):
        return self.die2.getUpFace()

    def getMaxGold(self):
        # todo: calculate max gold based on feats
        maxGold = 12
        return maxGold

    def getMaxSun(self):
        # todo: calculate max sun based on feats
        maxSun = 6
        return maxSun

    def getMaxMoon(self):
        # todo: calculate max moon based on feats
        maxMoon = 6
        return maxMoon

    def gainGold(self, amount):
        self.gold += amount
        maxGold = self.getMaxGold()
        if self.gold > maxGold:
            self.gold = maxGold

    def gainSun(self, amount):
        self.sun += amount
        maxSun = self.getMaxSun()
        if self.sun > maxSun:
            self.sun = maxSun

    def gainMoon(self, amount):
        self.moon += amount
        maxMoon = self.getMaxMoon()
        if self.moon > maxMoon:
            self.moon = maxMoon

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
        # todo: apply effect

    def buyFace(self, face):
        self.gainGold(-Data.getGoldValue(face))
        self.unforgedFaces.append(face)

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

    def getReinfOptions(self):
        return ((Move.PASS, self.playerID, ()), )  # todo (need to track which ones have been used somehow)

    def printPlayerInfo(self):
        print(f"Player {self.playerID}:\nGold: {self.gold}/{self.getMaxGold()}\nSun: {self.sun}/{self.getMaxSun()}")
        print(f"Moon: {self.moon}/{self.getMaxMoon()}\nVictory Points: {self.vp}")
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
        self.faces = (face1, face2, face3, face4, face5, face6)
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
