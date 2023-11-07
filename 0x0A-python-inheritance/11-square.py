#!/usr/bin/python3
'''module of rectangle class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square subclass'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''method area of square'''
        return self.__size ** 2

    def __str__(self):
        '''return string'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
