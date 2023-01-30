#!/usr/bin/python3
"""
    add_integer:
        checks if params are integers
        returns sum of parameters
"""


def add_integer(a, b=98):
    """
    Checks if int, otherwise return sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
