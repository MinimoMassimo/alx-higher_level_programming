#!/usr/bin/python3
"""module 9
    class that inherits from Base Geometry of module 7
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry
        Functions:
            __init__(self, width, height)
            area(self)
            __str__(self)
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

    def area(self):
        """calculates area
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
