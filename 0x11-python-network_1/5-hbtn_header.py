#!/usr/bin/python3
""" Python script
"""


import sys
import requests


if __name__ == "__main__":
    import requests
    from sys import argv

    url_req = requests.get(argv[1])
    print(url_req.headers.get('x-request-id'))
