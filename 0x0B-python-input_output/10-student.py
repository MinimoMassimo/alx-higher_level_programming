#!/usr/bin/python3
"""module 10
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
                if x in self.__dict__:
                    a_dict[x] = self.__dict__[x]
            return a_dict
        return self.__dict__
