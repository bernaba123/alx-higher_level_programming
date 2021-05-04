#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = []
    for i in range(len(my_list)):
        cp.append(my_list[i])
    if idx < 0:
        return cp
    elif idx >= len(my_list):
        return cp
    else:
        my_list[idx] = element
        print("{:d}".format(my_list))
