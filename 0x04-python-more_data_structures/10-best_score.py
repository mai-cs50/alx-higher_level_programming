#!/usr/bin/python3
def best_score(a_dictionary):
    maxv = 0
    maxk = None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxv = v
            maxk = k
    return maxk
