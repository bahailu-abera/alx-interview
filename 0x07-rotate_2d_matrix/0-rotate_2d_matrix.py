#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate @matrix 90 degree in place
    """
    row = len(matrix)
    col = len(matrix[0])

    tmp = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            c = row - 1
            c = (c * i + c) % row
            tmp[j][c] = matrix[i][j]

    for i in range(row):
        for j in range(col):
            matrix[i][j] = tmp[i][j]
