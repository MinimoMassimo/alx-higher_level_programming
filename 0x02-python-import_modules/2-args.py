#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    else:
        s = 's'
        if len(argv) == 2:
            s = ''
        print("{} argument{}:".format(len(argv) - 1, s))
        for x in range(1, len(argv)):
            print("{}: {}".format(x, argv[x]))
