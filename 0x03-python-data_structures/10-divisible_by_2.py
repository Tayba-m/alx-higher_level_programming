#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list_d = []
    for t in my_list:
        if (t % 2) == 0:
            list_d.append(True)
        else:
            list_d.append(False)
    return list_d
