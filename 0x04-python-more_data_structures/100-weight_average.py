#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns weighted average of the input list"""
    res = (sum([a * b for a, b in my_list])) / (sum(dict(my_list).values()))
    return (res)
