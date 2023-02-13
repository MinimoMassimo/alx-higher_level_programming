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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        return self.height * self.width

    def display(self):
        '''prints in stdout theRectablge instance with '#'
        '''
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(' '*self.x, end='')
            print('#'*self.width)

    def __str__(self):
        '''this is what it prints if print(Rectange) is called
        '''
        i = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, width, height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute
        '''
        if args:
            for k, v in enumerate(args):
                """if not isinstance(v, int):
                    raise TypeError("{} must be an integer".format(it))
                """
                if k == 0:
                    self.id = args[0]
                elif k == 1:
                    self.width = args[1]
                elif k == 2:
                    self.height = args[2]
                elif k == 3:
                    self.x = args[3]
                elif k == 4:
                    self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        i = self.id
        width = self.width
        height = self.height
        dct = {"id": i, "width": width, "height": height}
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
