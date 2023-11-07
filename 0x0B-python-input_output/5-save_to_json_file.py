#!/usr/bin/python3
''' function that returns the JSON representation of an object (string):'''

import json


def save_to_json_file(my_obj, filename):
    '''returns the JSON representation of an object'''
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
