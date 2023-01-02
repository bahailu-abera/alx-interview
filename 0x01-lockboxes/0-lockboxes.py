#!/usr/bin/python3
"""
Module for solving lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes are unlocked.
    """
    keys = [0]

    for key in keys:
        for ele in boxes[key]:
            if ele not in keys and ele < len(boxes):
                keys.append(ele)
    return len(keys) == len(boxes)
