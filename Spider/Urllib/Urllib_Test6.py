# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| error
'''

from urllib import request, error
import socket

try:
    response = request.urlopen("http://cuiqingcai.com/index.htm")
except error.URLError as e:
    print(e.reason)


try:
    response1 = request.urlopen("http://cuiqingcai.com/index.htm")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')


try:
    response2 = request.urlopen("https://www.baidu.com", timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time out')