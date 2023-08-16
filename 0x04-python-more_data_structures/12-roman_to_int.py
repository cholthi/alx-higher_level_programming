#!/usr/bin/python3

def roman_to_int(roman_string):
    """Roman to Dec """
    roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
            'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    dec = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:1 + 2] in roman_map:
            dec += roman_map[roman_string[i:1 + 2]]
            i += 2
        else:
            dec += roman_map[roman_string[i]]
            i += 1
    return (dec)
