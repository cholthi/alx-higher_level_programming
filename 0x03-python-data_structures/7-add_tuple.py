#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """sums tuples args passed to it"""
    tuple_a = tuple_a + (0,0)
    tuple_b = tuple_b + (0,0)

    return ((tuple_a[0] + tuple_b[0], tuple_a[1], tuple_b[1]))
