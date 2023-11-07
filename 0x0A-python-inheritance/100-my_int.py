#!/usr/bin/python3
'''
class MyInt that inherits from int
'''


class MyInt(int):
    '''rebel version of unteger'''
    def __new__(cls, *args, **kwargs):
        '''instant of class'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''MyInt has == and != operators inverted'''
        return int(self) != other

    def __ne__(self, other):
        '''MyInt has == and != operators inverted'''
        return int(self) == other
