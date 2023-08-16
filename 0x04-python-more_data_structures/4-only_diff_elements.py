#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """computes the diff of the two list"""
    return (list(set(set_1) - set(set_2)) + list((set(set_2) - set(set_1))))
