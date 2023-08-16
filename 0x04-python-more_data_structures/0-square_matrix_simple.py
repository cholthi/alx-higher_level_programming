#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes squares of the matrix values and return matrix"""
    new_matrix = []
    for i in matrix:
        new_matrix.append([v * v for v in i])
    return (new_matrix)
