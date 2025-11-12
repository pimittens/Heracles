import json
from enum import Enum


class HeroicFeat(Enum):
    THE_BLACKSMITHS_HAMMER = 0
    THE_BLACKSMITHS_CHEST = 1
    THE_SILVER_HIND = 2
    GREAT_BEAR = 3
    SATYRS = 4
    TENACIOUS_BOAR = 5
    TENACIOUS_BOAR_RED = 6
    TENACIOUS_BOAR_BLUE = 7
    TENACIOUS_BOAR_GREEN = 8
    TENACIOUS_BOAR_YELLOW = 9
    FERRYMAN = 10
    CERBERUS = 11
    HELMET_OF_INVISIBILITY = 12
    CANCER = 13
    SENTINEL = 14
    HYDRA = 15
    TYPHON = 16
    SPHINX = 17
    CYCLOPS = 18
    MIRROR_OF_THE_ABYSS = 19
    GORGON = 20
    TRITON = 21
    MINOTAUR = 22
    THE_GUARDIANS_SHIELD = 23
    THE_GUARDIANS_OWL = 24
    CELESTIAL_SHIP = 25
    WILD_SPIRITS = 26
    THE_ELDER = 27
    THE_TREE = 28
    THE_MERCHANT = 29
    THE_WOOD_NYMPH = 30
    THE_LIGHT = 31
    THE_OMNISCIENT = 32
    THE_GOLDSMITH = 33
    THE_ABYSSAL_TRIDENT = 34
    THE_LEFT_HAND = 35
    THE_ETERNAL_FIRE = 36
    THE_FIRST_TITAN = 37
    THE_GODDESS = 38
    THE_RIGHT_HAND = 39
    THE_ETERNAL_NIGHT = 40
    THE_MISTS = 41
    THE_ANCESTOR = 42
    THE_WIND = 43
    THE_CELESTIAL_DIE = 44
    THE_COMPANION = 45
    THE_BLACKSMITHS_SCEPTER = 46
    THE_TWINS = 47
    THE_MOON_GOLEM = 48
    THE_GREAT_GOLEM = 49
    THE_SUN_GOLEM = 50
    THE_TIME_GOLEM = 51
    THE_MEMORY = 52
    THE_ORACLE = 53
    THE_CHAOS = 54
    THE_DOGGED = 55
    THE_GUARDIAN = 56
    THE_MIRROR_OF_MISFORTUNE = 57
    MIRROR_OF_MISFORTUNE_RED = 58
    MIRROR_OF_MISFORTUNE_BLUE = 59
    MIRROR_OF_MISFORTUNE_YELLOW = 60
    MIRROR_OF_MISFORTUNE_GREEN = 61


class DieFace(Enum):
    GOLD1 = 0
    SUN1 = 1
    MOON1 = 2
    VP2 = 3
    GOLD3 = 4
    GOLD4 = 5
    GOLD6 = 6
    GOLD2MOON1 = 7
    VP1SUN1 = 8
    GOLD1SUN1MOON1OR = 9
    GOLD3VP2OR = 10
    MOON2 = 11
    SUN2 = 12
    VP3 = 13
    VP4 = 14
    GOLD1SUN1MOON1VP1 = 15
    MOON2VP2 = 16
    GOLD2SUN2MOON2OR = 17
    MIRROR = 18
    REDSHIELD = 19
    YELLOWSHIELD = 20
    GREENSHIELD = 21
    BLUESHIELD = 22
    REDBOAR = 23
    YELLOWBOAR = 24
    GREENBOAR = 25
    BLUEBOAR = 26
    TIMES3 = 27
    SHIP = 28
    MAZERED = 29
    MAZEBLUE = 30
    ANCIENTSHARD1 = 31
    VP1LOYALTY1 = 32
    REDCHAOS = 33
    BLUECHAOS = 34
    YELLOWCHAOS = 35
    GREENCHAOS = 36
    REDMISFORTUNE = 37
    BLUEMISFORTUNE = 38
    YELLOWMISFORTUNE = 39
    GREENMISFORTUNE = 40
    GOLD3ANCIENTSHARD1 = 41
    VP1GOLD2LOYALTY1 = 42
    BOAR = 43

