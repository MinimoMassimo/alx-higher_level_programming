#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    uniq_set = set(my_list)
    return sum(uniq_set)
