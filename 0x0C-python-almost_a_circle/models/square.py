#!/usr/bin/python3
'''module of square class'''
from models.rectangle import Rectangle


class Square:
    '''Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constuctor'''
        super().__init__(self, size, x=0, y=0, id=None)

    def __str__(self):
        '''return str info about square'''
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''rectangle size'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = width
        self.height = height
