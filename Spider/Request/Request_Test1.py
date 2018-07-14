# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| 
'''

import requests

response = requests.get("https://www.baidu.com/")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")