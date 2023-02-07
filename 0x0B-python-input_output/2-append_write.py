#!/usr/bin/python3
"""module 2
"""


def append_write(filename="", text=""):
    """function appends string at end of file
        returns number of chars added
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        a_file.write(text)
        return len(text)
