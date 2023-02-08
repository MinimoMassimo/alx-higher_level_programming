#!/usr/bin/python3
Square = __import__('11-square').Square

try:
    s = Square()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    s = Square([12, 52])
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    s = Square(-35)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    s = Square(0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    s = Square(5)
    print(s.size)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
