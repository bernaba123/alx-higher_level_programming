#!/usr/bin/python3
"""
ist 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
<sha>: <author name>` (one by line)
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/repos/"
    url = url + argv[2] + "/" + argv[1] + "/commits"
    res = requests.get(url)
    lists_ = res.json()
    for dic in lists_[0:10]:
        print("{}: {}".format(dic.get('sha'),
                              dic.get('commit').get('author').get('name')))
