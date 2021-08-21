#!/usr/bin/python3
"""
a python script that takes in a url
sends a request and displays the body
of the response (decoded in utf-8).
"""


import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
