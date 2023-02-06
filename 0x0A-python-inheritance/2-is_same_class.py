#!/usr/bin/python3
"""module 2
    function time
"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of specified class
        Returns true or false accordingly
    """
    if type(obj) == a_class:
        return True

    return False
