#!/usr/bin/python3

"""
This code snippet is a standalone script that takes a URL as a
command-line argument and sends a GET request
to that URL using the requests library.
It then checks the status code of the response and
prints either the error code or the response text.

Example Usage:
    python script.py https://www.example.com

Inputs:
    url (string): The URL to send the GET request to.
    It is passed as a command-line argument.

Outputs:
    If the status code of the response is greater than or equal to 400,
    the code snippet prints the error code.
    If the status code is less than 400,
    the code snippet prints the response text.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
