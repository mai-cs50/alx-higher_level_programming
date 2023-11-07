#!/usr/bin/python3
''' function that returns the JSON representation of an object (string):'''

import json


def load_from_json_file(filename):
    '''returns the JSON representation of an object'''
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
