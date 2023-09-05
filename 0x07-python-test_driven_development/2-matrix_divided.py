#!/usr/bin/python3
"""module: function that divides all elements of a matrix.

    Atributes:
            matrix_divided: divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list):a list of lists of integers or floats
        div (int, float): the number well be divded

    raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Return:
        a new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(i, list) for i in matrix) or
            not all((isinstance(j, int) or isinstance(j, float))
                    for j in [num for i in matrix for num in i])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map (lambda x : round (x /div, 2), i))for i in matrix])
