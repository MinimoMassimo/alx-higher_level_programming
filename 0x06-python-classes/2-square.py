#!/usr/bin/python3
'''
Module 2-square
Defines class Square with private attribute size
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
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
