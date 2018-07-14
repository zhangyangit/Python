# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| response()
'''

import urllib.request

response = urllib.request.urlopen("https://www.python.org/")
# 响应类型
print(type(response))
# 状态码
print(response.status)
# 响应头
print(response.getheaders())
print(response.getheader("Server"))
# 响应体
print(response.read().decode("utf-8"))
