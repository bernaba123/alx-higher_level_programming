#!/usr/bin/python3
"""
fetch form a give website and display in a given format
"""
import requests

if __name__ == "__main__":
    res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
