#!/usr/bin/python3
"""Takes a URL as an argument and send requests to it
Prints the response if success or
prints the error code
"""

if __name__ == '__main__':
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read())
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