class CelestialDieFace(Enum):
    CELESTIAL12GOLD = 0
    CELESTIAL5VP = 1
    CELESTIAL3VPAND3GOLD1SUN1MOONOR = 2
    CELESTIALMIRROR = 3
    CELESTIALGODDESS = 4
    CELESTIALUPGRADE = 5


class Treasure(Enum):
    VP_TREASURE = 0
    SUN_TREASURE = 1
    MOON_TREASURE = 2


facesData = tuple(json.loads(open("Faces.json").read()))
featsData = tuple(json.loads(open("Feats.json").read()))
mazeData = tuple(json.loads(open("MazeSpaces.json").read()))


def getLevel(face):
    for f in facesData:
        if f["name"] == face.name:
            return f["level"]
    return 0


def getPool(face):
    level = getLevel(face)
    if level == 0:
        return -1
    if level == 1:
        if face == DieFace.GOLD3:
            return 0
        return 1
    if level == 2:
        if face == DieFace.GOLD4:
            return 2
        return 3
    if level < 6:
        return level + 1
    if level == 6:
        if face == DieFace.SUN2:
            return 7
        return 8
    return 9


def getGoldValue(face):
    level = getLevel(face)
    if level == 7:
        return 12
    if level == 6:
        return 8
    if level > 0:
        return level + 1
    return 0


def getResourceValues(face):
    """
    get the resources provided by a face

    :param face: the face
    :return: a tuple containing the gold, sun, moon, vp, ancient shards, and loyalty for the face
    """
    for f in facesData:
        if f["name"] == face.name:
            return f["gold"], f["sun"], f["moon"], f["vp"], f["ancientshard"], f["loyalty"]
    return 0, 0, 0, 0, 0, 0


def getIsOr(face):
    for f in facesData:
        if f["name"] == face.name:
            return f["isOr"]
    return False


def isBoarFace(face):
    return face == DieFace.REDBOAR or face == DieFace.BLUEBOAR or face == DieFace.YELLOWBOAR or face == DieFace.GREENBOAR


def isBoarFeat(feat):
    return feat == HeroicFeat.TENACIOUS_BOAR or feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN


def containsBoarFeat(feats):
    for feat in feats:
        if isBoarFeat(feat):
            return True
    return False


def isMisfortuneFace(face):
    return face == DieFace.REDMISFORTUNE or face == DieFace.BLUEMISFORTUNE or face == DieFace.YELLOWMISFORTUNE or face == DieFace.GREENMISFORTUNE


def isMisfortuneFeat(feat):
    return feat == HeroicFeat.THE_MIRROR_OF_MISFORTUNE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_RED or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN


def containsMisfortuneFeat(feats):
    for feat in feats:
        if isMisfortuneFeat(feat):
            return True
    return False


def getPosition(feat):
    for f in featsData:
        if f["name"] == feat.name:
            return f["position"]
    if feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        return 11
    if feat == HeroicFeat.MIRROR_OF_MISFORTUNE_RED or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN:
        return 5
    return -1


def getFeatsByPosition(pos):
    ret = []
    for f in featsData:
        if f["position"] == pos and f["set"] < 3:
            ret.append(HeroicFeat[f["name"]])
    return ret


def getSet(feat):
    for f in featsData:
        if f["name"] == feat.name:
            return f["set"]
    return 0


def getPoints(feat):
    fe = feat
    if feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        fe = HeroicFeat.TENACIOUS_BOAR
    if feat == HeroicFeat.MIRROR_OF_MISFORTUNE_RED or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN:
        fe = HeroicFeat.THE_MIRROR_OF_MISFORTUNE
    for f in featsData:
        if f["name"] == fe.name:
            return f["points"]
    return 0


