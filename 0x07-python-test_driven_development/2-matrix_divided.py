#!/usr/bin/python3
"""
    Module of matrix_divided - A function
    that devides all elements of a matric
"""


def matrix_divided(matrix, div):
    """A fuction that divides all elements of a matrix_divided

    Args:
        matrix: matrix to be manipulated
        dix: matrix element divider

    Returns:

    Raises:
        TypeError: if element of matrix is not an integer or a float
        ZeroDivisionError: if div == 0
    """
    # Raise TypeError if matrix is not a list of lists of integer or floats
    if (not isinstance(matrix, list)
        or not all([isinstance(row, list) for row in matrix])
        or not all([(isinstance(elem, int) or isinstance(elem, float))
                    for row in matrix for elem in row])):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

        # Raise TypeError if each row of the matrix is not of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Raise TypeError if div is not integer or float
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    # Raise ZeroDivisionError if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all element of matrix by div, round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
