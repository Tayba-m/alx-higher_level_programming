#!/usr/bin/python3
def no_c(my_string):
    r = ""
    for t in range(len(my_string)):
        if my_string[t] != 'c' and my_string[t] != 'C':
            r += my_string[t]
    return r
