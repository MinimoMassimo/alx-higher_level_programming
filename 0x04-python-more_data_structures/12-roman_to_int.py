#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    i, v, x, l, c, d, m = 0, 0, 0, 0, 0, 0, 0

    for idx in range(len(roman_string)):
        a = roman_string[idx]
        if idx != 0:
            prev = roman_string[idx - 1]

        if a == 'I':
            i += 1
        elif a == 'V':
            if idx != 0 and prev == 'I':
                i += 3
            else:
                v += 1
        elif a == 'X':
            if idx != 0 and prev == 'I':
                i += 3
                v += 1
            else:
                x += 1
        elif a == 'L':
            if idx != 0 and prev == 'X':
                x += 3
            else:
                l += 1
        elif a == 'C':
            if idx != 0 and prev == 'X':
                x += 3
                l += 1
            else:
                c += 1
        elif a == 'D':
            if idx != 0 and prev == 'C':
                c += 3
            else:
                d += 1
        elif a == 'M':
            if idx != 0 and prev == 'C':
                c += 3
                d += 1
            else:
                m += 1

    result = m*1000 + d*500 + c*100 + l*50 + x*10 + v*5 + i
    return result
