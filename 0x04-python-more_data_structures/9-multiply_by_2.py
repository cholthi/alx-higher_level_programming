#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """multple dict values by 2"""
    d = {k: v * 2 for k, v in a_dictionary.copy().items()}
    return (d)
