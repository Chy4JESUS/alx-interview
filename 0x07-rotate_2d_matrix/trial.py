"""Rotate a 2D matrix 90 degrees clockwise"""
import sys


def rotate_2d_matrix(matrix):
    """This function transposed and reversed the matrix"""
    if not type(matrix) is list:
        sys.exit(1)

    n = len(matrix)
    if not n >= 2:
        sys.exit(1)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[j][i]

    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = 2
result = rotate_2d_matrix(matrix)

print(result)
