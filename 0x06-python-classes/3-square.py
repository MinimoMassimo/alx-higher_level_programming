#!/usr/bin/python3
'''
Module 3-square
Defines class Square with private attribute size and public instance method area
'''


class Square:
    '''
    class Square definition

    Args:
        size (int): size of a side
    '''
    def __init__(self, size=0):
        '''
        Initializes square

        Attributes:
            size: has to be int
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        Calculates and returns the area of the square

        Attributes:
            self: its attribut __size
        '''
        area = self.__size ** 2
        return area
