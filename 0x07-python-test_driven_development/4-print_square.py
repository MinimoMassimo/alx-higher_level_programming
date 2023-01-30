#!/usr/bin/python3
"""print_square prints a square using '#'
"""


def print_square(size):
    """prints a square
    checks if size is an integer, float or negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
