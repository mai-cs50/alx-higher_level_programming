#!/use/bin/python3
'''module for adds 2 integers'''

def add_integer(a, b=98):
    if type(a) not in (float, int):
        raise TypeError ('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError ('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
