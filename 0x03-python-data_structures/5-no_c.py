#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)

    while my_string.count('c') != 0:
        my_string.remove('c')
    while my_string.count('C') !=0:
        my_string.remove('C')

    return "".join(my_string)
