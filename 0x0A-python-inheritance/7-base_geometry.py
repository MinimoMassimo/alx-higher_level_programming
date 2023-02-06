#!/usr/bin/python3
"""module 7
    class based on module 6
"""


class BaseGeometry:
    """class
        Functions:
            area(self)
            integer_validator(self, name, value)
    """
    def area(self):
        """raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
            Arguments:
                name - assumed it is always a string
                value - only int is allowed, > 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
