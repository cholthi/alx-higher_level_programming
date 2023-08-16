#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """maps values of a list my_list using mul function"""
    return list(map(lambda x: x * number, my_list))
