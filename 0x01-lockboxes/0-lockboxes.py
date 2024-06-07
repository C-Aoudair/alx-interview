#!/usr/bin/python3
""" This module contains the functioin that solvse the lockboxes problem"""


def canUnlockAll(boxes):
    """ This function takes list of lists as boxes and return true
        if all boxes can be opened
    """
    openedBoxes = []
    boxesQueue = []
    boxesQueue.append(0)

    while len(boxesQueue) != 0:
        box = boxesQueue.pop(0)
        openedBoxes.append(box)

        for neighbour in boxes[box]:
            if neighbour not in boxesQueue and
            neighbour not in openedBoxes and
            neighbour < len(boxes):
                boxesQueue.append(neighbour)

    if len(openedBoxes) == len(boxes):
        return True
    return False
