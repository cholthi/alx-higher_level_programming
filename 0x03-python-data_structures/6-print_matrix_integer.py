#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints matrix of integers"""
    if len(matrix) == 0:
        print('')
        return

    for i in matrix:
        for j in i:
            print('{:d}'.format(j), end='')
        print('')
