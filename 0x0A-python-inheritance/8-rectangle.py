#!/usr/bin/python3
'''class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''a subclass represinting a rectangle'''
    def __init__(self, width, height):
        '''constructors'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
