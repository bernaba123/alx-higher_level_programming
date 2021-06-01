#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """reads my_file_0.txt with utf-8"""
    with open(filename, encoding='utf-8') as f:
        """prints the text file"""
        print(f.read(), end="")
