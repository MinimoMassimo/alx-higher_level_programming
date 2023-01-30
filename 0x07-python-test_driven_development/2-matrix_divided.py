#!/usr/bin/python3
"""matrix_divided divides the given matrix by param "div"
"""


def matrix_divided(matrix, div):
    """Divides all elements of param matrix by param div
    checks if entire list is int or float
    checks if each list in the matrix is of the same size
    checks if div is int or float or 0
    """
    mes = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(mes)
            else:
                temp.append(round(items / div, 2))
        result.append(temp)

    return result
