#!/usr/bin/python3

def no_c(my_string):
    """Removes character 'c' and 'C' from string my_string"""
    return (''.join(list((c for c in my_string if c not in 'cC'))))
