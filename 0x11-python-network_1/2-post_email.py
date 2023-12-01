#!/usr/bin/python3
""" Takes a URL and an email and sends a POST request to
the URL and displays response in utf8 encoding
"""

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    values = {"email": argv[2]}
    data = parse.urlencode(values).encode('utf8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf8'))
