#!/usr/bin/python3

"""
This script takes a URL as a command line argument and
sends a GET request to the specified URL.
It then retrieves the value of the "X-Request-Id"
header from the response and prints it.
Example Usage:
    python script.py https://example.com

Inputs:
    url (string): The URL to send the GET request to.

Outputs:
    The value of the "X-Request-Id" header from the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
