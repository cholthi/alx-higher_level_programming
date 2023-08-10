#!/usr/bin/python3
from sys import argv

arglen = len(argv) - 1

if __name__ == '__main__':
    if arglen == 1:
        argument = 'argument:'
    elif(arglen <= 0):
        argument = 'argument.'
    else:
        argument = 'arguments:'
    print('{} {}'.format(arglen, argument))
    [print('{}: {}'.format(idx + 1, x)) for idx, x in enumerate(argv[1:])]

