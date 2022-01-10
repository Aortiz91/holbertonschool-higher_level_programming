#!/usr/bin/python3
""" Python script
"""


import sys
import requests


if __name__ == "__main__":
    url_req = requests.get(sys.argv[1])
    print(url_req.headers['X-Request-Id'])
