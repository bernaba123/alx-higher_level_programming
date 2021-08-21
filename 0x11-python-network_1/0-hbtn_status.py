#!/usr/bin/python3
"""
This module contains a
Python script that fetches
https://intranet.hbtn.io/status
"""


import urllib.request


if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as myurl:
        data = myurl.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
