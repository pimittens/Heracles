import json
from types import SimpleNamespace

facesData = tuple(json.loads(open("Faces.json").read(), object_hook=SimpleNamespace))
featsData = tuple(json.loads(open("Feats.json").read(), object_hook=SimpleNamespace))

def getLevel(face):
    for f in facesData:
        if f.name == face.name:
            return f.level
    return 0

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
            return (f.gold, f.sun, f.moon, f.vp)
    return (0,0,0,0)

def getIsOr(face):
    for f in facesData:
        if f.name == face.name:
            return f.isOr
    return False

def getPosition(feat):
    for f in featsData:
        if f.name == feat.name:
            return f.isOr
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
    for f in featsData:
        if f.name == feat.name:
            return f.effect
    return "NONE"