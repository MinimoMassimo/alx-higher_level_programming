#!/usr/bin/python3
"""module 12
"""


def pascal_triangle(n):
    """creates pascal's trinagle
        Returns a lsit of lists of integers
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    
    list_of_list = [[1], [1, 1]]
    for i in range(2, n):
        prev = list_of_list[i - 1]
        temp = [1]
        for j in range(0, len(prev) - 1):
            temp.append(prev[j] + prev[j + 1])
        temp.append(1)
        list_of_list.append(temp)
    return list_of_list