def getEffect(feat):
    if feat == HeroicFeat.TENACIOUS_BOAR_RED:
        return "BOAR_INST_AUTO_RED"
    elif feat == HeroicFeat.TENACIOUS_BOAR_BLUE:
        return "BOAR_INST_AUTO_BLUE"
    elif feat == HeroicFeat.TENACIOUS_BOAR_YELLOW:
        return "BOAR_INST_AUTO_YELLOW"
    elif feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        return "BOAR_INST_AUTO_GREEN"
    if feat == HeroicFeat.MIRROR_OF_MISFORTUNE_RED:
        return "MISFORTUNE_INST_AUTO_RED"
    elif feat == HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE:
        return "MISFORTUNE_INST_AUTO_BLUE"
    elif feat == HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW:
        return "MISFORTUNE_INST_AUTO_YELLOW"
    elif feat == HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN:
        return "MISFORTUNE_INST_AUTO_GREEN"
    for f in featsData:
        if f["name"] == feat.name:
            return f["effect"]
    return "NONE"


def getSunCost(feat):
    pos = getPosition(feat)
    if pos <= 7:
        if pos == 7:
            return 5
        if pos == 0:
            return 1
        return pos
    return 0


def getMoonCost(feat):
    pos = getPosition(feat)
    if pos >= 7:
        if pos == 7:
            return 5
        if pos == 14:
            return 1
        return 14 - pos
    return 0


def getIsland(feat):
    pos = getPosition(feat)
    if pos <= 5:
        return (pos + 2) // 2
    if 5 < pos < 9:
        return 4
    return (pos + 1) // 2


def getResourceType(type):
    match type:
        case 0:
            return "gold"
        case 1:
            return "sun"
        case 2:
            return "moon"
        case 3:
            return "vp"
        case 4:
            return "ancient shards"
        case 5:
            return "loyalty"


faceCosts = {face: getGoldValue(face) for face in DieFace}


def getTotalGoldCost(faces):
    ret = 0
    for face in faces:
        ret += faceCosts[face]
    return ret


# maze stuff

def isIntersection(position):
    # return position == 0 or position == 1 or position == 3 or position == 5 or position == 15 or position == 18
    return len(mazeData[position]["next"]) > 1


def isReverseIntersection(position):
    # return position == 8 or position == 9 or position == 10 or position == 12
    return len(mazeData[position]["prev"]) > 1


def getMazeEffect(position):
    return mazeData[position]["effect"]


def getMazeOrEffects(position):
    match getMazeEffect(position):
        case "GOLD6VP3OR":
            return (6, 0, 0, 3)
        case "GOLD3SUN1MOON1OR":
            return (3, 1, 1, 0)
        case "MOON2VP3OR":
            return (0, 0, 2, 3)
        case "SUN2MOON2OR":
            return (0, 2, 2, 0)


def isTreasureHall(position):
    # return position == 7 or position == 12 or position == 20
    return mazeData[position]["effect"] == "TREASUREHALL"


def getMazeMoveOptions(position):
    return mazeData[position]["next"]


def getReverseMazeMoveOptions(position):
    return mazeData[position]["prev"]


# loyalty track stuff

def getAllegiancePoints(trackSpace):
    if trackSpace < 0:
        if trackSpace == -14:
            return -25
        return -getAllegiancePoints(-trackSpace)  # the points are symmetric except for the 14/-14 spaces
    if trackSpace < 4:
        return trackSpace
    if 3 < trackSpace < 8:
        return trackSpace + 1
    if 7 < trackSpace < 11:
        return 10 + 2 * (trackSpace - 8)
    if trackSpace == 11 or trackSpace == 12:
        return 17
    if trackSpace == 13 or trackSpace == 14:
        return 20
    return 25


def getEffectLevel(trackSpace):
    if -4 < trackSpace < 4:
        return 0
    if 3 < trackSpace < 7:
        return 1
    if 6 < trackSpace < 10:
        return 2
    if trackSpace > 9:
        return 3
    if -8 < trackSpace < -3:
        return -1
    return -2


def getNext(trackSpace):
    if trackSpace == 15:
        return 15
    return trackSpace + 1


def getPrev(trackSpace):
    if trackSpace == -15:
        return -15
    if trackSpace == 15 or trackSpace == 13 or trackSpace == -10 or trackSpace == -13:
        return trackSpace - 2
    return trackSpace - 1
