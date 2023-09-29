#!/usr/bin/python3

"""
This script makes a GET request to the URL "https://intranet.hbtn.io/status"
using the requests library. It then prints the response body,
including the type of the response and its content.

Example Usage:

    if __name__ == "__main__":
        r = requests.get("https://intranet.hbtn.io/status")
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
