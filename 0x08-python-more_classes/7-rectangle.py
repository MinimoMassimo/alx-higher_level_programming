#!/usr/bin/python3
"""Module 7 - Rectangle
defines a rectangle with public class attribute print_symbol
"""


class Rectangle:
    """Rectangle definition
        Args:
            width: width of rectangle (int)
            height: height of rectangle (int)
            number_of_instances (int)
            print_symbol
        Functions:
            __init__(self, width=0, height=0)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
            area(self)
            perimeter(self)
            __str__
            __repr__
            __del__
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculates are of rectangle
            returns the area
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """calculates the perimeter of rectangle
            returns the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """print() __str__ method returns rectangle in '#' format
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        res = ""
        for i in range(self.__height - 1):
            res += str(self.print_symbol) * self.__width + '\n'
        res += str(self.print_symbol) * self.__width
        return res

    def __repr__(self):
        """returns a string representation of this rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when deleting an instance of Rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
