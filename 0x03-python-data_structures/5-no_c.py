#!/usr/bin/python3
def no_c(my_string):
    r = ""
    for i in range(len(my_string)):
        if my_string[i] != "C" or my_string[i] != "c":
            return(r += my_string[i])
