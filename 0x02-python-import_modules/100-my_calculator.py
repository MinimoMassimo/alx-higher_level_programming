#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    import sys

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if op == '+':
        ans = add(a, b)
    elif op == '-':
        ans = sub(a, b)
    elif op == '*':
        ans = mul(a, b)
    elif op == '/':
        ans = div(a, b)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], ans))
