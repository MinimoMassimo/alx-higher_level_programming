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
            area(self)
            update(self, *args, **kwargs)
            display(self)
            __str__(self)
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
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(' '*self.__x, end='')
            print('#'*self.__width)

    def __str__(self):
        '''this is what it prints if print(Rectange) is called
        '''
        i = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, width, height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute
        '''
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = args[0]
                elif k == 1:
                    self.__width = args[1]
                elif k == 2:
                    self.__height = args[2]
                elif k == 3:
                    self.__x = args[3]
                elif k == 4:
                    self.__y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        i = self.id
        width = self.__width
        height = self.__height
        dct = {"id": i, "width": width, "height": height}
        dct["x"] = self.__x
        dct["y"] = self.__y
        return dct
