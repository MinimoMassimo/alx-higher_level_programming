#!/usr/bin/python3
"""module 8
"""


def class_to_json(obj):
    """returns dictionary description with simple data structure
        for JSON serialization of an object
    """
    return obj.__dict__
