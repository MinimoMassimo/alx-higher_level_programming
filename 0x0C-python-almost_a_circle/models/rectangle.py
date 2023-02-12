#!/usr/bin/python3
'''module 2
'''
from models.base import Base


class Rectangle(Base):
    '''defines a rectangle and inherits from Base
        Attributes:
            __width
            __height
            __x
            __y
        Functions:
            __init__(self, width, height, x=0, y=0, id=None)
            getters and setters for all attributes
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes
        '''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter
        '''
        return self.__width
    @property
    def height(self):
        '''getter
        '''
        return self.__height
    @property
    def x(self):
        '''getter
        '''
        return self.__x
    @property
    def y(self):
        '''getter
        '''
        return self.__y

    @width.setter
    def width(self, val):
        '''setter
        '''
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val
    @height.setter
    def height(self, val):
        '''setter
        '''
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val
    @x.setter
    def x(self, val):
        '''setter
        '''
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val
    @y.setter
    def y(self, val):
        '''setter
        '''
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        '''returns area
        '''
        return self.__height * self.__width

    def display(self):
        '''prints in stdout theRectablge instance with '#'
        '''
        for i in range(self.__height):
            print('#'*self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
