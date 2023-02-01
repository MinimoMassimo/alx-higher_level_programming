#!/usr/bin/python3
"""text_indentation prints text in specific format:
2 new lines are added after '.', '?', or ':'
"""


def text_indentation(text):
    """prints arg text with 2 \n after the chars '.', '?', and ':'
    checks if text is a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print('\n')
            while text[i + 1] == ' ':
                i += 1
        i += 1
