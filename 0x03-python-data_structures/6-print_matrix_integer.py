#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints matrix of integers"""
    for i in matrix:
        for k, j in enumerate(i):
            if k == 0:
                print('{:d}'.format(j), end='')
            else:
                print(' {:d}'.format(j), end='')
        print('')
    print('')
