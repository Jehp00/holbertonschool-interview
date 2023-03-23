#!/usr/bin/python3
"""Module intervie practice"""


def canUnlockAll(boxes):
    if not boxes or (not isinstance(boxes, list)):
        return False

    keyList = []
    # hasMoreKeys = False
    countBoxes = len(boxes)
    boxesUnlock = setBoxesUnlock(countBoxes)
    for i in range(countBoxes):
        if isinstance(boxes[i], list):
            if i == 0:
                keyList.append(0)
                setKeys(boxes[i], keyList, boxesUnlock)
            if boxesUnlock[i] == 0 and keyList.count(i) > 0:
                keyList = unLockBox(keyList, boxesUnlock, boxes)
        else:
            return False
    if boxesUnlock.count(0) == 0:
        return True
    return False


def unLockBox(keys, boxesUnlock, boxes):
    keys_copy = []
    if len(keys) > 0:
        if keys[0] < len(boxesUnlock):
            boxesUnlock[keys[0]] = 1
            if not boxes[keys[0]] or type(boxes[keys[0]] == list):
                setKeys(boxes[keys[0]], keys, boxesUnlock)
            keys.pop(0)
            unLockBox(keys, boxesUnlock, boxes)
    return keys


def setBoxesUnlock(count):
    boxes = []
    for i in range(count):
        boxes.append(0)
    return boxes


def setKeys(box, keyList, boxesUnlock):
    if box:
        for key in box:
            if isInteger(key):
                if key < len(boxesUnlock) and keyList.count(
                        key) == 0 and boxesUnlock[key] == 0:
                    keyList.append(key)


def isInteger(str):
    is_int = True
    try:
        int(str)
    except ValueError:
        is_int = False
    return is_int