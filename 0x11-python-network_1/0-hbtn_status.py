#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:
        website = f.read()
        print("Body response:")
        print('\t- type: {}'.format(type(website)))
        print('\t- content: {}'.format(website))
        print('\t- utf8 content: {}'.format(website.decode("utf-8", "replace")))
