#!/usr/bin/python3
for i in range(9):
    for j in range(1,10):
        if j > i:
            if j != 9 or i != 8:
                print("{:d}{:d}, ".format(i, j), end="")
            else:
                print("{:d}{:d}".format(i, j))
