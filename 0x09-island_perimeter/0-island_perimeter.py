#!/usr/bin/python3
"""
Module for finding the perimiter of island
"""


def island_perimeter(grid):
    """
    Returns the Perimeter of the island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 2
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 2

    return perimeter
