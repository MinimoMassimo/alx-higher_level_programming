#!/usr/bin/python3
import sys

if len(argv) != 2:
    print("Usage: nqueens N")
n = sys.argv[1]
if not isinstance(n, int):
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)

res = [[]]
temp = [[]]
for i in range(8):
    for j in range(8):
        if temp == [[]] or 
        temp.append([i, j])

