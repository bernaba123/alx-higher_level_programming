#!/usr/bin/python3
"""Matrix multiplication using numpy module.
The inputs are list of lists
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Matrix multiplication.
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    Yields:
        list of lists
    """
    return np.array(m_a).dot(np.array(m_b))
