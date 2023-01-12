#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    somma = 0
    for a in my_list:
        weight += a[0]*a[1]
        somma += a[1]
    return weight/somma
