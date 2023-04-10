#!/usr/bin/python3
'''module 1
'''
import json


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json string representation
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes JSON string representation of list_obj to file
        '''
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))
        f = cls.__name__ + ".json"
        with open(f, "w") as a_file:
            a_file.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        '''returns list of json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns instance with all attributes already set
        '''
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns list of instances
        '''
        filename = cls.__name__ + ".json"
        lst = []
        try:
            with open(filename, "r") as f:
                inst = cls.from_json_string(f.read())
            for i, dict in enumerate(inst):
                lst.append(cls.create(**inst[i]))
        except Exception:
            pass
        return lst

    @classmethod
    def save_to_file_cvs(cls, list_objs):
        """saves to cvs file
        """
        filename = cls.__name__ + ".json"
        objs = []
        if list_objs is not None:
            for i in list_objs:
                if i.__class__ == Rectangle:
                    w = i.width
                    h = i.height
                    objs.append("{},{},{},{},{}".format(i.id, w, h, i.x, i.y))
                if i.__class__ == Square:
                    objs.append("{},{},{},{}".format(i.id, i.size, i.x, i.y))
        with open(filename, "w") as f:
            f.write(objs)
    
    @classmethod
    def load_from_file_cvs(cls):
        """loads from cvs file
        """
        filename = cls.__name__ + ".json"
        lst = []
        try:
            with open(filename, "r") as f:
                inst = f.read()
            for i in inst:
                l = i.split(',')
                if cls.__name__ == "Square":
                    dummy = cls(l[1], l[2], l[3], l[0])
                if cls.__name__ == "Rectangle":
                    dummy = cls(l[1], l[2], l[3], l[4], l[0])
                lst.append(dummy)
        except Exception:
            pass
        return lst
