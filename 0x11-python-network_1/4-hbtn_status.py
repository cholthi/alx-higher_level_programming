#!/usr/bin/python3
""" Fetches content of the a URL and displays it in a format"""

import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(response.text)}"
          f"\n\t- content: {response.text}")
