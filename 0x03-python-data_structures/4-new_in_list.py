#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist_copy = my_list.copy()

    if idx >= 0 and idx <= (len(my_list) - 1):
        mylist_copy[idx] = element
        return mylist_copy
