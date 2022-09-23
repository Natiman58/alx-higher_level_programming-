#!/usr/bin/python3
"""
    A python request that sends a URL and
    displays the value of the variable 'X-Request-Id'
    from the response header
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
