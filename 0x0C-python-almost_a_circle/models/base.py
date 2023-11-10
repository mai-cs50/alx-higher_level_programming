#!/usr/bin/python3
'''module for base class'''


class base:
    ''' manage id attribute in all your future classes'''


    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
