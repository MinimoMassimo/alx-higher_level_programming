#!/usr/bin/python3
"""module 11
"""


class Student:
    """defines a student
        Attributes:
            first_name
            last_name
            age
        Functions:
            to_json(self, attrs=None)
            __init__(self, first_name, last_name, age)
            reload_From_json(self, json)
    """
    def __init__(self, first_name, last_name, age):
        """initializes
            Arguments:
                first_name
                last_name
                age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of a Student
            Arguments:
                attrs : default None; if it is a list of strings then only
                    the attributes listed must be returned.
                    Otherwise, all should be returned
        """
        if isinstance(attrs, list):
            a_dict = {}
            for x in attrs:
                if not isinstance(x, str):
                    return self.__dict__
                if x in self.__dict__.keys():
                    a_dict[x] = self.__dict__[x]
            return a_dict
        return self.__dict_

    def reload_from_json(self, json):
        """replaces all attributes of this instance
            Arguments:
                json : always a dictionary with key = public attribute name
                    and value = val of the public attribute
        """
        for x in json.keys():
            self.__dict__[x] = json[x]
