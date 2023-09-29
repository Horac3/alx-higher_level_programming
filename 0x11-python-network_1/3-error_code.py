#!/usr/bin/python3



"""
Retrieve the content of a URL specified as a command-line argument.

Args:
    sys.argv[1] (str): The URL to retrieve, passed as a command-line argument.

Example Usage:
    $ python script.py https://www.example.com

Outputs:
    The content of the URL specified as a command-line argument, if the request is successful.
    The error code of the `HTTPError` exception, if the request returns an HTTP error.
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
