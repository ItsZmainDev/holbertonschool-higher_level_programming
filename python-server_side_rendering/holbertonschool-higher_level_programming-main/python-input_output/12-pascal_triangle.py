#!/usr/bin/python3
"""Define a function that return a list of integer
    representing the pascal's triangle of a variable"""


def pascal_triangle(n):
    """Function to print a pascal's triangle"""

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
