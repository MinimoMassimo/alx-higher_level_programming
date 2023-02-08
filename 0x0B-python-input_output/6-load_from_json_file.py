#!/usr/bin/python3
"""module 6
"""
import json


def load_from_json_file(filename):
    """creates an obj from a JSON file
        Arguments:
            filename: path of the JSON file
    """
    with open(filename, mode='r', encoding="utf-8") as a_file:
        return json.load(a_file)
