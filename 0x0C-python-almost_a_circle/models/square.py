#!/usr/bin/python3
'''module 10
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''defines a rectangle
        Functions:
            __init__(self, size, x=0, y=0, id=None)
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''initializes
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        i = self.id
        x = self.__x
        y = self.__y
        height = self.__height
        return "[Square] ({}) {}/{} - {}".format(i, x, y, height)

    @property
    def size(self):
        '''getter
        '''
        return self.height

    @size.setter
    def size(self, val):
        '''setter
        '''
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        '''updates values using parent method
        '''
        if args:
            dct = {}
            i = 0
            for arg in args:
                if i == 0:
                    dct["id"] = arg
                if i == 1:
                    dct["height"] = arg
                    dct["weight"] = arg
                if i == 2:
                    dct["x"] = arg
                if i == 3:
                    dct["y"] = arg
                i += 1
            Rectangle.update(self, **dct)
        elif kwargs:
            if "size" in kwargs:
                self.height = kwargs["size"]
                self.width = kwargs["size"]
            Rectangle.update(self, **kwargs)

    def to_dictionary(self):
        dct = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dct
