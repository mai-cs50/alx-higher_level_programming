#!/usr/bin/python3
'''module of square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constuctor'''
        super().__init__(size, size, x, y, id)

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
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''method that assigns attributes'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update via no key-word'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''return dictionary represintation'''
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
