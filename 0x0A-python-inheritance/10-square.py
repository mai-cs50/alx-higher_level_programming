#!/usr/bin/python3
'''module of rectangle class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square subclass'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
