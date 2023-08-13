#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """sums tuples args passed to it"""
    all_tuples = (tuple_a, tuple_b)
    return tuple((sum(t) for t in all_tuples))
