#!/usr/bin/python3
"""
Module minoperations
"""


def minOperations(n):
    """
     Returns the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    prev = 1
    written = 1
    left = n - 1
    minop = 0

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
