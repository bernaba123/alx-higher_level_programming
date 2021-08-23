#!/usr/bin/python3
"""
fins the peak of a list
"""


def find_peak(list_of_integers):
    """ a function to return the first peak found """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
        if ((list_of_integers[i] >= list_of_integers[i - 1]) and
                (list_of_integers[i] >= list_of_integers[i + 1])):
            return list_of_integers[i]
