#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learn"
length, first = multiple_returns(sentence)
print("Length: {:d} - First cahr: {}".format(length, first))
