#!/usr/bin/python3
"""multiplys two matrices using Numpy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (numpy.matmul(m_a, m_b))
