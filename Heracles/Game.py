import copy
from enum import Enum
import random
from itertools import combinations

import Data


class Phase(Enum):  # todo: numbers
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
    MISFORTUNE_1 = 22
    MISFORTUNE_1_CHOOSE_OR = 24
    MISFORTUNE_1_APPLY_EFFECTS = 25
    MISFORTUNE_1_RESOLVE_SHIPS = 27
    MISFORTUNE_1_RESOLVE_SHIPS_FORGE = 28
    MISFORTUNE_2 = 29
    MISFORTUNE_2_CHOOSE_OR = 31
    MISFORTUNE_2_APPLY_EFFECTS = 32
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
    MINOR_RESOLVE_EFFECTS = 45
    MINOR_MAZE_MOVES = 46
    MINOR_RESOLVE_SHIPS = 47
    MINOR_RESOLVE_SHIPS_FORGE = 48
    MINOR_BOAR_CHOICE = 49
    MINOR_MISFORTUNE = 50
    MINOR_MISFORTUNE_1_OR = 52
    MINOR_MISFORTUNE_2_OR = 54
    MINOR_MISFORTUNE_RESOLVE = 55
    MINOR_MISFORTUNE_SHIPS = 57
    MINOR_MISFORTUNE_SHIPS_FORGE = 58
    MINOR_CERBERUS_DECISION = 59
    CHOOSE_REINF_EFFECT = 60
    RESOLVE_ELDER_REINF = 61
    RESOLVE_OWL_REINF = 62
    RESOLVE_HIND_REINF = 63
    RESOLVE_TREE_REINF = 64
    RESOLVE_MERCHANT_REINF = 65
    RESOLVE_LIGHT_REINF = 66
    RESOLVE_COMPANION_REINF = 67
    ACTIVE_PLAYER_CHOICE_1 = 68
    ACTIVE_PLAYER_BUY_FACES_1 = 69
    ACTIVE_PLAYER_PERFORM_FEAT_1 = 70
    EXTRA_TURN_DECISION = 71
    ACTIVE_PLAYER_CHOICE_2 = 72
    ACTIVE_PLAYER_BUY_FACES_2 = 73
    ACTIVE_PLAYER_PERFORM_FEAT_2 = 74
    CHOOSE_SHIELD_FACE_1 = 77
    CHOOSE_SHIELD_FACE_2 = 78
    FORGE_FEAT_FACE_1 = 81
    FORGE_FEAT_FACE_2 = 82
    CHOOSE_BOAR_MISFORTUNE_PLAYER_1 = 83
    CHOOSE_BOAR_MISFORTUNE_PLAYER_2 = 84
    FORGE_BOAR_MISFORTUNE_1 = 85
    FORGE_BOAR_MISFORTUNE_2 = 86
    BLESSING_ROLL_DIE_1 = 88
    BLESSING_ROLL_DIE_2 = 89
    END_TURN = 90
    DIE_1_CHOOSE_SENTINEL = 91
    DIE_2_CHOOSE_SENTINEL = 92
    CHOOSE_CYCLOPS = 93
    SATYRS_CHOOSE_DIE_1 = 94
    SATYRS_CHOOSE_DIE_2 = 95
    CHOOSE_CHAOS_FACE_1 = 96
    CHOOSE_CHAOS_FACE_2 = 97
    CHOOSE_DOGGED_FACE_1 = 98
    CHOOSE_DOGGED_FACE_2 = 99
    RESOLVE_GUARDIAN_REINF = 100
    NYMPH_1 = 101
    NYMPH_2 = 102
    TRIDENT_1 = 103
    TRIDENT_2 = 104
    GODDESS_CHOOSE_FACES = 105
    RIGHTHAND_1 = 106
    RIGHTHAND_2 = 107
    WIND_ROLL_DIE_1 = 108
    WIND_ROLL_DIE_2 = 109
    WIND_CHOOSE_RESOURCE = 110
    USE_ANCESTOR = 111
    TITAN_1 = 112
    TITAN_2 = 113
    LEFT_HAND_ROLL_1_1 = 114  # roll die 1, action 1
    LEFT_HAND_ROLL_1_2 = 115  # roll die 1, action 2
    LEFT_HAND_ROLL_2 = 116  # roll die 2
    CHOOSE_MAZE_ORDER = 117
    ROLL_CELESTIAL_DIE = 118
    CELESTIAL_USE_TWINS_CHOICE = 119
    CELESTIAL_TWINS_REROLL = 120
    CELESTIAL_TWINS_RESOURCE_CHOICE = 121
    CELESTIAL_CHOOSE_OR = 122
    CELESTIAL_CHOOSE_MIRROR = 123
    CELESTIAL_CHOOSE_GODDESS = 124
    CELESTIAL_CHOOSE_UPGRADE = 125
    CELESTIAL_RESOLVE_EFFECT = 126
    CELESTIAL_RESOLVE_DIE_MIRROR = 127
    CELESTIAL_RESOLVE_DIE_OR = 128
    CELESTIAL_RESOLVE_DIE_EFFECT = 129
    MISFORTUNE_1_BOAR_CHOICE = 130
    MISFORTUNE_2_BOAR_CHOICE = 131
    CELESTIAL_RESOLVE_SHIPS = 132
    CELESTIAL_RESOLVE_SHIPS_FORGE = 133
    CELESTIAL_BOAR_CHOICE = 134
    CELESTIAL_MISFORTUNE = 135
    MAZE_EFFECT = 136
    MAZE_EFFECT_FACE_BUY = 137
    MAZE_EFFECT_SPEND_GOLD = 138
    MAZE_EFFECT_SPEND_MOON = 139
    MAZE_EFFECT_GODDESS = 140
    MAZE_EFFECT_TREASUREHALL = 141
    MAZE_MIRROR_1 = 142
    MAZE_MIRROR_2 = 143
    MAZE_DIE_1_CHOOSE_OR = 144
    MAZE_DIE_2_CHOOSE_OR = 145
    MAZE_APPLY_DICE_EFFECTS = 146
    MAZE_BOAR_CHOICE_1 = 147
    MAZE_BOAR_CHOICE_2 = 148


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
    CHOOSE_ADD_HAMMER_SCEPTER = 25
    SATYRS_CHOOSE_DIE = 26
    USE_TRITON_TOKEN = 27
    GUARDIAN_CHOICE = 28
    USE_COMPANION = 29
    USE_LIGHT = 30
    SPEND_GOLD = 31
    SPEND_SUN = 32
    SPEND_MOON = 33
    CHOOSE_FACES = 34  # choose faces to place face up
    RIGHTHAND_SPEND = 35  # gain 1 vp per gold spent
    CHOOSE_RESOURCE = 36
    MERCHANT_UPGRADE = 37
    CHOOSE_MAZE_ORDER = 38
    CHOOSE_CELESTIAL_DIE_OR = 39
    CELESTIAL_UPGRADE = 40
    CELESTIAL_MIRROR_CHOICE = 41
    CELESTIAL_GODDESS = 42
    MAZE_MOVE = 43
    CHOOSE_TREASURE_HALL = 44
    MAZE_SPEND = 45
    CHOOSE_MAZE_OR = 46


