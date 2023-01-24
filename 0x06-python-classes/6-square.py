#!/usr/bin/python3
'''
Module 6-square
Defines class Square with a printing method
'''


class Square:
    '''
    class Square definition

    Args:
        size (int): size of a side
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes square

        Attributes:
            size: has to be int
            position
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        '''
        Calculates and returns the area of the square

        Returns: area
        '''
        area = self.__size ** 2
        return area

    @property
    def size(self):
        '''
        Gets the value __size

        Return: size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the value __size

        Attributes:
            value: the new value to be
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        '''
        Prints the square in #s
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        '''
        Getter
        '''
        return self.__position
    @position.setter
    def position(self, value):
        '''
        Setter

        Attributes:
            value : the new value to be of position
        '''
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
