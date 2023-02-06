#!/usr/bin/python3
"""module 4
    another function
"""


def inherits_from(obj, a_class):
    """checks if obj is instance of class that inherited from a_class
        Return True if yes, False otherwise
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
