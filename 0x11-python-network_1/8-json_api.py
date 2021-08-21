#!/usr/bin/python3
"""
a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        alpha = ""
    else:
        alpha = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': alpha}
    r = requests.post(url, data=payload)
    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
