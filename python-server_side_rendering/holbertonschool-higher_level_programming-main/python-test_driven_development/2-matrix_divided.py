#!/usr/bin/python3
"""
Module that define the function matrix_divided
which divides all elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: a list of lists of integers or floats.
        div: a number (int or float) to devide the matrix elements.

    Returns:
        A new matrix with the result of the division, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list if lists if integers/floats
        or if div is not a number
        or if the rows of the matrix are not the same size
    ZeroDivisionError: If div is 0
    """

    # Check if matrix is a list of lists of ints/floats
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(num, (int, float)) for row in matrix for num in row
            )):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows are the same size
    row_lenght = len(matrix[0])
    if any(len(row) != row_lenght for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check the div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with divided and rounded value
    return [[round(num / div, 2) for num in row] for row in matrix]
