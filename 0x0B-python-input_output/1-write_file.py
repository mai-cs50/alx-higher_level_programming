#!/usr/bin/python3
'''Write a function that appends a string at the end of a text file'''


def append_write(filename="", text=""):
    '''read file name with UTF8'''
    with open(filename, "w", endcoding="UTF-8") as f:
        return f.write(text)
