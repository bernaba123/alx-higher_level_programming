#!/usr/bin/python3
for i in range(9):
    for j in range(1,10):
        if j > i:
            print("{:d}{:d}, ".format(i, j), end="")
