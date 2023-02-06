#!/usr/bin/python3
"""module 8
    this time a class that inherits from Base Geometry of module 7
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry
        Functions:
            __init__(self, width, height)
    """
    def __init__(self, width, height):
        """initializes
            Arguments:
                width: positive int
                height: positive int'
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height
