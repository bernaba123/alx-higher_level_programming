#!/usr/bin/python3
"""
This python script takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in u$
"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
