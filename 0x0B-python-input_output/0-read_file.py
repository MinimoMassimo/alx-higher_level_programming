#!/usr/bin/python3
"""module 0
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
