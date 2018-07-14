# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| urlopen()
'''

import urllib.request
import urllib.parse
import urllib.error
import socket

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# Get 类型请求
data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding='utf8')
response = urllib.request.urlopen("https://www.baidu.com/")

print(response.headers)
print(response.code)
print(response.read().decode("utf-8"))

# Post 类型请求
response1 = urllib.request.urlopen("https://httpbin.org/post", data=data)
print(response1.code)
print(response1.read().decode("utf-8"))

# 超时设置
response2 = urllib.request.urlopen("https://httpbin.org/get", timeout=10)
print(response2.code)
print(response2.read().decode("utf-8"))

# 异常处理
try:
    response3 = urllib.request.urlopen("https://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time Out")


