#!/usr/bin/python3
"""Module for multiplying 2 matrices using NumPy"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply 2 matrices using NumPy"""
    return (numpy.matmul(m_a, m_b))