class BoardState:
    def __init__(self, players, initialState, module):
        self.players = players
        self.module = module  # 0 is no module, 1 is goddess, 2 is titans
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
        self.shields = []
        self.chaos = []
        self.dogged = []
        self.islands = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        self.treasures = ()
        self.cerberus = False
        self.islandChoice = 0  # used to remember choice for ousting
        self.round = 1
        self.activePlayer = 0
        self.blessingPlayer = 0  # player currently resolving a blessing
        self.misfortunePlayer = 0  # player currently using misfortune effect
        self.faceToForge = None  # boar or misfortune face
        self.cyclops = False
        self.sentinel = False
        self.satyrs = False
        self.minotaur = False
        self.eternalFire = False
        self.extraRolls = 0
        self.lastPlayer = 0  # player who last made a move
        self.phase = Phase.TURN_START
        self.returnPhase = Phase.TURN_START  # phase to return to after resolving dice effects
        self.celestialPlayer = 0  # player rolling the celestial die
        self.celestialReturnPhase = Phase.TURN_START  # where to return after rolling celestial die
        self.mazeReturnPhase = Phase.TURN_START  # where to return after resolving maze moves
        if initialState:
            self.setup()
            self.makeMove((Move.PASS, 0, ()))

    def copyState(self):
        copyPlayers = []
        for player in self.players:
            copyPlayers.append(player.copyPlayer())
        ret = BoardState(copyPlayers, False, self.module)
        ret.temple = copy.deepcopy(self.temple)
        ret.shields = copy.deepcopy(self.shields)
        ret.chaos = copy.deepcopy(self.chaos)
        ret.dogged = copy.deepcopy(self.dogged)
        ret.islands = copy.deepcopy(self.islands)
        ret.treasures = copy.deepcopy(self.treasures)
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
        ret.satyrs = self.satyrs
        ret.minotaur = self.minotaur
        ret.eternalFire = self.eternalFire
        ret.extraRolls = self.extraRolls
        ret.lastPlayer = self.lastPlayer
        ret.celestialPlayer = self.celestialPlayer
        ret.celestialReturnPhase = self.celestialReturnPhase
        ret.mazeReturnPhase = self.mazeReturnPhase
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
        if len(self.players) == 3:
            return self.round > 10
        return self.round > 9

    def makeMove(self, move):
        # print(f"Round: {self.round}, Phase: {self.phase}. Making move: {move}. Islands: {self.islands}. Island Choice: {self.islandChoice}")
        # self.printBoardState()
        # self.printPlayersInfo()
        self.lastPlayer = move[1]
        # print(f"last player: {self.lastPlayer}")
        if move[0] == Move.SPEND_GOLD:
            self.players[move[1]].spendGold(move[2][0])
            return
        if move[0] == Move.SPEND_SUN:
            self.players[move[1]].spendSun(move[2][0], move[2][1])
            return
        if move[0] == Move.SPEND_MOON:
            self.players[move[1]].spendMoon(move[2][0], move[2][1])
            return
        if move[0] == Move.USE_TRITON_TOKEN:
            match move[2][0]:
                case "sun":
                    self.players[move[1]].gainSun(2, False)
                case "moon":
                    self.players[move[1]].gainMoon(2, False)
                case "gold":
                    self.players[move[1]].gainGold(6, False)
            self.players[move[1]].tritonTokens -= 1
            return
        if move[0] == Move.USE_COMPANION:
            self.players[move[1]].gainSun(move[2][0], False)
            self.players[move[1]].gainVP(move[2][0])
            self.players[move[1]].companions.remove(move[2][0])
            return
        match self.phase:
            case Phase.TURN_START:
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.ROLL_DIE_1
                self.returnPhase = Phase.USE_TWINS_CHOICE
                if len(self.players) == 2:
                    self.extraRolls = 1
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
                    if not self.eternalFire:
                        self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        if self.satyrs:
                            self.phase = Phase.SATYRS_CHOOSE_DIE_1
                        elif self.minotaur:
                            self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                            self.players[self.blessingPlayer].setBuffers()
                            self.phase = Phase.MIRROR_1_CHOICE
                        else:
                            self.players[self.blessingPlayer].populateTwins()
                            self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.ROLL_DIE_1
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    if not self.eternalFire:
                        self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        if self.satyrs:
                            self.phase = Phase.SATYRS_CHOOSE_DIE_1
                        elif self.minotaur:
                            self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                            self.players[self.blessingPlayer].setBuffers()
                            self.phase = Phase.MIRROR_1_CHOICE
                        else:
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
                        self.players[self.blessingPlayer].gainGold(-3, False)
                        self.players[self.blessingPlayer].twinsToUse -= 1
                        self.phase = Phase.TWINS_REROLL_CHOICE
                    else:
                        self.phase = Phase.USE_CERBERUS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].twinsToUse == 0 or self.players[
                    self.blessingPlayer].getEffectiveGold() < 3:
                    self.phase = Phase.USE_CERBERUS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.TWINS_REROLL_CHOICE:
                if move[0] == Move.TWINS_CHOOSE_DIE:
                    if move[2][0]:
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
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die1.roll()
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
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    if self.players[self.blessingPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.blessingPlayer].gainVP(1)
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.TWINS_RESOURCE_CHOICE
            case Phase.TWINS_RESOURCE_CHOICE:
                if move[0] == Move.TWINS_CHOOSE_RESOURCE:
                    if move[2][0] == "vp":
                        self.players[self.blessingPlayer].gainVP(1)
                    else:
                        self.players[self.blessingPlayer].gainMoon(1, False)
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
                elif self.players[self.blessingPlayer].die1ResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MIRROR_2_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MIRROR_2_CHOICE:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.blessingPlayer].mirrorChoice2 = move[2][0]
                    self.phase = Phase.DIE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].die2ResultBuffer != Data.DieFace.MIRROR:
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
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.blessingPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.CHOOSE_MAZE_ORDER
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.blessingPlayer].gainDiceEffects(self.minotaur, self.sentinel)
                    if self.players[self.blessingPlayer].goldToGain == 0:
                        self.phase = Phase.CHOOSE_MAZE_ORDER
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_MAZE_ORDER:
                if move[0] == Move.CHOOSE_MAZE_ORDER:
                    if move[2][0]:
                        self.celestialReturnPhase = Phase.CHOOSE_MAZE_ORDER
                        self.celestialPlayer = self.blessingPlayer
                        self.phase = Phase.ROLL_CELESTIAL_DIE
                    else:
                        self.phase = Phase.RESOLVE_MAZE_MOVES
                        self.mazeReturnPhase = Phase.CHOOSE_MAZE_ORDER
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    if self.players[self.blessingPlayer].mazeMoves == 0 or self.players[
                        self.blessingPlayer].celestialRolls == 0:
                        if self.players[self.blessingPlayer].celestialRolls == 0:
                            if self.players[self.blessingPlayer].mazeMoves == 0 or self.players[
                                self.blessingPlayer].mazePosition == 35:
                                if self.players[self.blessingPlayer].shipsToResolve == 0 and self.players[
                                    self.blessingPlayer].times3ShipsToResolve == 0:
                                    self.phase = Phase.BOAR_CHOICE_1
                                    self.makeMove((Move.PASS, move[1], ()))
                                else:
                                    self.phase = Phase.RESOLVE_SHIPS
                            else:
                                self.phase = Phase.RESOLVE_MAZE_MOVES
                                self.mazeReturnPhase = Phase.CHOOSE_MAZE_ORDER
                                self.makeMove((Move.PASS, move[1], ()))
                        else:
                            self.celestialReturnPhase = Phase.CHOOSE_MAZE_ORDER
                            self.celestialPlayer = self.blessingPlayer
                            self.phase = Phase.ROLL_CELESTIAL_DIE
            case Phase.RESOLVE_MAZE_MOVES:
                if move[0] == Move.MAZE_MOVE:
                    self.players[self.blessingPlayer].mazePosition = move[2][0]
                    self.players[self.blessingPlayer].mazeMoves -= 1
                    self.phase = Phase.MAZE_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].mazeMoves == 0 or self.players[
                    self.blessingPlayer].mazePosition == 35 or (
                        self.players[self.blessingPlayer].mazePosition == 0 and self.players[
                    self.blessingPlayer].mazeMoves < 0):
                    self.players[self.blessingPlayer].mazeMoves = 0
                    if self.players[self.blessingPlayer].celestialRolls == 0:
                        self.phase = self.mazeReturnPhase
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.celestialReturnPhase = Phase.RESOLVE_MAZE_MOVES
                        self.celestialPlayer = self.blessingPlayer
                        self.phase = Phase.ROLL_CELESTIAL_DIE
                elif len(Data.getMazeMoveOptions(self.players[self.blessingPlayer].mazePosition)) == 1:
                    self.players[self.blessingPlayer].mazePosition = \
                        Data.getMazeMoveOptions(self.players[self.blessingPlayer].mazePosition)[0]
                    self.players[self.blessingPlayer].mazeMoves -= 1
                    self.phase = Phase.MAZE_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_EFFECT:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.blessingPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_MAZE_OR:
                    resources = Data.getMazeOrEffects(self.players[self.blessingPlayer].mazePosition)
                    match move[2][0]:
                        case 0:
                            self.players[self.blessingPlayer].gainGold(resources[0], False)
                        case 1:
                            self.players[self.blessingPlayer].gainSun(resources[1], False)
                        case 2:
                            self.players[self.blessingPlayer].gainMoon(resources[2], False)
                        case 3:
                            self.players[self.blessingPlayer].gainVP(resources[3])
                    if self.players[self.blessingPlayer].goldToGain == 0:
                        self.phase = Phase.RESOLVE_MAZE_MOVES
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    if self.checkBasicMazeEffect(self.players[self.blessingPlayer]):
                        self.phase = Phase.RESOLVE_MAZE_MOVES
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        match Data.getMazeEffect(self.players[self.blessingPlayer].mazePosition):
                            case "FACEBUY" | "FACEBUYDISCOUNT2":
                                self.phase = Phase.MAZE_EFFECT_FACE_BUY
                            case "6GOLDFOR6VP":
                                if self.players[self.blessingPlayer].getEffectiveGold() > 5:
                                    self.phase = Phase.MAZE_EFFECT_SPEND_GOLD
                                else:
                                    self.phase = Phase.RESOLVE_MAZE_MOVES
                                    self.makeMove((Move.PASS, move[1], ()))
                            case "2MOONFOR8VP":
                                if self.players[self.blessingPlayer].getEffectiveMoon() > 1:
                                    self.phase = Phase.MAZE_EFFECT_SPEND_MOON
                                else:
                                    self.phase = Phase.RESOLVE_MAZE_MOVES
                                    self.makeMove((Move.PASS, move[1], ()))
                            case "GODDESS":
                                self.phase = Phase.MAZE_EFFECT_GODDESS
                            case "TREASUREHALL":
                                hasTreasure = False
                                for treasure in self.treasures:
                                    if treasure[1] == self.players[self.blessingPlayer].mazePosition:
                                        hasTreasure = True
                                        self.gainSmallTreasureEffect(treasure[0], self.players[self.blessingPlayer])
                                if hasTreasure:
                                    self.phase = Phase.RESOLVE_MAZE_MOVES
                                    self.makeMove((Move.PASS, move[1], ()))
                                else:
                                    self.phase = Phase.MAZE_EFFECT_TREASUREHALL
            case Phase.MAZE_EFFECT_FACE_BUY:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeFace(move[2])
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.BUY_FACES:
                    if Data.getMazeEffect(self.players[self.blessingPlayer].mazePosition) == "FACEBUY":
                        discount = 0
                    else:
                        discount = 2
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face, discount)
                elif move[0] == Move.PASS:
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_EFFECT_SPEND_GOLD:
                if move[0] == Move.MAZE_SPEND:
                    if move[2][0]:
                        self.players[self.blessingPlayer].gainGold(-6, False)
                        self.players[self.blessingPlayer].gainVP(6)
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_EFFECT_SPEND_MOON:
                if move[0] == Move.MAZE_SPEND:
                    if move[2][0]:
                        self.players[self.blessingPlayer].gainMoon(-2, False)
                        self.players[self.blessingPlayer].gainVP(8)
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_EFFECT_GODDESS:
                if move[0] == Move.CHOOSE_FACES:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    self.players[self.blessingPlayer].die2.setToFace(move[2][1])
                    self.players[self.blessingPlayer].setMazeBuffers()
                    self.phase = Phase.MAZE_MIRROR_1
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_MIRROR_1:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.blessingPlayer].mirrorMazeChoice1 = move[2][0]
                    self.phase = Phase.MAZE_MIRROR_2
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].die1MazeResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MAZE_MIRROR_2
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_MIRROR_2:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.blessingPlayer].mirrorMazeChoice2 = move[2][0]
                    self.phase = Phase.MAZE_DIE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].die2MazeResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.MAZE_DIE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_DIE_1_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.blessingPlayer].orMazeChoice1 = move[2][0]
                    self.phase = Phase.MAZE_DIE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.blessingPlayer].getMazeDie1Result()):
                    self.phase = Phase.MAZE_DIE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_DIE_2_CHOOSE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.blessingPlayer].orMazeChoice2 = move[2][0]
                    self.phase = Phase.MAZE_APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.blessingPlayer].getMazeDie2Result()):
                    self.phase = Phase.MAZE_APPLY_DICE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_APPLY_DICE_EFFECTS:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.blessingPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.MAZE_BOAR_CHOICE_1
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.blessingPlayer].gainMazeDiceEffects()
                    if self.players[self.blessingPlayer].goldToGain == 0:
                        self.phase = Phase.MAZE_BOAR_CHOICE_1
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_BOAR_CHOICE_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.MAZE_BOAR_CHOICE_2
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die1MazeIsBoar():
                    self.phase = Phase.MAZE_BOAR_CHOICE_2
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_BOAR_CHOICE_2:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die2MazeIsBoar():
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MAZE_EFFECT_TREASUREHALL:
                if move[0] == Move.CHOOSE_TREASURE_HALL:
                    for treasure in self.treasures:
                        if treasure[0] == move[2][0]:
                            treasure[1] = self.players[self.blessingPlayer].mazePosition
                            self.gainTreasureEffect(treasure[0], self.players[self.blessingPlayer])
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    if self.players[self.blessingPlayer].times3ShipsToResolve > 0:
                        self.players[self.blessingPlayer].times3ShipsToResolve -= 1
                        for face in move[2]:
                            self.temple[Data.getPool(face)].remove(face)
                            self.players[self.blessingPlayer].buyFaceShip(face, 6)
                    else:
                        self.players[self.blessingPlayer].shipsToResolve -= 1
                        for face in move[2]:
                            self.temple[Data.getPool(face)].remove(face)
                            self.players[self.blessingPlayer].buyFaceShip(face, 2)
                    self.phase = Phase.RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    if self.players[self.blessingPlayer].times3ShipsToResolve > 0:
                        self.players[self.blessingPlayer].times3ShipsToResolve -= 1
                    else:
                        self.players[self.blessingPlayer].shipsToResolve -= 1
                    if self.players[self.blessingPlayer].shipsToResolve == 0 and self.players[
                        self.blessingPlayer].times3ShipsToResolve == 0:
                        self.phase = Phase.BOAR_CHOICE_1
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.blessingPlayer].forgeFace(move[2])
                    if self.players[self.blessingPlayer].shipsToResolve > 0 or self.players[
                        self.blessingPlayer].times3ShipsToResolve > 0:
                        self.phase = Phase.RESOLVE_SHIPS
                    else:
                        self.phase = Phase.BOAR_CHOICE_1
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.BOAR_CHOICE_1:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
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
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
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
                    self.phase = Phase.MISFORTUNE_1_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.isMisfortuneFace(self.players[self.blessingPlayer].die1ResultBuffer):
                    self.phase = Phase.MISFORTUNE_2
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
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.misfortunePlayer].useHammerOrScepter(move[2][0])
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MISFORTUNE_1_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.misfortunePlayer].gainDiceEffects(False, False)
                    if self.players[self.misfortunePlayer].goldToGain == 0:
                        if self.players[self.misfortunePlayer].shipsToResolve == 0:
                            self.phase = Phase.MISFORTUNE_1_BOAR_CHOICE
                            self.makeMove((Move.PASS, move[1], ()))
                        else:
                            self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                            self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face, 2)
                    self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MISFORTUNE_1_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.misfortunePlayer].forgeFace(move[2])
                    if self.players[self.misfortunePlayer].shipsToResolve > 0:
                        self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.MISFORTUNE_1_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_1_BOAR_CHOICE:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.MISFORTUNE_2
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die2IsBoar():
                    self.phase = Phase.MISFORTUNE_2
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice2 = move[2][0]
                    self.phase = Phase.MISFORTUNE_2_CHOOSE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.isMisfortuneFace(self.players[self.blessingPlayer].die2ResultBuffer):
                    self.phase = Phase.CERBERUS_DECISION
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
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.misfortunePlayer].useHammerOrScepter(move[2][0])
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MISFORTUNE_2_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.MISFORTUNE_2_RESOLVE_SHIPS
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.misfortunePlayer].gainDiceEffects(False, False)
                    if self.players[self.misfortunePlayer].goldToGain == 0:
                        if self.players[self.misfortunePlayer].shipsToResolve == 0:
                            self.phase = Phase.MISFORTUNE_2_BOAR_CHOICE
                            self.makeMove((Move.PASS, move[1], ()))
                        else:
                            self.phase = Phase.MISFORTUNE_2_RESOLVE_SHIPS
                            self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face, 2)
                    self.phase = Phase.MISFORTUNE_2_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.misfortunePlayer].shipsToResolve -= 1
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MISFORTUNE_2_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.misfortunePlayer].forgeFace(move[2])
                    if self.players[self.misfortunePlayer].shipsToResolve > 0:
                        self.phase = Phase.MISFORTUNE_1_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.MISFORTUNE_2_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MISFORTUNE_2_BOAR_CHOICE:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].die1IsBoar():
                    self.phase = Phase.CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CERBERUS_DECISION:
                if self.cerberus:
                    self.cerberus = False
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.returnPhase == Phase.USE_TWINS_CHOICE:  # start of turn divine blessings
                    if not self.eternalFire:
                        self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        if self.extraRolls > 0:
                            self.extraRolls -= 1
                            self.phase = Phase.ROLL_DIE_1
                        else:
                            self.players[self.activePlayer].populateReinfEffects()
                            self.phase = Phase.CHOOSE_REINF_EFFECT
                            self.eternalFire = False
                            self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.players[self.blessingPlayer].populateTwins()
                        self.phase = Phase.USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.extraRolls > 0:
                    self.extraRolls -= 1
                    self.phase = Phase.BLESSING_ROLL_DIE_1
                elif self.minotaur:
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.minotaur = False
                        self.phase = self.returnPhase
                        self.makeReturnMove(move[1])
                    else:
                        self.phase = Phase.MIRROR_1_CHOICE
                        self.players[self.blessingPlayer].setBuffers()
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.satyrs:
                    self.satyrs = False
                    self.phase = self.returnPhase
                    self.makeReturnMove(move[1])
                elif self.returnPhase == Phase.LEFT_HAND_ROLL_1_1 or self.returnPhase == Phase.LEFT_HAND_ROLL_1_2:
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    while self.players[self.blessingPlayer].location == 0:
                        self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                        if self.blessingPlayer == self.activePlayer:
                            break
                    if self.blessingPlayer == self.activePlayer:  # everyone ousted
                        if self.returnPhase == Phase.LEFT_HAND_ROLL_1_1:
                            self.phase = Phase.EXTRA_TURN_DECISION
                        else:
                            self.phase = Phase.END_TURN
                        self.makeReturnMove(move[1])
                    else:
                        self.players[self.blessingPlayer].checkBears()
                        self.players[self.blessingPlayer].location = 0
                        self.phase = self.returnPhase
                else:
                    self.phase = self.returnPhase
                    self.makeReturnMove(move[1])
            case Phase.SATYRS_CHOOSE_DIE_1:
                if move[0] == Move.SATYRS_CHOOSE_DIE:
                    self.players[self.activePlayer].orChoice1 = move[2][0]
                    self.phase = Phase.SATYRS_CHOOSE_DIE_2
            case Phase.SATYRS_CHOOSE_DIE_2:
                if move[0] == Move.SATYRS_CHOOSE_DIE:
                    self.players[self.activePlayer].orChoice2 = move[2][0]
                    if self.players[self.activePlayer].orChoice1 % 2 == 0:
                        self.players[self.activePlayer].die1ResultBuffer = self.players[
                            self.players[self.activePlayer].orChoice1 // 2].getDie1UpFace()
                    else:
                        self.players[self.activePlayer].die1ResultBuffer = self.players[
                            self.players[self.activePlayer].orChoice1 // 2].getDie2UpFace()
                    if self.players[self.activePlayer].orChoice2 % 2 == 0:
                        self.players[self.activePlayer].die2ResultBuffer = self.players[
                            self.players[self.activePlayer].orChoice2 // 2].getDie1UpFace()
                    else:
                        self.players[self.activePlayer].die2ResultBuffer = self.players[
                            self.players[self.activePlayer].orChoice2 // 2].getDie2UpFace()
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
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
                        self.players[self.blessingPlayer].gainGold(-3, False)
                        self.players[self.blessingPlayer].twinsToUse -= 1
                        self.phase = Phase.MINOR_TWINS_REROLL
                    else:
                        self.phase = Phase.MINOR_USE_CERBERUS
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].twinsToUse == 0 or self.players[
                    self.blessingPlayer].getEffectiveGold() < 3:
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
                elif move[0] == Move.RANDOM_ROLL:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.players[self.blessingPlayer].die1.roll()
                    else:
                        self.players[self.blessingPlayer].die2.roll()
                    if self.players[self.blessingPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.blessingPlayer].gainVP(1)
                        self.phase = Phase.MINOR_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.MINOR_TWINS_RESOURCE
            case Phase.MINOR_TWINS_RESOURCE:
                if move[0] == Move.TWINS_CHOOSE_RESOURCE:
                    if move[2][0] == "vp":
                        self.players[self.blessingPlayer].gainVP(1)
                    else:
                        self.players[self.blessingPlayer].gainMoon(1, False)
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
                        if self.cyclops:
                            self.phase = Phase.CHOOSE_CYCLOPS
                        else:
                            self.phase = Phase.MINOR_RESOLVE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                    elif not Data.getIsOr(self.players[self.blessingPlayer].getDie1Result()):
                        if self.cyclops:
                            self.phase = Phase.CHOOSE_CYCLOPS
                        else:
                            self.phase = Phase.MINOR_RESOLVE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    if move[0] == Move.CHOOSE_DIE_OR:
                        self.players[self.blessingPlayer].orChoice2 = move[2][0]
                        if self.cyclops:
                            self.phase = Phase.CHOOSE_CYCLOPS
                        else:
                            self.phase = Phase.MINOR_RESOLVE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
                    elif not Data.getIsOr(self.players[self.blessingPlayer].getDie2Result()):
                        if self.cyclops:
                            self.phase = Phase.CHOOSE_CYCLOPS
                        else:
                            self.phase = Phase.MINOR_RESOLVE_EFFECTS
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_CYCLOPS:
                if move[0] == Move.CHOOSE_USE_CYCLOPS:
                    self.players[self.blessingPlayer].sentinel1Choice = move[2][0]  # reuse sentinel1Choice
                    self.phase = Phase.MINOR_RESOLVE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.blessingPlayer].canUseCyclops():
                    self.phase = Phase.MINOR_RESOLVE_EFFECTS
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_RESOLVE_EFFECTS:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.blessingPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.MINOR_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.blessingPlayer].gainMinorBlessingEffect(self.cyclops)
                    if self.players[self.blessingPlayer].goldToGain == 0:
                        self.phase = Phase.MINOR_MAZE_MOVES
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MAZE_MOVES:
                if self.players[self.blessingPlayer].mazeMoves > 0 and self.players[
                    self.blessingPlayer].mazePosition != 35:
                    self.phase = Phase.RESOLVE_MAZE_MOVES
                    self.mazeReturnPhase = Phase.MINOR_MAZE_MOVES
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.blessingPlayer].shipsToResolve == 0:
                    self.phase = Phase.MINOR_BOAR_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.phase = Phase.MINOR_RESOLVE_SHIPS
            case Phase.MINOR_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.blessingPlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.blessingPlayer].buyFaceShip(face, 2)
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
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
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
                if (self.players[self.blessingPlayer].dieChoice and not Data.isMisfortuneFace(
                        self.players[self.blessingPlayer].die1ResultBuffer)) or (
                        not self.players[self.blessingPlayer].dieChoice and not Data.isMisfortuneFace(self.players[
                                                                                                          self.blessingPlayer].die2ResultBuffer)):
                    self.phase = Phase.MINOR_CERBERUS_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    if self.players[self.blessingPlayer].dieChoice:
                        self.misfortunePlayer = self.decideMisfortunePlayer(
                            self.players[self.blessingPlayer].getDie1Result())
                    else:
                        self.misfortunePlayer = self.decideMisfortunePlayer(
                            self.players[self.blessingPlayer].getDie2Result())
                    self.phase = Phase.MINOR_MISFORTUNE_1_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.MINOR_MISFORTUNE_1_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.misfortunePlayer].orChoice1 = move[2][0]
                    self.phase = Phase.MINOR_MISFORTUNE_2_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.misfortunePlayer].getDie1Result()):
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
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.misfortunePlayer].useHammerOrScepter(move[2][0])
                    if self.players[self.misfortunePlayer].shipsToResolve == 0:
                        self.phase = Phase.MINOR_CERBERUS_DECISION
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.MINOR_MISFORTUNE_SHIPS
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.misfortunePlayer].gainDiceEffects(False, False)
                    if self.players[self.misfortunePlayer].goldToGain == 0:
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
                        self.players[self.blessingPlayer].buyFaceShip(face, 2)
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
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_ELDER_REINF:
                if move[0] == Move.USE_ELDER:
                    if move[2][0]:
                        self.players[self.activePlayer].gainGold(-3, False)
                        self.players[self.activePlayer].gainVP(4)
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove(move)
            case Phase.RESOLVE_OWL_REINF:
                if move[0] == Move.OWL_CHOICE:
                    match move[2][0]:
                        case "gold":
                            self.players[self.activePlayer].gainGold(1, False)
                        case "sun":
                            self.players[self.activePlayer].gainSun(1, False)
                        case "moon":
                            self.players[self.activePlayer].gainMoon(1, False)
                    if self.players[self.activePlayer].goldToGain == 0:
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_HIND_REINF:
                self.phase = Phase.MINOR_CHOOSE_DIE
                self.blessingPlayer = self.activePlayer
                self.returnPhase = Phase.CHOOSE_REINF_EFFECT
            case Phase.RESOLVE_TREE_REINF:
                if move[0] == Move.PASS:
                    if self.players[self.activePlayer].gold < 8:  # note: this only checks hero inventory reserve
                        self.players[self.activePlayer].gainGold(3, False)
                        self.players[self.activePlayer].gainVP(1)
                    else:
                        self.players[self.activePlayer].gainVP(2)
                    if self.players[self.activePlayer].goldToGain == 0:
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_MERCHANT_REINF:
                if move[0] == Move.MERCHANT_UPGRADE:
                    self.players[self.activePlayer].gainVP(move[2][0])
                    if len(move[2]) > 1:
                        self.temple[Data.getPool(move[2][3])].remove(move[2][3])
                        self.players[self.activePlayer].upgradeFace(move[2][1], move[2][2], move[2][3])
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_LIGHT_REINF:
                if move[0] == Move.USE_LIGHT:
                    if move[2][0]:
                        self.players[self.activePlayer].gainGold(-3, False)
                        self.players[self.activePlayer].die1ResultBuffer = move[2][1]
                        self.players[self.activePlayer].dieChoice = True
                        self.blessingPlayer = self.activePlayer
                        self.phase = Phase.MINOR_CHOOSE_OR
                        self.returnPhase = Phase.CHOOSE_REINF_EFFECT
                    else:
                        self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_COMPANION_REINF:
                self.players[self.activePlayer].advanceCompanions()
                self.phase = Phase.CHOOSE_REINF_EFFECT
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.RESOLVE_GUARDIAN_REINF:
                if move[0] == Move.GUARDIAN_CHOICE:
                    match move[2][0]:
                        case "ancientshard":
                            self.players[self.activePlayer].gainAncientShards(1)
                        case "loyalty":
                            self.players[self.activePlayer].gainLoyalty(1)
                    self.phase = Phase.CHOOSE_REINF_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
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
                        self.players[self.activePlayer].gainSun(-2, False)
                        self.phase = Phase.ACTIVE_PLAYER_CHOICE_2
                    else:
                        self.phase = Phase.TURN_START
                        self.advanceActivePlayer(move[1])
                elif self.players[self.activePlayer].getEffectiveSun() < 2:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
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
                        self.advanceActivePlayer(move[1])
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
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
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.EXTRA_TURN_DECISION
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
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.CHOOSE_SHIELD_FACE_1 | Phase.CHOOSE_CHAOS_FACE_1 | Phase.CHOOSE_DOGGED_FACE_1:
                if move[0] == Move.BUY_FACES:
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CHOOSE_SHIELD_FACE_2 | Phase.CHOOSE_CHAOS_FACE_2 | Phase.CHOOSE_DOGGED_FACE_2:
                if move[0] == Move.BUY_FACES:
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.FORGE_FEAT_FACE_1:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.FORGE_FEAT_FACE_2:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
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
                    self.advanceActivePlayer(move[1])
            case Phase.NYMPH_1:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                elif move[0] == Move.BUY_FACES:
                    self.temple[Data.getPool(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].buyFace(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.NYMPH_2:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                elif move[0] == Move.BUY_FACES:
                    self.temple[Data.getPool(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].buyFace(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.TRIDENT_1:
                if move[0] == Move.BUY_FACES:
                    if move[2][0] == Data.DieFace.REDSHIELD or move[2][0] == Data.DieFace.REDSHIELD or move[2][
                        0] == Data.DieFace.REDSHIELD or move[2][0] == Data.DieFace.REDSHIELD:
                        self.shields.remove(move[2][0])
                    elif Data.getPool(move[2][0]) != -1:
                        self.temple[Data.getPool(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.TRIDENT_2:
                if move[0] == Move.BUY_FACES:
                    if move[2][0] == Data.DieFace.REDSHIELD or move[2][0] == Data.DieFace.REDSHIELD or move[2][
                        0] == Data.DieFace.REDSHIELD or move[2][0] == Data.DieFace.REDSHIELD:
                        self.shields.remove(move[2][0])
                    elif Data.getPool(move[2][0]) != -1:
                        self.temple[Data.getPool(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.GODDESS_CHOOSE_FACES:
                if move[0] == Move.CHOOSE_FACES:
                    self.players[self.activePlayer].die1.setToFace(move[2][0])
                    self.players[self.activePlayer].die2.setToFace(move[2][1])
                    self.players[self.activePlayer].setBuffers()
                    self.blessingPlayer = self.activePlayer
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RIGHTHAND_1:
                if move[0] == Move.RIGHTHAND_SPEND:
                    self.players[self.activePlayer].gainGold(-move[2][0], False)
                    self.players[self.activePlayer].gainVP(move[2][0])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.RIGHTHAND_2:
                if move[0] == Move.RIGHTHAND_SPEND:
                    self.players[self.activePlayer].gainGold(-move[2][0], False)
                    self.players[self.activePlayer].gainVP(move[2][0])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.WIND_ROLL_DIE_1:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    self.phase = Phase.WIND_ROLL_DIE_2
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die1.roll()
                    self.phase = Phase.WIND_ROLL_DIE_2
            case Phase.WIND_ROLL_DIE_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.phase = Phase.WIND_CHOOSE_RESOURCE
                    else:
                        self.phase = Phase.WIND_ROLL_DIE_1
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    self.blessingPlayer = (self.blessingPlayer + 1) % len(self.players)
                    if self.blessingPlayer == self.activePlayer:
                        self.phase = Phase.WIND_CHOOSE_RESOURCE
                    else:
                        self.phase = Phase.WIND_ROLL_DIE_1
            case Phase.WIND_CHOOSE_RESOURCE:
                if move[0] == Move.CHOOSE_RESOURCE:
                    for player in self.players:
                        self.players[self.activePlayer].gainWindResources(player.getDie1UpFace(), move[2][0])
                        self.players[self.activePlayer].gainWindResources(player.getDie2UpFace(), move[2][0])
                    self.phase = self.returnPhase
                    self.makeReturnMove(self.activePlayer)
            case Phase.USE_ANCESTOR:
                if move[0] == Move.BUY_FACES:
                    self.temple[Data.getPool(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].unforgedFaces.append(move[2][0])
                elif move[0] == Move.FORGE_FACE:
                    self.players[self.activePlayer].forgeFace(move[2])
                    self.players[self.activePlayer].dieChoice = move[2][0]
                    self.phase = Phase.MINOR_ROLL_DIE
                elif move[0] == Move.PASS:
                    self.phase = Phase.MINOR_CHOOSE_DIE
            case Phase.TITAN_1:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFreeFeat(move[2][0])
                    effect = Data.getEffect(move[2][0])
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.EXTRA_TURN_DECISION
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.TITAN_2:
                if move[0] == Move.PERFORM_FEAT:
                    self.islands[Data.getPosition(move[2][0])].remove(move[2][0])
                    self.players[self.activePlayer].performFreeFeat(move[2][0])
                    effect = Data.getEffect(move[2][0])
                    if "INST" in effect:
                        self.resolveInstEffect(effect)
                    else:
                        self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.activePlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
                elif move[0] == Move.PASS:
                    self.phase = Phase.TURN_START
                    self.advanceActivePlayer(move[1])
            case Phase.LEFT_HAND_ROLL_1_1 | Phase.LEFT_HAND_ROLL_1_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die1.setToFace(move[2][0])
                    self.returnPhase = self.phase
                    self.phase = Phase.LEFT_HAND_ROLL_2
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die1.roll()
                    self.returnPhase = self.phase
                    self.phase = Phase.LEFT_HAND_ROLL_2
            case Phase.LEFT_HAND_ROLL_2:
                if move[0] == Move.ROLL:
                    self.players[self.blessingPlayer].die2.setToFace(move[2][0])
                    self.players[self.activePlayer].die1ResultBuffer = self.players[self.blessingPlayer].getDie1UpFace()
                    self.players[self.activePlayer].die2ResultBuffer = self.players[self.blessingPlayer].getDie2UpFace()
                    self.blessingPlayer = self.activePlayer
                    self.phase = Phase.MIRROR_1_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.RANDOM_ROLL:
                    self.players[self.blessingPlayer].die2.roll()
                    self.players[self.activePlayer].die1ResultBuffer = self.players[self.blessingPlayer].getDie1UpFace()
                    self.players[self.activePlayer].die2ResultBuffer = self.players[self.blessingPlayer].getDie2UpFace()
                    self.blessingPlayer = self.activePlayer
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.ROLL_CELESTIAL_DIE:
                if move[0] == Move.ROLL or move[0] == Move.RANDOM_ROLL:
                    self.players[self.celestialPlayer].celestialRolls -= 1
                    if move[0] == Move.RANDOM_ROLL:
                        self.players[self.celestialPlayer].celestialResultBuffer = self.celestialDieRandomRoll()
                    else:
                        self.players[self.celestialPlayer].celestialResultBuffer = move[2][0]
                    self.players[self.celestialPlayer].populateTwins()
                    self.phase = Phase.CELESTIAL_USE_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS and self.players[self.celestialPlayer].celestialRolls == 0:
                    if self.players[self.celestialPlayer].mazeMoves == 0:
                        self.phase = self.celestialReturnPhase
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.RESOLVE_MAZE_MOVES
                        if self.celestialReturnPhase != Phase.RESOLVE_MAZE_MOVES:
                            self.mazeReturnPhase = self.celestialReturnPhase
                        self.blessingPlayer = self.celestialPlayer
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_USE_TWINS_CHOICE:  # call populateTwins() before entering this state for the first time
                if move[0] == Move.USE_TWINS:
                    if move[2][0]:
                        self.players[self.celestialPlayer].gainGold(-3, False)
                        self.players[self.celestialPlayer].twinsToUse -= 1
                        self.phase = Phase.CELESTIAL_TWINS_REROLL
                    else:
                        self.phase = Phase.CELESTIAL_RESOLVE_EFFECT
                        self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.celestialPlayer].twinsToUse == 0 or self.players[
                    self.celestialPlayer].getEffectiveGold() < 3:
                    self.phase = Phase.CELESTIAL_RESOLVE_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_TWINS_REROLL:
                if move[0] == Move.ROLL or move[0] == Move.RANDOM_ROLL:
                    if move[0] == Move.RANDOM_ROLL:
                        self.players[self.celestialPlayer].celestialResultBuffer = self.celestialDieRandomRoll()
                    else:
                        self.players[self.celestialPlayer].celestialResultBuffer = move[2][0]
                    if self.players[self.celestialPlayer].hasMaxMoon():  # max moon so gain vp
                        self.players[self.celestialPlayer].gainVP(1)
                        self.phase = Phase.CELESTIAL_USE_TWINS_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                    else:
                        self.phase = Phase.CELESTIAL_TWINS_RESOURCE_CHOICE
            case Phase.CELESTIAL_TWINS_RESOURCE_CHOICE:
                if move[0] == Move.TWINS_CHOOSE_RESOURCE:
                    if move[2][0] == "vp":
                        self.players[self.celestialPlayer].gainVP(1)
                    else:
                        self.players[self.celestialPlayer].gainMoon(1, False)
                    self.phase = Phase.CELESTIAL_USE_TWINS_CHOICE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_EFFECT:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.celestialPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.ROLL_CELESTIAL_DIE
                    self.makeMove((Move.PASS, move[1], ()))
                else:
                    match self.players[self.celestialPlayer].celestialResultBuffer:
                        case Data.DieFace.CELESTIAL12GOLD:
                            self.players[self.celestialPlayer].gainGold(12, False)
                        case Data.DieFace.CELESTIAL5VP:
                            self.players[self.celestialPlayer].gainVP(5)
                        case Data.DieFace.CELESTIAL3VPAND3GOLD1SUN1MOONOR:
                            self.players[self.celestialPlayer].gainVP(3)
                            self.phase = Phase.CELESTIAL_CHOOSE_OR
                        case Data.DieFace.CELESTIALMIRROR:
                            self.phase = Phase.CELESTIAL_CHOOSE_MIRROR
                        case Data.DieFace.CELESTIALGODDESS:
                            self.phase = Phase.CELESTIAL_CHOOSE_GODDESS
                        case Data.DieFace.CELESTIALUPGRADE:
                            self.phase = Phase.CELESTIAL_CHOOSE_UPGRADE
                    if self.phase == Phase.CELESTIAL_RESOLVE_EFFECT and self.players[
                        self.celestialPlayer].goldToGain == 0:
                        self.phase = Phase.ROLL_CELESTIAL_DIE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_CHOOSE_OR:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.celestialPlayer].useHammerOrScepter(move[2][0])
                    self.phase = Phase.ROLL_CELESTIAL_DIE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.CHOOSE_CELESTIAL_DIE_OR:
                    if move[2][0] == 0:
                        self.players[self.celestialPlayer].gainGold(3, False)
                    elif move[2][0] == 1:
                        self.players[self.celestialPlayer].gainSun(1, False)
                    elif move[2][0] == 2:
                        self.players[self.celestialPlayer].gainMoon(1, False)
                    if self.players[self.celestialPlayer].goldToGain == 0:
                        self.phase = Phase.ROLL_CELESTIAL_DIE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_CHOOSE_UPGRADE:
                if move[0] == Move.CELESTIAL_UPGRADE:
                    self.temple[Data.getPool(move[2][2])].remove(move[2][2])
                    self.players[self.celestialPlayer].upgradeFace(move[2][0], move[2][1], move[2][2])
                    self.phase = Phase.ROLL_CELESTIAL_DIE
                    self.makeMove((Move.PASS, move[1], ()))
                elif move[0] == Move.PASS:
                    self.phase = Phase.ROLL_CELESTIAL_DIE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_CHOOSE_MIRROR:
                if move[0] == Move.CELESTIAL_MIRROR_CHOICE:
                    self.players[self.celestialPlayer].celestialResultBuffer = move[2][0]
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_CHOOSE_GODDESS:
                if move[0] == Move.CELESTIAL_GODDESS:
                    if move[2][0]:
                        self.players[self.celestialPlayer].die1.setToFace(move[2][1])
                    else:
                        self.players[self.celestialPlayer].die2.setToFace(move[2][1])
                    self.players[self.celestialPlayer].celestialResultBuffer = move[2][1]
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_MIRROR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_DIE_MIRROR:
                if move[0] == Move.MIRROR_CHOICE:
                    self.players[self.celestialPlayer].celestialResultBuffer = move[2][0]
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_OR
                    self.makeMove((Move.PASS, move[1], ()))
                elif self.players[self.celestialPlayer].celestialResultBuffer != Data.DieFace.MIRROR:
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_OR
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_DIE_OR:
                if move[0] == Move.CHOOSE_DIE_OR:
                    self.players[self.celestialPlayer].celestialOrChoice = move[2][0]
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
                elif not Data.getIsOr(self.players[self.celestialPlayer].celestialResultBuffer):
                    self.phase = Phase.CELESTIAL_RESOLVE_DIE_EFFECT
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_DIE_EFFECT:
                if move[0] == Move.CHOOSE_ADD_HAMMER_SCEPTER:
                    self.players[self.celestialPlayer].useHammerOrScepter(move[2][0])
                    if self.players[self.celestialPlayer].shipsToResolve > 0:
                        self.phase = Phase.CELESTIAL_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.CELESTIAL_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
                else:
                    self.players[self.celestialPlayer].gainCelestialDieEffects()
                    if self.players[self.celestialPlayer].goldToGain == 0:
                        if self.players[self.celestialPlayer].shipsToResolve > 0:
                            self.phase = Phase.CELESTIAL_RESOLVE_SHIPS
                        else:
                            self.phase = Phase.CELESTIAL_BOAR_CHOICE
                            self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_SHIPS:
                if move[0] == Move.BUY_FACES:
                    self.players[self.celestialPlayer].shipsToResolve -= 1
                    for face in move[2]:
                        self.temple[Data.getPool(face)].remove(face)
                        self.players[self.celestialPlayer].buyFaceShip(face, 2)
                    self.phase = Phase.CELESTIAL_RESOLVE_SHIPS_FORGE
                elif move[0] == Move.PASS:
                    self.players[self.celestialPlayer].shipsToResolve -= 1
                    if self.players[self.celestialPlayer].shipsToResolve == 0:
                        self.phase = Phase.CELESTIAL_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_RESOLVE_SHIPS_FORGE:
                if move[0] == Move.FORGE_FACE:
                    self.players[self.celestialPlayer].forgeFace(move[2])
                    if self.players[self.celestialPlayer].shipsToResolve > 0:
                        self.phase = Phase.CELESTIAL_RESOLVE_SHIPS
                    else:
                        self.phase = Phase.CELESTIAL_BOAR_CHOICE
                        self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_BOAR_CHOICE:
                if move[0] == Move.BOAR_CHOICE:
                    match move[2][0]:
                        case "sun":
                            self.players[move[1]].gainSun(1, False)
                        case "moon":
                            self.players[move[1]].gainMoon(1, False)
                        case "vp":
                            self.players[move[1]].gainVP(3)
                    self.phase = Phase.CELESTIAL_MISFORTUNE
                    self.makeMove((Move.PASS, move[1], ()))
                elif not self.players[self.celestialPlayer].celestialIsBoar():
                    self.phase = Phase.CELESTIAL_MISFORTUNE
                    self.makeMove((Move.PASS, move[1], ()))
            case Phase.CELESTIAL_MISFORTUNE:
                # todo
                self.phase = Phase.ROLL_CELESTIAL_DIE
                self.makeMove((Move.PASS, move[1], ()))
            case Phase.END_TURN:
                self.phase = Phase.TURN_START
                self.advanceActivePlayer(move[1])

    def getOptions(self):
        # print(self.phase)
        # self.printBoardState()
        for player in self.players:
            if player.goldToSpend > 0:
                return self.getSpendGoldOptions(player)
            if player.sunToSpend > 0:
                return self.getSpendSunOptions(player)
            if player.moonToSpend > 0:
                return self.getSpendMoonOptions(player)
        ret = ((Move.PASS, self.activePlayer, ()),)
        match self.phase:
            case Phase.ROLL_DIE_1 | Phase.BLESSING_ROLL_DIE_1 | Phase.TWINS_REROLL_1 | Phase.WIND_ROLL_DIE_1 | Phase.LEFT_HAND_ROLL_1_1 | Phase.LEFT_HAND_ROLL_1_2:
                ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die1)
            case Phase.ROLL_DIE_2 | Phase.BLESSING_ROLL_DIE_2 | Phase.TWINS_REROLL_2 | Phase.WIND_ROLL_DIE_2 | Phase.LEFT_HAND_ROLL_2:
                ret = self.generateRollDieOptions(self.blessingPlayer, self.players[self.blessingPlayer].die2)
            case Phase.USE_TWINS_CHOICE | Phase.MINOR_TWINS_CHOICE | Phase.CELESTIAL_USE_TWINS_CHOICE:
                ret = ((Move.USE_TWINS, self.blessingPlayer, (True,)), (Move.USE_TWINS, self.blessingPlayer, (False,)))
            case Phase.TWINS_REROLL_CHOICE:
                ret = (
                    (Move.TWINS_CHOOSE_DIE, self.blessingPlayer, (True,)),
                    (Move.TWINS_CHOOSE_DIE, self.blessingPlayer, (False,)))
            case Phase.TWINS_RESOURCE_CHOICE | Phase.MINOR_TWINS_RESOURCE | Phase.CELESTIAL_TWINS_RESOURCE_CHOICE:
                ret = ((Move.TWINS_CHOOSE_RESOURCE, self.blessingPlayer, ("vp",)),
                       (Move.TWINS_CHOOSE_RESOURCE, self.blessingPlayer, ("moon",)))
            case Phase.USE_CERBERUS_CHOICE | Phase.MINOR_USE_CERBERUS:
                ret = (
                    (Move.USE_CERBERUS, self.blessingPlayer, (True,)),
                    (Move.USE_CERBERUS, self.blessingPlayer, (False,)))
            case Phase.MIRROR_1_CHOICE:
                if self.satyrs:
                    ret = self.getMirrorChoices(self.players[self.activePlayer].orChoice1 // 2)
                else:
                    ret = self.getMirrorChoices(self.blessingPlayer)
            case Phase.MIRROR_2_CHOICE:
                if self.satyrs:
                    ret = self.getMirrorChoices(self.players[self.activePlayer].orChoice2 // 2)
                else:
                    ret = self.getMirrorChoices(self.blessingPlayer)
            case Phase.MAZE_MIRROR_1 | Phase.MAZE_MIRROR_2:
                ret = self.getMirrorChoices(self.blessingPlayer)
            case Phase.MINOR_MIRROR_CHOICE:
                ret = self.getMirrorChoices(self.blessingPlayer)
            case Phase.CHOOSE_MAZE_ORDER:
                ret = (Move.CHOOSE_MAZE_ORDER, self.blessingPlayer, (True,)), (
                    Move.CHOOSE_MAZE_ORDER, self.blessingPlayer, (False,))
            case Phase.RESOLVE_MAZE_MOVES:
                ret = self.getMazeMoveChoices(self.players[self.blessingPlayer])
            case Phase.MAZE_EFFECT_SPEND_GOLD | Phase.MAZE_EFFECT_SPEND_MOON:
                ret = (
                    (Move.MAZE_SPEND, self.blessingPlayer, (True,)), (Move.MAZE_SPEND, self.blessingPlayer, (False,)))
            case Phase.MAZE_EFFECT:
                if self.players[self.blessingPlayer].goldToGain > 0:
                    ret = self.getHammerScepterChoices(self.blessingPlayer)
                else:
                    ret = self.getMazeEffectOrChoices(self.players[self.blessingPlayer])
            case Phase.MAZE_EFFECT_FACE_BUY:
                if self.players[self.blessingPlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.blessingPlayer)
                elif Data.getMazeEffect(self.players[self.blessingPlayer].mazePosition) == "FACEBUY":
                    ret = self.generateBuyFace(self.blessingPlayer, 0)
                else:
                    ret = self.generateBuyFace(self.blessingPlayer, 2)
            case Phase.MAZE_EFFECT_GODDESS:
                ret = self.generateGoddessChoice(self.players[self.blessingPlayer])
            case Phase.MAZE_EFFECT_TREASUREHALL:
                ret = []
                for treasure in self.treasures:
                    if treasure[1] == -1:
                        ret.append((Move.CHOOSE_TREASURE_HALL, self.blessingPlayer, (treasure[0],)))
                ret = tuple(ret)
            case Phase.ROLL_CELESTIAL_DIE | Phase.CELESTIAL_TWINS_REROLL:
                ret = self.generateCelestialDieDecision(self.celestialPlayer)
            case Phase.CELESTIAL_RESOLVE_EFFECT | Phase.CELESTIAL_RESOLVE_DIE_EFFECT:
                ret = self.getHammerScepterChoices(self.celestialPlayer)
            case Phase.CELESTIAL_CHOOSE_OR:
                if self.players[self.celestialPlayer].goldToGain > 0:
                    ret = self.getHammerScepterChoices(self.celestialPlayer)
                else:
                    ret = (Move.CHOOSE_CELESTIAL_DIE_OR, self.celestialPlayer, (0,)), (
                        Move.CHOOSE_CELESTIAL_DIE_OR, self.celestialPlayer, (1,)), (
                        Move.CHOOSE_CELESTIAL_DIE_OR, self.celestialPlayer, (2,))
            case Phase.CELESTIAL_CHOOSE_UPGRADE:
                ret = self.getCelestialUpgradeChoices(self.players[self.celestialPlayer])
            case Phase.CELESTIAL_CHOOSE_MIRROR:
                ret = self.getCelestialMirrorChoices(self.celestialPlayer)
            case Phase.CELESTIAL_CHOOSE_GODDESS:
                ret = self.getCelestialGoddessChoices(self.players[self.celestialPlayer])
            case Phase.CELESTIAL_RESOLVE_DIE_MIRROR:
                ret = self.getMirrorChoices(self.celestialPlayer)
            case Phase.CELESTIAL_RESOLVE_DIE_OR:
                ret = self.players[self.celestialPlayer].getCelestialDieOptions()
            case Phase.CELESTIAL_RESOLVE_SHIPS:
                ret = self.generateBuyFace(self.celestialPlayer, 2)
            case Phase.CELESTIAL_RESOLVE_SHIPS_FORGE:
                ret = self.generateForgeFace(self.celestialPlayer)
            case Phase.CELESTIAL_BOAR_CHOICE:
                ret = self.generateBoarChoice(self.players[self.celestialPlayer].celestialResultBuffer)
            case Phase.DIE_1_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getDieOptions(True)
            case Phase.DIE_2_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getDieOptions(False)
            case Phase.MAZE_DIE_1_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getMazeDieOptions(True)
            case Phase.MAZE_DIE_2_CHOOSE_OR:
                ret = self.players[self.blessingPlayer].getMazeDieOptions(False)
            case Phase.APPLY_DICE_EFFECTS | Phase.MAZE_APPLY_DICE_EFFECTS:
                ret = self.getHammerScepterChoices(self.blessingPlayer)
            case Phase.BOAR_CHOICE_1 | Phase.MISFORTUNE_2_BOAR_CHOICE:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie1Result())
            case Phase.BOAR_CHOICE_2 | Phase.MISFORTUNE_1_BOAR_CHOICE:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie2Result())
            case Phase.MAZE_BOAR_CHOICE_1:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getMazeDie1Result())
            case Phase.MAZE_BOAR_CHOICE_2:
                ret = self.generateBoarChoice(self.players[self.blessingPlayer].getMazeDie2Result())
            case Phase.MISFORTUNE_1:
                ret = self.generateMisfortune1Choice()
            case Phase.MISFORTUNE_1_CHOOSE_OR | Phase.MINOR_MISFORTUNE_1_OR:
                ret = self.players[self.misfortunePlayer].getDieOptions(False)
            case Phase.MISFORTUNE_2:
                ret = self.generateMisfortune2Choice()
            case Phase.MISFORTUNE_2_CHOOSE_OR | Phase.MINOR_MISFORTUNE_2_OR:
                ret = self.players[self.misfortunePlayer].getDieOptions(True)
            case Phase.MISFORTUNE_2_APPLY_EFFECTS | Phase.MISFORTUNE_2_APPLY_EFFECTS:
                ret = self.getHammerScepterChoices(self.misfortunePlayer)
            case Phase.DIE_1_CHOOSE_SENTINEL | Phase.DIE_2_CHOOSE_SENTINEL:
                ret = (Move.CHOOSE_USE_SENTINEL, self.blessingPlayer, (True,)), (
                    Move.CHOOSE_USE_SENTINEL, self.blessingPlayer, (False,))
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
            case Phase.CHOOSE_CYCLOPS:
                ret = (Move.CHOOSE_USE_CYCLOPS, self.blessingPlayer, (True,)), (
                    Move.CHOOSE_USE_CYCLOPS, self.blessingPlayer, (False,))
            case Phase.MINOR_RESOLVE_EFFECTS:
                ret = self.getHammerScepterChoices(self.blessingPlayer)
            case Phase.MINOR_BOAR_CHOICE:
                if self.players[self.blessingPlayer].dieChoice:
                    ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie1Result())
                else:
                    ret = self.generateBoarChoice(self.players[self.blessingPlayer].getDie2Result())
            case Phase.MINOR_MISFORTUNE_RESOLVE:
                ret = self.getHammerScepterChoices(self.misfortunePlayer)
            case Phase.CHOOSE_REINF_EFFECT:
                ret = self.players[self.activePlayer].getReinfOptions()
            case Phase.RESOLVE_ELDER_REINF:
                if self.players[self.activePlayer].getEffectiveGold() >= 3:
                    ret = (Move.USE_ELDER, self.activePlayer, (True,)), (Move.USE_ELDER, self.activePlayer, (False,))
                else:
                    ret = (Move.USE_ELDER, self.activePlayer, (False,)),
            case Phase.RESOLVE_OWL_REINF:
                if self.players[self.activePlayer].goldToGain == 0:
                    ret = (
                        (Move.OWL_CHOICE, self.activePlayer, ("gold",)), (Move.OWL_CHOICE, self.activePlayer, ("sun",)),
                        (Move.OWL_CHOICE, self.activePlayer, ("moon",)))
                else:
                    ret = self.getHammerScepterChoices(self.activePlayer)
            case Phase.RESOLVE_TREE_REINF:
                ret = self.getHammerScepterChoices(self.activePlayer)
            case Phase.RESOLVE_MERCHANT_REINF:
                ret = self.generateMerchantChoices(self.players[self.activePlayer])
            case Phase.RESOLVE_LIGHT_REINF:
                if self.players[self.activePlayer].getEffectiveGold() >= 3:
                    ret = self.generateLightChoices()
                else:
                    ret = (Move.USE_LIGHT, self.activePlayer, (False,)),
            case Phase.RESOLVE_GUARDIAN_REINF:
                ret = ((Move.GUARDIAN_CHOICE, self.activePlayer, ("ancientshard",)),
                       (Move.GUARDIAN_CHOICE, self.activePlayer, ("loyalty",)))
            case Phase.ACTIVE_PLAYER_CHOICE_1 | Phase.ACTIVE_PLAYER_CHOICE_2:
                ret = (Move.CHOOSE_BUY_FACES, self.activePlayer, ()), (Move.CHOOSE_PERFORM_FEAT, self.activePlayer, ())
            case Phase.ACTIVE_PLAYER_BUY_FACES_1 | Phase.ACTIVE_PLAYER_BUY_FACES_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateBuyFaces(self.players[self.activePlayer].getEffectiveGold())
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 | Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                if self.players[self.activePlayer].goldToGain == 0:
                    ret = self.generatePerformFeats()
                else:
                    ret = self.getHammerScepterChoices(self.activePlayer)
            case Phase.EXTRA_TURN_DECISION:
                if self.players[self.activePlayer].getEffectiveSun() < 2:
                    self.makeMove((Move.PASS, self.activePlayer, ()))
                    return self.getOptions()
                ret = (
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (True,)),
                    (Move.TAKE_EXTRA_TURN, self.activePlayer, (False,)))
            case Phase.CHOOSE_SHIELD_FACE_1 | Phase.CHOOSE_SHIELD_FACE_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateChooseShield()
            case Phase.CHOOSE_CHAOS_FACE_1 | Phase.CHOOSE_CHAOS_FACE_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateChooseChaos()
            case Phase.CHOOSE_DOGGED_FACE_1 | Phase.CHOOSE_DOGGED_FACE_1:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateChooseDogged()
            case Phase.FORGE_FEAT_FACE_1 | Phase.FORGE_FEAT_FACE_2:
                ret = self.generateForgeFace(self.activePlayer)
            case Phase.RESOLVE_SHIPS | Phase.MINOR_RESOLVE_SHIPS:
                if self.players[self.blessingPlayer].times3ShipsToResolve > 0:
                    ret = self.generateBuyFace(self.blessingPlayer, 6)
                else:
                    ret = self.generateBuyFace(self.blessingPlayer, 2)
            case Phase.RESOLVE_SHIPS_FORGE | Phase.MINOR_RESOLVE_SHIPS_FORGE:
                ret = self.generateForgeFace(self.blessingPlayer)
            case Phase.MISFORTUNE_1_RESOLVE_SHIPS | Phase.MISFORTUNE_2_RESOLVE_SHIPS | Phase.MINOR_MISFORTUNE_SHIPS:
                ret = self.generateBuyFace(self.misfortunePlayer, 2)
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
            case Phase.SATYRS_CHOOSE_DIE_1:
                ret = self.generateSatyrsChooseDie(True)
            case Phase.SATYRS_CHOOSE_DIE_2:
                ret = self.generateSatyrsChooseDie(False)
            case Phase.NYMPH_1 | Phase.NYMPH_2:
                if self.players[self.activePlayer].goldToGain > 0:
                    ret = self.getHammerScepterChoices(self.activePlayer)
                elif self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateBuyFace(self.activePlayer, 0)
            case Phase.TRIDENT_1 | Phase.TRIDENT_2:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateTridentAction(self.activePlayer)
            case Phase.GODDESS_CHOOSE_FACES:
                ret = self.generateGoddessChoice(self.players[self.activePlayer])
            case Phase.RIGHTHAND_1 | Phase.RIGHTHAND_2:
                ret = self.generateRightHandChoice(self.players[self.activePlayer])
            case Phase.WIND_CHOOSE_RESOURCE:
                ret = (Move.CHOOSE_RESOURCE, self.activePlayer, (0,)), (
                    Move.CHOOSE_RESOURCE, self.activePlayer, (1,)), (Move.CHOOSE_RESOURCE, self.activePlayer, (2,)), (
                    Move.CHOOSE_RESOURCE, self.activePlayer, (3,)), (Move.CHOOSE_RESOURCE, self.activePlayer, (4,)), (
                    Move.CHOOSE_RESOURCE, self.activePlayer, (5,))
            case Phase.USE_ANCESTOR:
                if self.players[self.activePlayer].unforgedFaces:
                    ret = self.generateForgeFace(self.activePlayer)
                else:
                    ret = self.generateAncestorChoice(self.players[self.activePlayer])
            case Phase.TITAN_1 | Phase.TITAN_2:
                if self.players[self.activePlayer].goldToGain == 0:
                    ret = self.generateTitanChoice(self.activePlayer)
                else:
                    ret = self.getHammerScepterChoices(self.activePlayer)
        if ret[0][1] == self.activePlayer and self.players[self.activePlayer].tritonTokens >= 1:
            ret = list(ret)
            ret.append((Move.USE_TRITON_TOKEN, self.activePlayer, ("gold",)))
            if self.players[self.activePlayer].sun < self.players[self.activePlayer].maxSun:
                ret.append((Move.USE_TRITON_TOKEN, self.activePlayer, ("sun",)))
            if self.players[self.activePlayer].moon < self.players[self.activePlayer].maxMoon:
                ret.append((Move.USE_TRITON_TOKEN, self.activePlayer, ("moon",)))
            ret = tuple(ret)
        if ret[0][1] == self.activePlayer and self.players[self.activePlayer].companions:
            ret = list(ret)
            for companion in self.players[self.activePlayer].companions:
                if companion > 0:
                    move = Move.USE_COMPANION, self.activePlayer, (companion,)
                    if move not in ret:
                        ret.append(move)
            ret = tuple(ret)
        return ret

    def generateBuyFaces(self, gold):
        ret = []
        availableFaces = []
        if gold >= 2:
            if self.temple[0]:
                availableFaces.append(self.temple[0][0])
            if self.temple[1]:
                availableFaces.append(self.temple[1][0])
            if gold >= 3:
                if self.temple[2]:
                    availableFaces.append(self.temple[2][0])
                if self.temple[3]:
                    availableFaces.append(self.temple[3][0])
                if gold >= 4:
                    for face in self.temple[4]:
                        availableFaces.append(face)
                    if gold >= 5:
                        if self.temple[5]:
                            availableFaces.append(self.temple[5][0])
                        if gold >= 6:
                            if self.temple[6]:
                                availableFaces.append(self.temple[6][0])
                            if gold >= 8:
                                if self.temple[7]:
                                    availableFaces.append(self.temple[7][0])
                                if self.temple[8]:
                                    availableFaces.append(self.temple[8][0])
                                if gold >= 12:
                                    for face in self.temple[9]:
                                        availableFaces.append(face)
        for i in range(1, len(availableFaces) + 1):
            for combo in combinations(availableFaces, i):
                if Data.getTotalGoldCost(combo) <= gold:
                    ret.append((Move.BUY_FACES, self.activePlayer, tuple(combo)))
        ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def generateBuyFace(self, player, goldBonus):
        ret = []
        gold = self.players[player].getEffectiveGold() + goldBonus
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

    def generateTridentAction(self, playerID):
        ret = []
        for pool in self.temple:
            for face in pool:
                next = Move.BUY_FACES, playerID, (face,)
                if not next in ret:
                    ret.append(next)
        times3 = boar = ship = shield = mirror = False
        for island in self.islands:
            for feat in island:
                if feat == Data.HeroicFeat.HELMET_OF_INVISIBILITY:
                    times3 = True
                elif feat == Data.HeroicFeat.TENACIOUS_BOAR_RED or feat == Data.HeroicFeat.TENACIOUS_BOAR_RED or feat == Data.HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == Data.HeroicFeat.TENACIOUS_BOAR_GREEN:
                    boar = True
                elif feat == Data.HeroicFeat.CELESTIAL_SHIP:
                    ship = True
                elif feat == Data.HeroicFeat.THE_GUARDIANS_SHIELD:
                    shield = True
                elif feat == Data.HeroicFeat.MIRROR_OF_THE_ABYSS:
                    mirror = True
        for player in self.players:
            for feat in player.feats:
                if feat == Data.HeroicFeat.HELMET_OF_INVISIBILITY:
                    times3 = True
                elif feat == Data.HeroicFeat.TENACIOUS_BOAR_RED or feat == Data.HeroicFeat.TENACIOUS_BOAR_RED or feat == Data.HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == Data.HeroicFeat.TENACIOUS_BOAR_GREEN:
                    boar = True
                elif feat == Data.HeroicFeat.CELESTIAL_SHIP:
                    ship = True
                elif feat == Data.HeroicFeat.THE_GUARDIANS_SHIELD:
                    shield = True
                elif feat == Data.HeroicFeat.MIRROR_OF_THE_ABYSS:
                    mirror = True
        if not times3:
            ret.append((Move.BUY_FACES, playerID, (Data.DieFace.TIMES3,)))
        if not boar:
            ret.append((Move.BUY_FACES, playerID, (Data.DieFace.BOAR,)))
        if not ship:
            ret.append((Move.BUY_FACES, playerID, (Data.DieFace.SHIP,)))
        if not shield:
            for face in self.shields:
                ret.append((Move.BUY_FACES, playerID, (face,)))
        if not mirror:
            ret.append((Move.BUY_FACES, playerID, (Data.DieFace.MIRROR,)))
        if not ret:
            ret.append((Move.PASS, playerID, ()))
        return tuple(ret)

    def generatePerformFeats(self):
        ret = []
        sun = self.players[self.activePlayer].getEffectiveSun()
        moon = self.players[self.activePlayer].getEffectiveMoon()
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
        if self.islands[7] and self.players[self.activePlayer].canBuy55Feat():
            ret.append((Move.PERFORM_FEAT, self.activePlayer, (self.islands[7][0],)))
        ret.append((Move.PASS, self.activePlayer, ()))
        return tuple(ret)

    def generateForgeFace(self, player):
        ret = []
        face = self.players[player].unforgedFaces[0]
        for existingFace in self.players[player].die1.faces:
            if not Data.isBoarFace(existingFace) and not Data.isMisfortuneFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (True, face, existingFace)))
        for existingFace in self.players[player].die2.faces:
            if not Data.isBoarFace(existingFace) and not Data.isMisfortuneFace(existingFace):
                ret.append((Move.FORGE_FACE, player, (False, face, existingFace)))
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

    def generateChooseChaos(self):
        ret = []
        for face in self.chaos:
            ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
        return tuple(ret)

    def generateChooseDogged(self):
        ret = []
        for face in self.dogged:
            ret.append((Move.BUY_FACES, self.activePlayer, (face,)))
        return tuple(ret)

    def generateGoddessChoice(self, player):
        # choose a face on each die to place face up
        die1Faces = set(player.die1.faces)  # don't need duplicates
        die2Faces = set(player.die2.faces)
        ret = []
        for face1 in die1Faces:
            for face2 in die2Faces:
                ret.append((Move.CHOOSE_FACES, player.playerID, (face1, face2)))
        return tuple(ret)

    def generateRightHandChoice(self, player):
        ret = []
        i = 0
        max = player.getEffectiveGold()
        while i <= max:
            ret.append((Move.RIGHTHAND_SPEND, player.playerID, (i,)))
            i += 1
        return tuple(ret)

    def generateAncestorChoice(self, player):
        if Data.DieFace.VP1SUN1 in self.temple[4]:
            return (Move.BUY_FACES, player.playerID, (Data.DieFace.VP1SUN1,)),
        if self.temple[5]:
            return (Move.BUY_FACES, player.playerID, (self.temple[5][0],)),
        if self.temple[8]:
            return (Move.BUY_FACES, player.playerID, (self.temple[8][0],)),
        ret = []
        for face in self.temple[9]:
            if not face == Data.DieFace.GOLD2SUN2MOON2OR:
                ret.append((Move.BUY_FACES, player.playerID, (face,)))
        if not ret:
            return (Move.PASS, player.playerID, ()),
        return tuple(ret)

    def generateTitanChoice(self, player):
        ret = []
        if self.islands[0]:
            ret.append((Move.PERFORM_FEAT, player, (self.islands[0][0],)))
        if self.islands[1]:
            ret.append((Move.PERFORM_FEAT, player, (self.islands[1][0],)))
        if self.islands[13]:
            ret.append((Move.PERFORM_FEAT, player, (self.islands[13][0],)))
        if self.islands[14]:
            ret.append((Move.PERFORM_FEAT, player, (self.islands[14][0],)))
        return tuple(ret)

    def getSpendGoldOptions(self, player):
        ret = []
        i = player.goldToSpend - player.gold
        while i <= player.getScepterGold() and i <= player.goldToSpend:
            ret.append((Move.SPEND_GOLD, player.playerID,
                        (i,)))  # spend this amount from scepters, spend the rest from main reserve
            i += 1
        return tuple(ret)

    def getSpendSunOptions(self, player):
        ret = []
        i = 0  # counts scepter spends
        while i <= player.getScepterSunMoon() and i <= player.sunToSpend:
            j = 0  # counts ancient shards
            while j <= player.ancientShards and i + j <= player.sunToSpend:
                if i + j + player.sun >= player.sunToSpend and (
                        player.moonToSpend == 0 or player.canBuy55FeatAfterSunSpend(i, j)):
                    ret.append((Move.SPEND_SUN, player.playerID, (
                        i, j)))  # spend i from scepters, j ancient shards, and spend the rest from main reserve
                j += 1
            i += 1
        return tuple(ret)

    def getSpendMoonOptions(self, player):
        ret = []
        i = 0  # counts scepter spends
        while i <= player.getScepterSunMoon() and i <= player.moonToSpend:
            j = 0  # counts ancient shards
            while j <= player.ancientShards and i + j <= player.moonToSpend:
                if i + j + player.moon >= player.moonToSpend:
                    ret.append((Move.SPEND_MOON, player.playerID,
                                (
                                    i,
                                    j)))  # spend i from scepters, j ancient shards, and spend the rest from main reserve
                j += 1
            i += 1
        return tuple(ret)

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

    def generateCelestialDieDecision(self, player):
        return (Move.ROLL, player, (Data.DieFace.CELESTIAL12GOLD, 1)), (
            Move.ROLL, player, (Data.DieFace.CELESTIAL5VP, 1)), (
            Move.ROLL, player, (Data.DieFace.CELESTIAL3VPAND3GOLD1SUN1MOONOR, 1)), (
            Move.ROLL, player, (Data.DieFace.CELESTIALMIRROR, 1)), (
            Move.ROLL, player, (Data.DieFace.CELESTIALGODDESS, 1)), (
            Move.ROLL, player, (Data.DieFace.CELESTIALUPGRADE, 1)), (Move.RANDOM_ROLL, player, ())

    def celestialDieRandomRoll(self):
        return random.choice((Data.DieFace.CELESTIAL12GOLD, Data.DieFace.CELESTIAL5VP,
                              Data.DieFace.CELESTIAL3VPAND3GOLD1SUN1MOONOR, Data.DieFace.CELESTIALGODDESS,
                              Data.DieFace.CELESTIALUPGRADE))

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
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def getHammerScepterChoices(self, player):
        if self.players[player].canAddHammer():
            return self.getHammerChoices(player)
        return self.getScepterChoices(player)

    def getCelestialUpgradeChoices(self, player):
        ret = []
        faces = set(player.die1.faces)
        for face in faces:
            level = Data.getLevel(face)
            if level > 5:
                continue
            pool = self.getUpgradePool(level + 2)
            for upgradeFace in pool:
                ret.append(
                    (Move.CELESTIAL_UPGRADE, player.playerID, (True, face, upgradeFace)))
        faces = set(player.die2.faces)
        for face in faces:
            level = Data.getLevel(face)
            if level > 5:
                continue
            pool = self.getUpgradePool(level + 2)
            for upgradeFace in pool:
                ret.append((Move.CELESTIAL_UPGRADE, player.playerID, (False, face, upgradeFace)))
        if not ret:
            return (Move.PASS, player.playerID, ()),
        return tuple(ret)

    def getCelestialMirrorChoices(self, playerID):
        ret = []
        for player in self.players:
            if player.getDie1UpFace() != Data.DieFace.MIRROR:
                ret.append((Move.CELESTIAL_MIRROR_CHOICE, playerID, (player.getDie1UpFace(),)))
            if player.getDie2UpFace() != Data.DieFace.MIRROR:
                ret.append((Move.CELESTIAL_MIRROR_CHOICE, playerID, (player.getDie2UpFace(),)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def getCelestialGoddessChoices(self, player):
        ret = []
        faces = set(player.die1.faces)
        for face in faces:
            ret.append((Move.CELESTIAL_GODDESS, player.playerID, (True, face)))
        faces = set(player.die2.faces)
        for face in faces:
            ret.append((Move.CELESTIAL_GODDESS, player.playerID, (False, face)))
        return tuple(ret)

    def generateMerchantChoices(self, player):
        ret = []
        levels = player.getMerchantCount()
        faces = set(player.die1.faces)
        for face in faces:
            level = Data.getLevel(face)
            if level == 7:
                continue
            upgrade = 1
            while upgrade <= levels:
                pool = self.getUpgradePool(level + upgrade)
                for upgradeFace in pool:
                    ret.append(
                        (Move.MERCHANT_UPGRADE, player.playerID, (2 * (levels - upgrade), True, face, upgradeFace)))
                upgrade += 1
        faces = set(player.die2.faces)
        for face in faces:
            level = Data.getLevel(face)
            if level == 7:
                continue
            upgrade = 1
            while upgrade <= levels:
                pool = self.getUpgradePool(level + upgrade)
                for upgradeFace in pool:
                    ret.append(
                        (Move.MERCHANT_UPGRADE, player.playerID, (2 * (levels - upgrade), False, face, upgradeFace)))
                upgrade += 1
        ret.append((Move.MERCHANT_UPGRADE, player.playerID, (2 * levels,)))
        return tuple(ret)

    def getUpgradePool(self, level):
        ret = []
        match level:
            case 1:
                if self.temple[0]:
                    ret.append(self.temple[0][0])
                if self.temple[1]:
                    ret.append(self.temple[1][0])
            case 2:
                if self.temple[2]:
                    ret.append(self.temple[2][0])
                if self.temple[3]:
                    ret.append(self.temple[3][0])
            case 3:
                for face in self.temple[4]:
                    ret.append(face)
            case 4:
                if self.temple[5]:
                    ret.append(self.temple[5][0])
            case 5:
                if self.temple[6]:
                    ret.append(self.temple[6][0])
            case 6:
                if self.temple[7]:
                    ret.append(self.temple[7][0])
                if self.temple[8]:
                    ret.append(self.temple[8][0])
            case 7:
                if self.temple[9]:
                    ret.append(self.temple[9][0])
            case _:
                return tuple()
        if not ret:
            return self.getUpgradePool(level + 1)
        return tuple(ret)

    def getMazeMoveChoices(self, player):
        ret = []
        if player.mazeMoves > 0:
            options = Data.getMazeMoveOptions(player.mazePosition)
        else:
            options = Data.getReverseMazeMoveOptions(player.mazePosition)
        for move in options:
            ret.append((Move.MAZE_MOVE, player.playerID, (move,)))
        return tuple(ret)

    def getMazeEffectOrChoices(self, player):
        ret = []
        resources = Data.getMazeOrEffects(player.mazePosition)
        if resources[0] > 0:
            ret.append((Move.CHOOSE_MAZE_OR, player.playerID, (0,)))
        if resources[1] > 0:
            ret.append((Move.CHOOSE_MAZE_OR, player.playerID, (1,)))
        if resources[2] > 0:
            ret.append((Move.CHOOSE_MAZE_OR, player.playerID, (2,)))
        if resources[3] > 0:
            ret.append((Move.CHOOSE_MAZE_OR, player.playerID, (3,)))
        return tuple(ret)

    def getHammerChoices(self, player):
        hammerLeft = self.players[player].getMaxHammer() - self.players[player].hammerTrack
        goldToSpend = self.players[player].goldToGain
        ret = []
        i = max(goldToSpend - (self.players[player].maxGold - self.players[player].gold), 0)
        while i <= hammerLeft and i <= goldToSpend:
            ret.append((Move.CHOOSE_ADD_HAMMER_SCEPTER, player, (i,)))  # spend i gold on hammer, remainder is gained
            i += 1
        if not ret:
            ret.append((Move.CHOOSE_ADD_HAMMER_SCEPTER, player, (i,)))  # this will happen if both can be maxed out
        return tuple(ret)

    def getScepterChoices(self, player):
        scepterSpace = self.players[player].getScepterSpace()
        goldToSpend = self.players[player].goldToGain
        ret = []
        i = max(goldToSpend - (self.players[player].maxGold - self.players[player].gold), 0)
        while i <= scepterSpace and i <= goldToSpend:
            ret.append((Move.CHOOSE_ADD_HAMMER_SCEPTER, player, (i,)))  # spend i gold on scepter, remainder is gained
            i += 1
        if not ret:
            ret.append((Move.CHOOSE_ADD_HAMMER_SCEPTER, player, (i,)))  # this will happen if both can be maxed out
        return tuple(ret)

    def generateSatyrsChooseDie(self, die1):
        picked = -1
        if not die1:
            picked = self.players[self.activePlayer].orChoice1
        ret = []
        for player in self.players:
            if player.playerID == self.activePlayer:
                continue
            next = player.playerID * 2
            if not picked == next:
                ret.append((Move.SATYRS_CHOOSE_DIE, self.activePlayer, (next,)))
            if not picked == next + 1:
                ret.append((Move.SATYRS_CHOOSE_DIE, self.activePlayer, (next + 1,)))
        return tuple(ret)

    def generateLightChoices(self):
        ret = []
        for player in self.players:
            if player.getDie1UpFace() != Data.DieFace.MIRROR:
                move = Move.USE_LIGHT, self.activePlayer, (True, player.getDie1UpFace())
                if not move in ret:
                    ret.append(move)
            if player.getDie2UpFace() != Data.DieFace.MIRROR:
                move = Move.USE_LIGHT, self.activePlayer, (True, player.getDie2UpFace())
                if not move in ret:
                    ret.append(move)
        ret.append((Move.USE_LIGHT, self.activePlayer, (False,)))
        return tuple(ret)

    def makeReturnMove(self, player):
        self.sentinel = False
        self.cyclops = False
        match self.returnPhase:
            case Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 | Phase.ACTIVE_PLAYER_PERFORM_FEAT_2:
                self.makeMove((Move.RETURN_TO_FEAT, player, ()))
            case _:
                self.makeMove((Move.PASS, player, ()))

    def checkBasicMazeEffect(self, player):
        match Data.getMazeEffect(player.mazePosition):
            case "NONE":
                return True
            case "SUN1":
                player.gainSun(1, False)
                return True
            case "MOON1":
                player.gainMoon(1, False)
                return True
            case "VP3":
                player.gainVP(3)
                return True
            case "VP5":
                player.gainVP(5)
                return True
            case "VP3SUN1MOON1":
                player.gainVP(3)
                player.gainSun(1, False)
                player.gainMoon(1, False)
                return True
            case "VP2STEAL":
                steal = 0
                for pl in self.players:
                    if player.playerID == pl.playerID:
                        continue
                    steal += max(2, pl.vp)
                    pl.gainVP(-2)
                player.gainVP(steal)
                return True
            case "CELESTIALDIE1":
                player.celestialRolls += 1
                return True
            case "CELESTIALDIE2":
                player.celestialRolls += 2
                return True
            case "CELESTIALDIE2":
                player.celestialRolls += 2
                return True
            case "GOLD6":
                player.gainGold(6, False)
                return player.goldToGain == 0
            case "1VPPERFORGE":
                player.gainVP(player.numForged)
                return True
            case "GODDESS":
                player.gainVP(player.numForged)
                for pl in self.players:
                    if player.playerID == pl.playerID:
                        continue
                    if pl.mazePosition == 35:
                        return True
            case "TREASUREHALL":
                for treasure in self.treasures:
                    if treasure[1] == player.mazePosition:
                        match treasure[0]:
                            case Data.Treasure.VP_TREASURE:
                                player.gainVP(2)
                            case Data.Treasure.SUN_TREASURE:
                                player.gainSun(1, False)
                            case Data.Treasure.MOON_TREASURE:
                                player.gainMoon(1, False)
                        return True
        return False

    def gainTreasureEffect(self, treasure, player):
        match treasure:
            case Data.Treasure.VP_TREASURE:
                player.gainVP(10)
            case Data.Treasure.SUN_TREASURE:
                player.gainSun(4, False)
            case Data.Treasure.MOON_TREASURE:
                player.gainMoon(4, False)

    def gainSmallTreasureEffect(self, treasure, player):
        match treasure:
            case Data.Treasure.VP_TREASURE:
                player.gainVP(2)
            case Data.Treasure.SUN_TREASURE:
                player.gainSun(1, False)
            case Data.Treasure.MOON_TREASURE:
                player.gainMoon(1, False)

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
            case "GUARDIAN_REINF":
                self.phase = Phase.RESOLVE_GUARDIAN_REINF

    def resolveInstEffect(self, effect):
        match effect:
            case "SPIRITS_INST":
                if self.players[self.activePlayer].scepters:
                    # it is possible to spend gold from scepter tracks to pay for the feat
                    # this can open up space for gold, but happens after this, so delay the gold gain
                    self.players[self.activePlayer].goldToGain = 3
                else:
                    self.players[self.activePlayer].gainGold(3, False)
                self.players[self.activePlayer].gainMoon(3, False)
                if self.players[self.activePlayer].goldToGain == 0:
                    self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SHIP_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.SHIP)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_FEAT_FACE_1
                else:
                    self.phase = Phase.FORGE_FEAT_FACE_2
            case "SHIELD_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_SHIELD_FACE_1
                else:
                    self.phase = Phase.CHOOSE_SHIELD_FACE_2
            case "MINOTAUR_INST":
                self.minotaur = True
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.ROLL_DIE_1
                self.blessingPlayer = (self.activePlayer + 1) % len(self.players)
            case "TRITON_INST":
                self.players[self.activePlayer].tritonTokens += 1
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "MIRROR_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.MIRROR)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_FEAT_FACE_1
                else:
                    self.phase = Phase.FORGE_FEAT_FACE_2
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
                    self.phase = Phase.FORGE_FEAT_FACE_1
                else:
                    self.phase = Phase.FORGE_FEAT_FACE_2
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
                self.satyrs = True
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.ROLL_DIE_1
                self.blessingPlayer = (self.activePlayer + 1) % len(self.players)
            case "CHEST_INST":
                self.players[self.activePlayer].chestEffect()
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "HAMMER_INST":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # handled elsewhere
            case "NYMPH_INST":
                self.players[self.activePlayer].gainGold(4, False)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1 or self.phase == Phase.TITAN_1:
                    self.phase = Phase.NYMPH_1
                else:
                    self.phase = Phase.NYMPH_2
            case "OMNISCIENT_INST":
                vpFaces = 0
                for face in self.players[self.activePlayer].die1.faces:
                    if face == Data.DieFace.VP2 or face == Data.DieFace.VP3 or face == Data.DieFace.VP4 or face == Data.DieFace.VP1SUN1 or face == Data.DieFace.GOLD3VP2OR or face == Data.DieFace.GOLD1SUN1MOON1VP1 or face == Data.DieFace.MOON2VP2 or face == Data.DieFace.REDSHIELD or face == Data.DieFace.BLUESHIELD or face == Data.DieFace.YELLOWSHIELD or face == Data.DieFace.GREENSHIELD or face == Data.DieFace.VP1GOLD2LOYALTY1 or face == Data.DieFace.REDCHAOS or face == Data.DieFace.BLUECHAOS or face == Data.DieFace.YELLOWCHAOS or face == Data.DieFace.GREENCHAOS:
                        vpFaces += 1
                for face in self.players[self.activePlayer].die2.faces:
                    if face == Data.DieFace.VP2 or face == Data.DieFace.VP3 or face == Data.DieFace.VP4 or face == Data.DieFace.VP1SUN1 or face == Data.DieFace.GOLD3VP2OR or face == Data.DieFace.GOLD1SUN1MOON1VP1 or face == Data.DieFace.MOON2VP2 or face == Data.DieFace.REDSHIELD or face == Data.DieFace.BLUESHIELD or face == Data.DieFace.YELLOWSHIELD or face == Data.DieFace.GREENSHIELD or face == Data.DieFace.VP1GOLD2LOYALTY1 or face == Data.DieFace.REDCHAOS or face == Data.DieFace.BLUECHAOS or face == Data.DieFace.YELLOWCHAOS or face == Data.DieFace.GREENCHAOS:
                        vpFaces += 1
                self.players[self.activePlayer].gainVP(2 * vpFaces)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "GOLDSMITH_INST":
                feats = set()
                for feat in self.players[self.activePlayer].feats:
                    if feat == Data.HeroicFeat.TENACIOUS_BOAR_RED or feat == Data.HeroicFeat.TENACIOUS_BOAR_BLUE or feat == Data.HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == Data.HeroicFeat.TENACIOUS_BOAR_GREEN:
                        feats.add(Data.HeroicFeat.TENACIOUS_BOAR)
                    elif feat == Data.HeroicFeat.MIRROR_OF_MISFORTUNE_RED or feat == Data.HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE or feat == Data.HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW or feat == Data.HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN:
                        feats.add(Data.HeroicFeat.THE_MIRROR_OF_MISFORTUNE)
                    else:
                        feats.add(feat)
                self.players[self.activePlayer].gainVP(2 * len(feats))
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "TRIDENT_INST":
                self.players[self.activePlayer].gold = 0
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.TRIDENT_1
                else:
                    self.phase = Phase.TRIDENT_2
            case "LEFTHAND_INST":
                for player in self.players:
                    if player.location != 0 and player.playerID != self.activePlayer:
                        # another player will be ousted, so activate bears for active player
                        self.players[self.activePlayer].checkBears()
                        break
                self.players[self.activePlayer].location = 0
                self.blessingPlayer = self.activePlayer  # active player will always need to be ousted so start there
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.LEFT_HAND_ROLL_1_1
                else:
                    self.phase = Phase.LEFT_HAND_ROLL_1_2
            case "FIRE_INST":
                self.eternalFire = True
                self.phase = Phase.TURN_START
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "TITAN_INST":
                if self.islands[0] or self.islands[1] or self.islands[13] or self.islands[14]:
                    if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                        self.phase = Phase.TITAN_1
                    else:
                        self.phase = Phase.TITAN_2
                else:
                    self.makeMove((Move.PASS, self.activePlayer, ()))
            case "GODDESS_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.phase = Phase.GODDESS_CHOOSE_FACES
            case "RIGHTHAND_INST":
                if self.players[self.activePlayer].getEffectiveGold() > 0:
                    if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                        self.phase = Phase.RIGHTHAND_1
                    else:
                        self.phase = Phase.RIGHTHAND_2
                else:
                    self.makeMove((Move.PASS, self.activePlayer, ()))
            case "NIGHT_INST":
                sunLost = moonLost = 0
                for player in self.players:
                    if player.playerID == self.activePlayer:
                        continue
                    sunLost += min(1, player.sun)
                    player.gainSun(-1, True)  # should only come from reserve
                    moonLost += min(1, player.moon)
                    player.gainMoon(-1, True)  # should only come from reserve
                self.players[self.activePlayer].gainSun(sunLost, False)
                self.players[self.activePlayer].gainMoon(moonLost, False)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "MISTS_INST":
                minGold = self.players[0].gold
                for player in self.players:
                    if player.gold < minGold:  # only checks regular reserve
                        minGold = player.gold
                vpLost = 0
                for player in self.players:
                    if player.gold == minGold:
                        vpLost += min(5, player.vp)
                        player.gainVP(-5)
                self.players[self.activePlayer].gainVP(vpLost)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "ANCESTOR_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.USE_ANCESTOR
            case "WIND_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.returnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.returnPhase = Phase.END_TURN
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.WIND_ROLL_DIE_1
            case "DIE_INST":
                self.players[self.activePlayer].celestialRolls += 1
                self.celestialPlayer = self.activePlayer
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.celestialReturnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.celestialReturnPhase = Phase.END_TURN
                self.phase = Phase.ROLL_CELESTIAL_DIE
            case "COMPANION_INST_REINF":
                self.players[self.activePlayer].companions.append(0)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SCEPTER_INST":
                self.players[self.activePlayer].scepters.append(0)
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "MOONGOLEM_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.MAZEBLUE)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_FEAT_FACE_1
                else:
                    self.phase = Phase.FORGE_FEAT_FACE_2
            case "GREATGOLEM_INST":
                self.players[self.activePlayer].mazeMoves = 2
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.RESOLVE_MAZE_MOVES
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.mazeReturnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.mazeReturnPhase = Phase.END_TURN
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "SUNGOLEM_INST":
                self.players[self.activePlayer].unforgedFaces.append(Data.DieFace.MAZERED)
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.FORGE_FEAT_FACE_1
                else:
                    self.phase = Phase.FORGE_FEAT_FACE_2
            case "TIMEGOLEM_INST":
                self.players[self.activePlayer].mazeMoves = -2
                self.blessingPlayer = self.activePlayer
                self.phase = Phase.RESOLVE_MAZE_MOVES
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.mazeReturnPhase = Phase.EXTRA_TURN_DECISION
                else:
                    self.mazeReturnPhase = Phase.END_TURN
                self.makeMove((Move.PASS, self.activePlayer, ()))
            case "MEMORY_INST_AUTO":
                self.makeMove((Move.PASS, self.activePlayer, ()))  # todo
            case "CHAOS_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_CHAOS_FACE_1
                else:
                    self.phase = Phase.CHOOSE_CHAOS_FACE_2
            case "DOGGED_INST":
                if self.phase == Phase.ACTIVE_PLAYER_PERFORM_FEAT_1:
                    self.phase = Phase.CHOOSE_DOGGED_FACE_1
                else:
                    self.phase = Phase.CHOOSE_DOGGED_FACE_2
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

    def advanceActivePlayer(self, prevPlayer):
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

    def printPlayersInfo(self):
        print(f"Player {self.activePlayer} is the active player.")
        print(f"Current blessing player: {self.blessingPlayer}")
        print("Players:")
        for p in self.players:
            p.printPlayerInfo()
            print(f"die 1 result buffer: {p.die1ResultBuffer}")
            print(f"die 2 result buffer: {p.die2ResultBuffer}")
            print(f"or choice 1: {p.orChoice1}")
            print(f"or choice 2: {p.orChoice2}")
            print(f"mirror choice 1: {p.mirrorChoice1}")
            print(f"mirror choice 2: {p.mirrorChoice2}")

    def printPoints(self):
        print("Victory Points:")
        for player in self.players:
            print(f"Player {player.playerID}: {player.vp}")

    def setup(self):
        self.selectRandomFeats()
        self.players[0].gainGold(3, False)
        self.players[1].gainGold(2, False)
        if len(self.players) > 2:
            self.players[2].gainGold(1, False)
        if len(self.players) == 2:
            for pool in self.temple:
                if Data.DieFace.GOLD6 in pool:
                    pool.remove(Data.DieFace.GOLD6)
                else:
                    pool.remove(random.choice(pool))
                pool.remove(random.choice(pool))
        if self.module == 1:
            self.treasures = [Data.Treasure.VP_TREASURE, -1], [Data.Treasure.SUN_TREASURE, -1], [
                Data.Treasure.MOON_TREASURE, -1]

    def selectRandomFeats(self):
        i = 0
        while i < 15:
            if i == 2 and self.module == 1:
                self.addFeat(i, Data.HeroicFeat.THE_SUN_GOLEM)
                i += 1
                continue
            if i == 3 and self.module == 1:
                self.addFeat(i, Data.HeroicFeat.THE_TIME_GOLEM)
                i += 1
                continue
            if i == 9 and self.module == 1:
                self.addFeat(i, Data.HeroicFeat.THE_GREAT_GOLEM)
                i += 1
                continue
            if i == 12 and self.module == 1:
                self.addFeat(i, Data.HeroicFeat.THE_MOON_GOLEM)
                i += 1
                continue
            if i == 1 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_DOGGED)
                i += 1
                continue
            if i == 2 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_GUARDIAN)
                i += 1
                continue
            if i == 5 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_MIRROR_OF_MISFORTUNE)
                i += 1
                continue
            if i == 9 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_CHAOS)
                i += 1
                continue
            if i == 12 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_ORACLE)
                i += 1
                continue
            if i == 13 and self.module == 2:
                self.addFeat(i, Data.HeroicFeat.THE_MEMORY)
                i += 1
                continue
            feats = Data.getFeatsByPosition(i)
            self.addFeat(i, feats[random.randrange(len(feats))])
            i += 1
        self.shields = [Data.DieFace.REDSHIELD, Data.DieFace.YELLOWSHIELD, Data.DieFace.GREENSHIELD,
                        Data.DieFace.BLUESHIELD]  # always need these in case of abyssal trident

    def addFeat(self, island, feat):
        if feat == Data.HeroicFeat.TENACIOUS_BOAR:
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_RED)
            self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_BLUE)
            if len(self.players) > 2:
                self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_GREEN)
                if len(self.players) > 3:
                    self.islands[island].append(Data.HeroicFeat.TENACIOUS_BOAR_YELLOW)
        elif feat == Data.HeroicFeat.THE_MIRROR_OF_MISFORTUNE:
            self.islands[island].append(Data.HeroicFeat.MIRROR_OF_MISFORTUNE_RED)
            self.islands[island].append(Data.HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE)
            if len(self.players) > 2:
                self.islands[island].append(Data.HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN)
                if len(self.players) > 3:
                    self.islands[island].append(Data.HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW)
        else:
            if feat == Data.HeroicFeat.THE_CHAOS:
                self.chaos = [Data.DieFace.REDCHAOS, Data.DieFace.YELLOWCHAOS, Data.DieFace.GREENCHAOS,
                              Data.DieFace.BLUECHAOS]
            elif feat == Data.HeroicFeat.THE_DOGGED:
                self.dogged = [Data.DieFace.GOLD3ANCIENTSHARD1, Data.DieFace.GOLD3ANCIENTSHARD1,
                               Data.DieFace.VP1GOLD2LOYALTY1, Data.DieFace.VP1GOLD2LOYALTY1]
            j = 0
            while j < len(self.players):
                self.islands[island].append(feat)
                j += 1


