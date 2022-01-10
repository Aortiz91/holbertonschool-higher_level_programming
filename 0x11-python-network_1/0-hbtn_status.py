#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""


import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as f:
        website = f.read()
        print('Body response:')
        print("\t- type: {}".format(type(website)))
        print("\t- content: {}".format(website))
        print("\t- utf8 content: {}".format(website.decode('utf-8')))
