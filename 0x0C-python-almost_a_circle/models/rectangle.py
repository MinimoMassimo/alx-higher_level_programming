#!/usr/bin/python3
'''module 2
'''
from models.base import Base


def Rectangle(Base):
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

    def width(self, val):
        '''setter
        '''
        self.__width = val
    def height(self, val):
        '''setter
        '''
        self.__height = val
    def x(self, val):
        '''setter
        '''
        self.__x = val
    def y(self, val):
        '''setter
        '''
        self.__y = val
