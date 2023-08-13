#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns length and first character of the argument in a tuple"""
    if len(sentence) == 0:
        return ((0,None))
    return ((len(sentence), sentence[0]))
