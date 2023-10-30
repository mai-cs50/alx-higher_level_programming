#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""
class Rectangle:
    """width, hight"""
    def __init__(self, width=0, height=0):
        """intialise rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter with the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter with the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        '''getter with the private instance'''
        return self.__hight

    @height.setter
    def height(self, value):
        """setter with the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
