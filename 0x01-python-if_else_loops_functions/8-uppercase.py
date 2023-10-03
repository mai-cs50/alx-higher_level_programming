#!/usr/bin/python3
#def islower(c):
    #if ord(c) >= ord('a') and ord(c) <= ord('z'):
        #return True
    #else:
        #return False


def uppercase(str):
    for c in str:
        c = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        print(uppercase_char, end="")
    print()
        #print("{:c}"
              #.format(ord(c) if not islower(c) else ord(c) - 32),
              #end="")
        #print("")
