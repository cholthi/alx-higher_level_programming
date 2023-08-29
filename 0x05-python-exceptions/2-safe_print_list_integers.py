#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                len += 1
    except ValueError:
        pass
    finally:
        print()
        return (len)
