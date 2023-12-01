#!/usr/bin/python3
"""Fetches content from remote url and formats
It in a certain format
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    data = response.read()
    _type = type(data)
    decoded_utf8 = data.decode('utf8')
    print(f"Body response:\n\t- type: {_type}\n\t- content: {data}"""
          f"\n\t- utf8 content: {decoded_utf8}""")
