#!/usr/bin/python3

"""
This script takes a URL as a command line argument and sends a request to that URL. It then prints the value of the "X-Request-Id" header from the response.

Example Usage:
    python script.py https://example.com

Inputs:
    url (string): The URL to send the request to. It is passed as a command line argument.

Outputs:
    The value of the "X-Request-Id" header from the response is printed.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
