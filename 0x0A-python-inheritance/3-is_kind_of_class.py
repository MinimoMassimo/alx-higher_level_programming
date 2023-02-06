#!/usr/bin/python3
"""module 3
    function again
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instace of, or if obj is an instance of
        a calss that inherited from a_class
        Returns True if yes, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
