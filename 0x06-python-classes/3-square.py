#!/usr/bin/python3
'''
defines a square by: (based on 2-square.py)
'''


class Square:
    '''
    init
    '''
    def __init__(self, int):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        return self.__size ** 2
