#!/usr/bin/python3

"""
0-pascal_triangle
"""


def find(n):
    """
     returns a list of lists of integers representing
     the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    row = [1]
    triangle.append(row)
    for i in range(1, n):
        row = []
        row.append(triangle[i - 1][0])
        j = 0
        while j < len(triangle[i - 1]) - 1:
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            j += 1
        row.append(triangle[i - 1][j])
        triangle.append(row)

    return triangle
