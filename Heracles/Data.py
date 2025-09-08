import json
from types import SimpleNamespace
from enum import Enum


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
    THE_MOON_GOLEM = 49
    THE_GREAT_GOLEM = 50
    THE_SUN_GOLEM = 51
    THE_TIME_GOLEM = 52
    THE_MEMORY = 53
    THE_ORACLE = 54
    THE_CHAOS = 55
    THE_DOGGED = 56
    THE_GUARDIAN = 57
    THE_MIRROR_OF_MISFORTUNE = 58
    MIRROR_OF_MISFORTUNE_RED = 59
    MIRROR_OF_MISFORTUNE_BLUE = 60
    MIRROR_OF_MISFORTUNE_YELLOW = 61
    MIRROR_OF_MISFORTUNE_GREEN = 62


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
    MAZERED = 30
    MAZEBLUE = 31
    ANCIENTSHARD1 = 32
    VP1LOYALTY1 = 33
    REDCHAOS = 34
    BLUECHAOS = 35
    YELLOWCHAOS = 36
    GREENCHAOS = 37
    REDMISFORTUNE = 38
    BLUEMISFORTUNE = 39
    YELLOWMISFORTUNE = 40
    GREENMISFORTUNE = 41
    GOLD3ANCIENTSHARD1 = 42
    VP1GOLD2LOYALTY1 = 43
    BOAR = 44
    CELESTIAL12GOLD = 45
    CELESTIAL5VP = 46
    CELESTIAL3VPAND3GOLD1SUN1MOONOR = 47
    CELESTIALMIRROR = 48
    CELESTIALGODDESS = 49
    CELESTIALUPGRADE = 50


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


def isMisfortuneFace(face):
    return face == DieFace.REDMISFORTUNE or face == DieFace.BLUEMISFORTUNE or face == DieFace.YELLOWMISFORTUNE or face == DieFace.GREENMISFORTUNE


def isMisfortuneFeat(feat):
    return feat == HeroicFeat.THE_MIRROR_OF_MISFORTUNE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_RED or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_BLUE or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_YELLOW or feat == HeroicFeat.MIRROR_OF_MISFORTUNE_GREEN


def getPosition(feat):
    for f in featsData:
        if f["name"] == feat.name:
            return f["position"]
    if feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        return 11
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
    for f in featsData:
        if f["name"] == feat.name:
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
