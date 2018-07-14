# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| request()
'''

import urllib.request
from urllib import request, parse

url = "http:/http://httpbin.org/post"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
           'Host': 'httpbin.org'
           }

dict = {'name': 'Germey'
        }
request1 = request.Request("https://python.org")
response1 = request.urlopen(request)
print(response1.read().decode("utf-8"))

data = bytes(parse.urlencode(dict), encoding='utf8')
request2 = request.Request(url=url, data=data, headers=headers, method='POST')
response2 = request.urlopen(request2)
print(response2.read().decode("utf-8"))