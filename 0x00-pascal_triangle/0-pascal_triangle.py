#!/usr/bin/python3

"""Module for Pascal's Triangle concept."""


def pascal_triangle(n):
    """Function declaration."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(num)
        triangle.append(row)

    return triangle
