#!/usr/bin/python3
def uppercase(str):
    for i in len(str):
        if str[i] >= 'a' and str[i] <= 'z':
            str = chr(ord(str[i]) - 32)
        else:
            str = chr(ord(str[i]))
        print(str, end="")
    print("\n", end="")
