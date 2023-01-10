#!/usr/bin/python3
"""
Module minoperations
"""


def minOperations(n: int) -> int:
    """
     Returns the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    prev: int
    written: int = 1
    left: int = n - 1
    minop: int = 0

    while left > 0:
        # Copy and poste operation
        if left % written == 0:
            minop += 2
            prev = written
            written *= 2
        # Paste operation only
        else:
            minop += 1
            written += prev
        left = n - written
    return minop
