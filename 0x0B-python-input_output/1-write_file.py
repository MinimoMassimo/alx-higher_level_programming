#!/usr/bin/python3
"""module 1
"""


def write_file(filename="", text=""):
    """writes a string to a text file
        returns num of chars written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    return (len(text))
