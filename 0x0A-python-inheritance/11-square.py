#!/usr/bin/python3
"""module 11
    class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle and defines a square
        Functions:
            __init__(self, size)
            area(self)
            __str__(self)
    """
    def __init__(self, size):
        """initializes
            Arguments:
                size: private, positive integer validated by integer_validator
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area
        """
        return self.__size ** 2

    def __str__(self):
        """makes class printable
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
