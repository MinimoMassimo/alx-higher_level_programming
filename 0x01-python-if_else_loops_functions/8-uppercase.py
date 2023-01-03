#!/usr/bin/python3
def uppercase(str):
    for c in str:
        uni = ord(c)
        if uni < 97 or uni > 122:
            x = c
        else:
            x = chr(uni - 32)
        print("{}".format(x), end='')
    print()
