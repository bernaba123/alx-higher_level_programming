#!/usr/bin/python3
class LockedClass:
    """prevent the dynamic creation of attributes"""
    __slots__ = ['first_name']
