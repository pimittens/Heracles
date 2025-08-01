import json
from types import SimpleNamespace

facesData = tuple(json.loads(open("Faces.json").read(), object_hook=SimpleNamespace))
featsData = tuple(json.loads(open("Feats.json").read(), object_hook=SimpleNamespace))


def getLevel(face):
    for f in facesData:
        if f.name == face.name:
            return f.level
    return 0


def getPool(face):
    from Game import DieFace
    level = getLevel(face)
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
    :return: a tuple containing the gold, sun, moon, and vp for the face
    """
    for f in facesData:
        if f.name == face.name:
            return f.gold, f.sun, f.moon, f.vp
    return 0, 0, 0, 0


def getIsOr(face):
    for f in facesData:
        if f.name == face.name:
            return f.isOr
    return False


def isBoarFace(face):
    from Game import DieFace
    return face == DieFace.REDBOAR or face == DieFace.BLUEBOAR or face == DieFace.YELLOWBOAR or face == DieFace.GREENBOAR


def isBoarFeat(feat):
    from Game import HeroicFeat
    return feat == HeroicFeat.TENACIOUS_BOAR or feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN


def getPosition(feat):
    for f in featsData:
        if f.name == feat.name:
            return f.position
    from Game import HeroicFeat
    if feat == HeroicFeat.TENACIOUS_BOAR_RED or feat == HeroicFeat.TENACIOUS_BOAR_BLUE or feat == HeroicFeat.TENACIOUS_BOAR_YELLOW or feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        return 11
    return -1


def getFeatsByPosition(pos):
    from Game import HeroicFeat
    ret = []
    for f in featsData:
        if f.position == pos:
            ret.append(HeroicFeat[f.name])
    return ret


def getSet(feat):
    for f in featsData:
        if f.name == feat.name:
            return f.set
    return 0


def getPoints(feat):
    for f in featsData:
        if f.name == feat.name:
            return f.points
    return 0


def getEffect(feat):
    from Game import HeroicFeat
    if feat == HeroicFeat.TENACIOUS_BOAR_RED:
        return "BOAR_INST_AUTO_RED"
    elif feat == HeroicFeat.TENACIOUS_BOAR_BLUE:
        return "BOAR_INST_AUTO_BLUE"
    elif feat == HeroicFeat.TENACIOUS_BOAR_YELLOW:
        return "BOAR_INST_AUTO_YELLOW"
    elif feat == HeroicFeat.TENACIOUS_BOAR_GREEN:
        return "BOAR_INST_AUTO_GREEN"
    for f in featsData:
        if f.name == feat.name:
            return f.effect
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
    if pos > 5 and pos < 9:
        return 4
    return (pos + 1) // 2
