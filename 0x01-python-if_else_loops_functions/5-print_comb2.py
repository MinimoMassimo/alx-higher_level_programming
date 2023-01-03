#!/usr/bin/python3
for x in range(100):
    if x == 100:
        print(x)
        break
    print("{:02d}".format(x), end=', ')
