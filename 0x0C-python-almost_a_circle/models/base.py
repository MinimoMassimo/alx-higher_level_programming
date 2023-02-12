#!/usr/bin/python3
'''module 1
'''

class Base:
    '''this is the base of all other classes in this project.
    It manages 'id' in all future classes
    Attributes:
        __nb_objects: number of ids with values None instances
    Functions:
        __init__(self)
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        '''initializes id
            Arguments:
                id: int
        '''
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
