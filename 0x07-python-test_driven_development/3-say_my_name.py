#!/usr/bin/python3
"""say_my_name print the parameters, first_name + last_name
    last name id empty on default
"""


def say_my_name(first_name, last_name=""):
    """prints "My name is <first_name> <last_name>"
    checks if both are strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
