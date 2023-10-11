#!/usr/bin/python3

"""
    Generate the pascal triangle of a nth term
    n = 0, produces empty list,
    n = 1, produces [[1]].
"""


def pascal_triangle(n):
    """
    list of lists of numbers is generated to
    produce pascal triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)
            row.append(1)
            triangle.append(row)

    return triangle
