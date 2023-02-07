#!/usr/bin/python3
"""module 4
"""
import json


def from_json_string(my_str):
    """returns python obj represented by JSON string
    """
    return json.loads(my_str)
