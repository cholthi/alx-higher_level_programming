#!/usr/bin/python3


if __name__ == '__main__':
    """Prints its arguments"""
    import sys


    arglen = len(sys.argv) - 1
    if arglen == 1:
        argument = 'argument:'
    elif arglen = 0:
        argument = 'argument.'
    else:
        argument = 'arguments:'
    print('{} {}'.format(arglen, argument))
    [print('{}: {}'.format(idx + 1, x)) for idx, x in enumerate(sys.argv[1:])]
