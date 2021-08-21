#!/usr/bin/python3
"""
ends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""


from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    print("{}".format(r.headers.get("X-Request-Id")))
