#!/usr/bin/python3
"""Takes a url as argument and Fetches content from remote url
and displays the value of the X-Request-Id header
"""

if __name__ == '__main__':
    from urllib import request
    import sys

    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.info().get('X-Request-Id'))
