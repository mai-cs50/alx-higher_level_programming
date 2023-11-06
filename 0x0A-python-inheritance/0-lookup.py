#!/usr/bin/python3
"""function returns the list of available attributes, methods of an object"""

def lookup(obj):
    '''returns the list of available attributes,
    methods of an object'''
    return dir(obj)
