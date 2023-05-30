#!/usr/bin/python3

def safe_print_division(a, b):
    """Pint result of dividing a by b."""

    try:
        res =  a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {:d}".format(res))
        return (res)
