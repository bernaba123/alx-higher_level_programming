#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, new_size=0):
        """Initialize class."""
        if new_size is not 0:
            self.__size = new_size
