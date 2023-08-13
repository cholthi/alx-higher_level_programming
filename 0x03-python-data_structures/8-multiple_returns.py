#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns length and first character of the argument in a tuple"""
    if ''.__eq__(sentence.strip()):
        return ((0,None))
    return ((len(sentence), sentence[0]))
