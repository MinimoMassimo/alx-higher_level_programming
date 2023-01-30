#!/usr/bin/python3
"""Module 1 - Rectangle
defines a rectangle with private attribute width and height
"""


class Rectangle:
    """Rectangle definition
        Args:
            width: width of rectangle (int)
            height: height of rectangle (int)
        Functions:
            __init__(self, width=0, height=0)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initializes the attributes width and height
            Attributes:
                width : has to be positive int
                height : has to be positive int
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter of width attribute
        """
        return self.__width

    @property
    def height(self):
        """getter of height attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """setter of width attribute

            Args:
                value : has to be positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height attribute

            Args:
                value : has to be positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
