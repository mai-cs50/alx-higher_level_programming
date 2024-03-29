#!/usr/bin/python3
"""   """

def find_peak(list_of_integers):
    """ """

    list_ = list_of_integers
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = (end + start) // 2
        if list_[mid] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
