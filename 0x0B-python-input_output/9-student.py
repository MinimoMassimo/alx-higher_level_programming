#!/usr/bin/python3
"""module 9
"""


class Student:
    """defines a student
        Attributes:
            first_name
            last_name
            age
        Functions:
            to_json(self)
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

    def to_json(self):
        """retrieves dictionary representation of a Student
        """
        return self.__dict__
