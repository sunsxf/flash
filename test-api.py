#!/usr/bin/env python
# --coding-- utf-8

'''
'''

import requests
import json

url = 'http://localhost:5000/flash?pkg=com.test.a&ver=1&mk=android'
r = requests.get(url)
resp_data = r.text
if 'etag' in r.headers:
    etag = r.headers['etag']
else:
    etag = None
status = r.status_code
print("HTTP GET, request url : %s" % r.url)
print("status code : ", status)
print("etag : %s" % etag)
print("response : %s" % resp_data)


if etag is not None:
    headers = {'etag': etag}
    r1 = requests.get(
        url, headers=headers
    )
    resp_data = r1.text
    status = r1.status_code
    if 'etag' in r1.headers:
        etag = r1.headers['etag']
    else:
        etag = None
    print("\n*******************************************\n")
    print("HTTP GET, request url : %s" % r1.url)
    print("status code : ", status)
    print("etag : %s" % etag)
    print("response : %s" % resp_data)

