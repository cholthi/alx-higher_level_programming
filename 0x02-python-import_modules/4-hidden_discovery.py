#!/usr/bin/python3

if __name__  == "__main__":
    """Prints names defined in the hiiden module."""

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if namep[:2] != "__":
            print(name)
