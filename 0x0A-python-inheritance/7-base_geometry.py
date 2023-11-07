#!/usr/bin/python3
''' class BaseGeometry (based on 6-base_geometry.py)'''


class BaseGeometry:
    '''method to compute this area'''
    def area(self):
        '''method to compute area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''method for validating value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
