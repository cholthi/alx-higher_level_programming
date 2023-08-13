#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns length and first character of the argument in a tuple"""
    if sentence == '':
        return ((None,))
    return ((len(sentence), sentence[0]))
