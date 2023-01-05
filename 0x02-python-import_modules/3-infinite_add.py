#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    size = len(argv) - 1
    if size == 0:
        print(0)
    else:
        somma = 0
        for i in range(1, size + 1):
            somma += int(argv[i])
        print("{}".format(somma))
