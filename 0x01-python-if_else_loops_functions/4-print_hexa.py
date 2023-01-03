#!/usr/bin/python3
for i in range(99):
    remainder = i % 16
    if remainder == 10:
        remainder = 'a'
    elif remainder == 11:
        remainder = 'b'
    elif remainder == 12:
        remainder = 'c'
    elif remainder == 13:
        remainder = 'd'
    elif remainder == 14:
        remainder = 'e'
    elif remainder == 15:
        remainder = 'f'
    x = i / 16
    print(f"{i} = 0x{int(x)}{remainder}")
