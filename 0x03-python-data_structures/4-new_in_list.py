#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    t_list = my_list[:]
    if 0 <= idx < len(my_list):
        t_list[idx] = element
        return (t_list)
    return (my_list)
