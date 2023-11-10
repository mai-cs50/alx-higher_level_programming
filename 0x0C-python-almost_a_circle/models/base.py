#!/usr/bin/python3
'''module for base class'''


class Base:
    ''' manage id attribute in all your future classes'''


    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
