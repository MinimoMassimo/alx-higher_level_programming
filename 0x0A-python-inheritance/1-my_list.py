#!/usr/bin/python3
"""module 1
    a class that inherits from list with method 'print_sorted'
"""


class MyList(list):
    """inherits from list
        Functions:
            print_sorted
    """
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