class Player:
    def __init__(self, playerID, ai, module):
        self.module = module
        self.playerID = playerID
        self.ai = ai
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
        self.die1MazeResultBuffer = None
        self.die2MazeResultBuffer = None
        self.celestialResultBuffer = None
        self.celestialOrChoice = 0
        self.mirrorChoice1 = None
        self.mirrorChoice2 = None
        self.mirrorMazeChoice1 = None
        self.mirrorMazeChoice2 = None
        self.orChoice1 = 0
        self.orChoice2 = 0
        self.orMazeChoice1 = 0
        self.orMazeChoice2 = 0
        self.dieChoice = True
        self.sentinel1Choice = False
        self.sentinel2Choice = False
        self.feats = []
        self.die1 = createLightDie(module)
        self.die2 = createDarkDie(module)
        self.location = 0  # 0 is portal, 1-7 are islands
        self.numForged = 0  # number of faces forged
        self.unforgedFaces = []
        self.unusedReinfEffects = []
        self.companions = []
        self.scepters = []
        self.allegiance = 0  # position on loyalty track
        self.mazePosition = 0  # position in maze
        self.mazeMoves = 0
        self.shipsToResolve = 0
        self.times3ShipsToResolve = 0
        self.celestialRolls = 0
        self.hammerTrack = 0
        self.goldToGain = 0  # can choose to spend on hammers or scepters
        self.goldToSpend = 0  # can spend from track or scepters
        self.sunToSpend = 0
        self.moonToSpend = 0

    def copyPlayer(self):
        ret = Player(self.playerID, self.ai, self.module)
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
        ret.die1MazeResultBuffer = self.die1MazeResultBuffer
        ret.die2MazeResultBuffer = self.die2MazeResultBuffer
        ret.celestialResultBuffer = self.celestialResultBuffer
        ret.celestialOrChoice = self.celestialOrChoice
        ret.mirrorChoice1 = self.mirrorChoice1
        ret.mirrorChoice2 = self.mirrorChoice2
        ret.mirrorMazeChoice1 = self.mirrorMazeChoice1
        ret.mirrorMazeChoice2 = self.mirrorMazeChoice2
        ret.orChoice1 = self.orChoice1
        ret.orChoice2 = self.orChoice2
        ret.orMazeChoice1 = self.orMazeChoice1
        ret.orMazeChoice2 = self.orMazeChoice2
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
        ret.scepters = copy.deepcopy(self.scepters)
        ret.allegiance = self.allegiance
        ret.mazePosition = self.mazePosition
        ret.mazeMoves = self.mazeMoves
        ret.shipsToResolve = self.shipsToResolve
        ret.times3ShipsToResolve = self.times3ShipsToResolve
        ret.celestialRolls = self.celestialRolls
        ret.hammerTrack = self.hammerTrack
        ret.goldToGain = self.goldToGain
        ret.goldToSpend = self.goldToSpend
        ret.sunToSpend = self.sunToSpend
        ret.moonToSpend = self.moonToSpend
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

    def getMazeDie1Result(self):
        if self.die1MazeResultBuffer == Data.DieFace.MIRROR:
            return self.mirrorMazeChoice1
        return self.die1MazeResultBuffer

    def getMazeDie2Result(self):
        if self.die2MazeResultBuffer == Data.DieFace.MIRROR:
            return self.mirrorMazeChoice2
        return self.die2MazeResultBuffer

    def gainGold(self, amount, reserveOnly):
        if (self.canAddHammer() or self.canAddScepter()) and amount > 0:
            self.goldToGain += amount
        elif amount < 0 < self.getScepterGold() and not reserveOnly:
            self.goldToSpend -= amount
        else:
            self.gold = max(min(self.gold + amount, self.maxGold), 0)

    def spendGold(self, scepter):
        i = len(self.scepters) - 1
        toSpend = scepter
        while i >= 0 and toSpend >= 0:
            next = min(self.scepters[i], toSpend)
            self.scepters[i] -= next
            toSpend -= next
            i -= 1
        self.gold = max(self.gold - (self.goldToSpend - scepter), 0)
        self.goldToSpend = 0

    def gainSun(self, amount, reserveOnly):
        if amount < 0 and (self.ancientShards > 0 or self.getScepterSunMoon() > 0) and not reserveOnly:
            self.sunToSpend -= amount
        else:
            self.sun = max(min(self.sun + amount, self.maxSun), 0)

    def spendSun(self, scepter, ancientShard):
        toSpend = scepter
        if scepter > 1:
            i = len(self.scepters) - 1
            while i >= 0 and toSpend > 0 and toSpend != 1:
                if self.scepters[i] == 6:
                    self.scepters[i] = 0
                    toSpend -= 2
                i -= 1
        i = len(self.scepters) - 1
        while i >= 0 and toSpend > 0:
            if self.scepters[i] > 3:
                self.scepters[i] = 0
                toSpend -= 1
            i -= 1
        self.scepters.sort(reverse=True)
        self.ancientShards = max(self.ancientShards - ancientShard, 0)
        self.sun = max(self.sun - (self.sunToSpend - scepter - ancientShard), 0)
        self.sunToSpend = 0

    def gainMoon(self, amount, reserveOnly):
        if amount < 0 and (self.ancientShards > 0 or self.getScepterSunMoon() > 0) and not reserveOnly:
            self.moonToSpend -= amount
        else:
            self.moon = max(min(self.moon + amount, self.maxMoon), 0)

    def spendMoon(self, scepter, ancientShard):
        toSpend = scepter
        if scepter > 1:
            i = len(self.scepters) - 1
            while i >= 0 and toSpend > 0 and toSpend != 1:
                if self.scepters[i] == 6:
                    self.scepters[i] = 0
                    toSpend -= 2
                i -= 1
        i = len(self.scepters) - 1
        while i >= 0 and toSpend > 0:
            if self.scepters[i] > 3:
                self.scepters[i] = 0
                toSpend -= 1
            i -= 1
        self.scepters.sort(reverse=True)
        self.ancientShards = max(self.ancientShards - ancientShard, 0)
        self.moon = max(self.moon - (self.moonToSpend - scepter - ancientShard), 0)
        self.moonToSpend = 0

    def gainVP(self, amount):
        self.vp = max(self.vp + amount, 0)

    def hasMaxSun(self):
        return self.sun == self.maxSun

    def hasMaxMoon(self):
        return self.moon == self.maxMoon

    def getEffectiveGold(self):
        ret = self.gold
        for scepter in self.scepters:
            ret += scepter
        return ret

    def getEffectiveSun(self):
        ret = self.sun
        for scepter in self.scepters:
            if scepter == 6:
                ret += 2
            elif scepter > 3:
                ret += 1
        ret += self.ancientShards
        return ret

    def getEffectiveMoon(self):
        ret = self.moon
        for scepter in self.scepters:
            if scepter == 6:
                ret += 2
            elif scepter > 3:
                ret += 1
        ret += self.ancientShards
        return ret

    def gainAncientShards(self, amount):
        self.ancientShards = max(min(self.ancientShards + amount, 6), 0)
        # todo: advance on loyalty track

    def gainLoyalty(self, amount):
        pass  # todo: advance on loyalty track

    def getMaxHammer(self):
        ret = 0
        for feat in self.feats:
            if feat == Data.HeroicFeat.THE_BLACKSMITHS_HAMMER:
                ret += 30
        return ret

    def canAddHammer(self):
        return self.hammerTrack < self.getMaxHammer()

    def canAddScepter(self):
        for scepter in self.scepters:
            if scepter < 6:
                return True
        return False

    def getScepterSpace(self):
        ret = 0
        for scepter in self.scepters:
            ret += 6 - scepter
        return ret

    def getScepterGold(self):
        ret = 0
        for scepter in self.scepters:
            ret += scepter
        return ret

    def getScepterSunMoon(self):
        ret = 0
        for scepter in self.scepters:
            if scepter == 6:
                ret += 2
            elif scepter > 3:
                ret += 1
        return ret

    def addHammer(self, amount):
        beforeHammer = self.hammerTrack
        self.hammerTrack = min(self.hammerTrack + amount, self.getMaxHammer())
        i = 1
        while i < 9:
            if self.hammerTrack >= 15 * i > beforeHammer:
                if i % 2 == 0:
                    self.gainVP(15)
                else:
                    self.gainVP(10)
            i += 1

    def addScepter(self, amount):  # just adding to scepters in order should be optimal
        i = 0
        toSpend = amount
        while i < len(self.scepters) and toSpend > 0:
            spend = min(6 - self.scepters[i], toSpend)
            self.scepters[i] = self.scepters[i] + spend
            toSpend -= spend
            i += 1

    def useHammerOrScepter(self, amount):  # spend hammerAmount on hammer or scepter, gain remainder as gold
        if self.canAddScepter():
            self.addScepter(amount)
        else:
            self.addHammer(amount)
        self.gold = min(self.gold + self.goldToGain - amount, self.maxGold)
        self.goldToGain = 0

    def die1IsBoar(self):
        if self.die1ResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorChoice1)
        return Data.isBoarFace(self.die1ResultBuffer)

    def die2IsBoar(self):
        if self.die2ResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorChoice2)
        return Data.isBoarFace(self.die2ResultBuffer)

    def die1MazeIsBoar(self):
        if self.die1MazeResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorMazeChoice1)
        return Data.isBoarFace(self.die1MazeResultBuffer)

    def die2MazeIsBoar(self):
        if self.die2MazeResultBuffer == Data.DieFace.MIRROR:
            return Data.isBoarFace(self.mirrorMazeChoice2)
        return Data.isBoarFace(self.die2MazeResultBuffer)

    def celestialIsBoar(self):
        return Data.isBoarFace(self.celestialResultBuffer)

    def populateTwins(self):
        self.twinsToUse = 0
        for feat in self.feats:
            if feat == Data.HeroicFeat.THE_TWINS:
                self.twinsToUse += 1

    def canBuy55Feat(self):
        ancientShardsLeft = self.ancientShards
        scepter1 = 0  # number of scepters that can spend for 1 sun/moon
        scepter2 = 0  # number of scepters that can spend for 2 sun/moon
        for scepter in self.scepters:
            if scepter == 6:
                scepter2 += 1
            elif scepter > 3:
                scepter1 += 1
        sun = self.sun
        while sun < 5:
            if scepter1 == 0 and scepter2 == 0 and ancientShardsLeft == 0:
                break
            if sun == 4 and scepter1 > 0:
                scepter1 -= 1
                sun += 1
            else:
                if scepter2 > 0:
                    scepter2 -= 1
                    sun += 2
                elif ancientShardsLeft > 0:
                    ancientShardsLeft -= 1
                    sun += 1
                else:
                    scepter1 -= 1
                    sun += 1
        moon = self.moon + ancientShardsLeft + scepter1 + scepter2 * 2
        return sun >= 5 and moon >= 5

    def canBuy55FeatAfterSunSpend(self, scepter, ancientShard):
        scepter1 = 0  # number of scepters that can spend for 1 sun/moon
        scepter2 = 0  # number of scepters that can spend for 2 sun/moon
        for scept in self.scepters:
            if scept == 6:
                scepter2 += 1
            elif scept > 3:
                scepter1 += 1
        scepterLeft = scepter2 * 2 + scepter1
        scepterSpent = 0
        while scepterSpent < scepter:
            if scepter - scepterSpent == 1 and scepter1 > 0:
                scepter1 -= 1
                scepterLeft -= 1
                scepterSpent += 1
            elif scepter2 > 0:
                scepter2 -= 1
                scepterLeft -= 2
                scepterSpent += 2
            else:
                scepter1 -= 1
                scepterLeft -= 1
                scepterSpent += 1
        return self.moon + self.ancientShards - ancientShard + scepterLeft >= 5

    def setBuffers(self):
        self.die1ResultBuffer = self.die1.getUpFace()
        self.die2ResultBuffer = self.die2.getUpFace()

    def setMazeBuffers(self):
        self.die1MazeResultBuffer = self.die1.getUpFace()
        self.die2MazeResultBuffer = self.die2.getUpFace()

    def gainWindResources(self, face, resourceType):
        if face == Data.DieFace.REDSHIELD:
            self.gainSun(2, False)
            return
        if face == Data.DieFace.BLUESHIELD:
            self.gainMoon(2, False)
            return
        if face == Data.DieFace.YELLOWSHIELD:
            self.gainGold(3, False)
            return
        if face == Data.DieFace.GREENSHIELD:
            self.gainVP(3)
            return
        if face == Data.DieFace.REDCHAOS or face == Data.DieFace.BLUECHAOS:
            self.gainAncientShards(2)
            return
        if face == Data.DieFace.YELLOWCHAOS or face == Data.DieFace.GREENCHAOS:
            self.gainLoyalty(2)
            return
        match resourceType:
            case 0:
                self.gainGold(Data.getResourceValues(face)[0], False)
            case 1:
                self.gainSun(Data.getResourceValues(face)[1], False)
            case 2:
                self.gainMoon(Data.getResourceValues(face)[2], False)
            case 3:
                self.gainVP(Data.getResourceValues(face)[3])
            case 4:
                self.gainAncientShards(Data.getResourceValues(face)[4])
            case 5:
                self.gainLoyalty(Data.getResourceValues(face)[5])

    def gainCelestialDieEffects(self):
        gains = Data.getResourceValues(self.celestialResultBuffer)
        if Data.getIsOr(self.celestialResultBuffer):
            match self.celestialOrChoice:
                case 0:
                    self.gainGold(gains[0], False)
                case 1:
                    self.gainSun(gains[1], False)
                case 2:
                    self.gainMoon(gains[2], False)
                case 3:
                    self.gainVP(gains[3])
                case 4:
                    self.gainAncientShards(gains[4])
                case 5:
                    self.gainLoyalty(gains[5])
        else:
            self.gainGold(gains[0], False)
            self.gainSun(gains[1], False)
            self.gainMoon(gains[2], False)
            self.gainVP(gains[3])
            self.gainAncientShards(gains[4])
            self.gainLoyalty(gains[5])
        match self.celestialResultBuffer:
            case Data.DieFace.REDSHIELD:
                self.gainSun(2, False)
            case Data.DieFace.BLUESHIELD:
                self.gainMoon(2, False)
            case Data.DieFace.GREENSHIELD:
                self.gainVP(3)
            case Data.DieFace.YELLOWSHIELD:
                self.gainGold(3, False)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2)
            case Data.DieFace.SHIP:
                self.shipsToResolve += 1
            case Data.DieFace.MAZERED | Data.DieFace.MAZEBLUE:
                self.mazeMoves += 1

    def gainMinorBlessingEffect(self, cyclops):
        if self.dieChoice:
            face = self.getDie1Result()
        else:
            face = self.getDie2Result()
        gains = Data.getResourceValues(face)
        if Data.getIsOr(face):
            match self.orChoice1:
                case 0:
                    if cyclops and self.sentinel1Choice:
                        self.gainVP(gains[0])
                    else:
                        self.gainGold(gains[0], False)
                case 1:
                    self.gainSun(gains[1], False)
                case 2:
                    self.gainMoon(gains[2], False)
                case 3:
                    self.gainVP(gains[3])
                case 4:
                    self.gainAncientShards(gains[4])
                case 5:
                    self.gainLoyalty(gains[5])
        else:
            if cyclops and self.sentinel1Choice:
                self.gainVP(gains[0])
            else:
                self.gainGold(gains[0], False)
            self.gainSun(gains[1], False)
            self.gainMoon(gains[2], False)
            self.gainVP(gains[3])
            self.gainAncientShards(gains[4])
            self.gainLoyalty(gains[5])
        match face:
            case Data.DieFace.REDSHIELD:
                self.gainSun(2, False)
            case Data.DieFace.BLUESHIELD:
                self.gainMoon(2, False)
            case Data.DieFace.GREENSHIELD:
                self.gainVP(3)
            case Data.DieFace.YELLOWSHIELD:
                if cyclops and self.sentinel1Choice:
                    self.gainVP(3)
                else:
                    self.gainGold(3, False)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2)
            case Data.DieFace.SHIP:
                self.shipsToResolve += 1
            case Data.DieFace.MAZERED | Data.DieFace.MAZEBLUE:
                self.mazeMoves += 1

    def gainDiceEffects(self, minotaur, sentinel):
        self.gainDiceEffectsInternal(self.getDie1Result(), self.getDie2Result(), minotaur, sentinel)

    def gainMazeDiceEffects(self):
        self.gainDiceEffectsInternal(self.getMazeDie1Result(), self.getMazeDie2Result(), False, False)

    def gainDiceEffectsInternal(self, die1, die2, minotaur, sentinel):
        mult = 1
        if die1 == Data.DieFace.TIMES3 or die2 == Data.DieFace.TIMES3:
            mult = 3
        if minotaur:
            mult *= -1
        else:
            if die1 == Data.DieFace.SHIP:
                if mult == 3:
                    self.times3ShipsToResolve += 1
                else:
                    self.shipsToResolve += 1
            if die2 == Data.DieFace.SHIP:
                if mult == 3:
                    self.times3ShipsToResolve += 1
                else:
                    self.shipsToResolve += 1
        if die1 == Data.DieFace.MAZERED or die1 == Data.DieFace.MAZEBLUE:
            self.mazeMoves += mult  # note: minotaur and can't be used with goddess maze module so mult won't be negative
        if die2 == Data.DieFace.MAZERED or die2 == Data.DieFace.MAZEBLUE:
            self.mazeMoves += mult
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
                    self.gainGold(die1gains[0] * mult, minotaur)
                    gains1 = (die1gains[0], 0, 0, 0)
                case 1:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(die1gains[1] * mult * 2)
                    else:
                        self.gainSun(die1gains[1] * mult, minotaur)
                    gains1 = (0, die1gains[1], 0, 0)
                case 2:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(die1gains[2] * mult * 2)
                    else:
                        self.gainMoon(die1gains[2] * mult, minotaur)
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
            self.gainGold(die1gains[0] * mult, minotaur)
            if sentinel and self.sentinel1Choice:
                self.gainVP(die1gains[1] * mult * 2 + die1gains[2] * mult * 2)
            else:
                self.gainSun(die1gains[1] * mult, minotaur)
                self.gainMoon(die1gains[2] * mult, minotaur)
            self.gainVP(die1gains[3] * mult)
            self.gainAncientShards(die1gains[4] * mult)
            self.gainLoyalty(die1gains[5] * mult)
        if Data.getIsOr(die2):
            match self.orChoice2:
                case 0:
                    self.gainGold(die2gains[0] * mult, minotaur)
                    gains2 = (die2gains[0], 0, 0, 0)
                case 1:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(die2gains[1] * mult * 2)
                    else:
                        self.gainSun(die2gains[1] * mult, minotaur)
                    gains2 = (0, die2gains[1], 0, 0)
                case 2:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(die2gains[2] * mult * 2)
                    else:
                        self.gainMoon(die2gains[2] * mult, minotaur)
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
            self.gainGold(die2gains[0] * mult, minotaur)
            if sentinel and self.sentinel2Choice:
                self.gainVP(die2gains[1] * mult * 2 + die2gains[2] * mult * 2)
            else:
                self.gainSun(die2gains[1] * mult, minotaur)
                self.gainMoon(die2gains[2] * mult, minotaur)
            self.gainVP(die2gains[3] * mult)
            self.gainAncientShards(die2gains[4] * mult)
            self.gainLoyalty(die2gains[5] * mult)
        match die1:
            case Data.DieFace.REDSHIELD:
                if gains2[1] == 0:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainSun(2 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.BLUESHIELD:
                if gains2[2] == 0:
                    if sentinel and self.sentinel1Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainMoon(2 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.GREENSHIELD:
                if gains2[3] == 0:
                    self.gainVP(3 * mult)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.YELLOWSHIELD:
                if gains2[0] == 0:
                    self.gainGold(3 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2 * mult)
                if gains2[1] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2 * mult)
                if gains2[2] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2 * mult)
                if gains2[3] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2 * mult)
                if gains2[0] > 0:
                    self.gainVP(3 * mult)
        match die2:
            case Data.DieFace.REDSHIELD:
                if gains1[1] == 0:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainSun(2 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.BLUESHIELD:
                if gains1[2] == 0:
                    if sentinel and self.sentinel2Choice:
                        self.gainVP(4 * mult)
                    else:
                        self.gainMoon(2 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.GREENSHIELD:
                if gains1[3] == 0:
                    self.gainVP(3 * mult)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.YELLOWSHIELD:
                if gains1[0] == 0:
                    self.gainGold(3 * mult, minotaur)
                else:
                    self.gainVP(5 * mult)
            case Data.DieFace.REDCHAOS:
                self.gainAncientShards(2 * mult)
                if gains1[1] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.BLUECHAOS:
                self.gainAncientShards(2 * mult)
                if gains1[2] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.GREENCHAOS:
                self.gainLoyalty(2 * mult)
                if gains1[3] > 0:
                    self.gainVP(3 * mult)
            case Data.DieFace.YELLOWCHAOS:
                self.gainLoyalty(2 * mult)
                if gains1[0] > 0:
                    self.gainVP(3 * mult)

    def buyFace(self, face):
        self.gainGold(-Data.faceCosts[face], False)
        self.unforgedFaces.append(face)

    def buyFaceShip(self, face, bonusGold):
        self.gainGold(-(Data.faceCosts[face] - bonusGold), False)
        self.unforgedFaces.append(face)

    def forgeFace(self, forgeInfo):
        if forgeInfo[0]:
            die = self.die1
        else:
            die = self.die2
        die.faces.remove(forgeInfo[2])
        die.faces.append(forgeInfo[1])
        die.upFace = 5
        self.unforgedFaces.remove(forgeInfo[1])
        self.numForged += 1

    def upgradeFace(self, die1, oldFace, newFace):
        if die1:
            die = self.die1
        else:
            die = self.die2
        die.faces.remove(oldFace)
        die.faces.append(newFace)
        die.upFace = 5
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

    def advanceCompanions(self):
        i = 0
        while i < len(self.companions):
            if self.companions[i] < 5:
                self.companions[i] = self.companions[i] + 1
            i += 1
        while "COMPANION_INST_REINF" in self.unusedReinfEffects:
            self.unusedReinfEffects.remove("COMPANION_INST_REINF")

    def hasFeat(self, feat):
        for myFeat in self.feats:
            if myFeat == feat:
                return True
        return False

    def performFeat(self, feat):
        self.gainSun(-Data.getSunCost(feat), False)
        self.gainMoon(-Data.getMoonCost(feat), False)
        self.feats.append(feat)
        self.gainVP(Data.getPoints(feat))

    def performFreeFeat(self, feat):
        self.feats.append(feat)
        self.gainVP(Data.getPoints(feat))

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

    def getMazeDieOptions(self, die1):
        # True for die 1, False for die 2
        if die1:
            face = self.getMazeDie1Result()
        else:
            face = self.getMazeDie2Result()
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

    def getCelestialDieOptions(self):
        resources = Data.getResourceValues(self.celestialResultBuffer)
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

    def canUseCyclops(self):
        if self.dieChoice:
            die = self.getDie1Result()
            orChoice = self.orChoice1
        else:
            die = self.getDie2Result()
            orChoice = self.orChoice2
        resources = Data.getResourceValues(die)
        if Data.getIsOr(die):
            if orChoice == 0 and resources[0] > 0:
                return True
            return False
        return resources[0] > 0 or die == Data.DieFace.YELLOWSHIELD

    def hasReinfEffects(self):
        for feat in self.feats:
            if "REINF" in Data.getEffect(feat):
                return True
        return False

    def populateReinfEffects(self):
        for feat in self.feats:
            effect = Data.getEffect(feat)
            if "REINF" in effect:
                if feat == Data.HeroicFeat.THE_MERCHANT and effect in self.unusedReinfEffects:
                    continue  # only resolve merchant once
                self.unusedReinfEffects.append(effect)

    def getMerchantCount(self):
        ret = 0
        for feat in self.feats:
            if feat == Data.HeroicFeat.THE_MERCHANT:
                ret += 1
        return ret

    def getReinfOptions(self):
        ret = []
        for effect in self.unusedReinfEffects:
            ret.append((Move.CHOOSE_REINF_EFFECT, self.playerID, (effect,)))
        ret = set(ret)  # remove duplicates
        return tuple(ret)

    def printPlayerInfo(self):
        print(f"Player {self.playerID}:\nGold: {self.gold}/{self.maxGold}\nSun: {self.sun}/{self.maxSun}")
        print(f"Moon: {self.moon}/{self.maxMoon}\nVictory Points: {self.vp}")
        print(f"Ancient Shards: {self.ancientShards}/6")
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
        print(f"Maze location: {self.mazePosition}")
        print(f"Hammer: {self.hammerTrack} / {self.getMaxHammer()}")
        for companion in self.companions:
            print(f"Companion: {companion}")
        for scepter in self.scepters:
            print(f"Scepter: {scepter}")
        print(f"Number of faces forged: {self.numForged}")
        print("Unforged Faces:")
        for face in self.unforgedFaces:
            print(face)
        print(f"Scepter gold: {self.getScepterGold()}")


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


def createLightDie(module):
    if module == 2:
        return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1,
                   Data.DieFace.ANCIENTSHARD1)
    return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1,
               Data.DieFace.SUN1)


def createDarkDie(module):
    if module == 1:
        return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.VP2,
                   Data.DieFace.MAZEBLUE)
    if module == 2:
        return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1,
                   Data.DieFace.VP1LOYALTY1,
                   Data.DieFace.MOON1)
    return Die(Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.GOLD1, Data.DieFace.VP2,
               Data.DieFace.MOON1)
