#!/usr/bin/python3
"""
Module for finding the perimiter of island
"""


def island_perimeter(grid):
    """
    Returns the Perimeter of the island
    """
    perimeter = 0
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            if grid[row][col]:
                if grid[row - 1][col] == 0:
                    perimeter += 2
                if grid[row][col - 1] == 0:
                    perimeter += 2

    return perimeter
