# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| GET
'''


import requests
import json
import re

# 1. 基本用法
response = requests.get("http://httpbin.org/get")
print(response.text)

# 2. 带参数请求

response1 = requests.get("http://httpbin.org/get?name=germey&age=22")
print(response1.text)

# 3. 传入参数
data = {
    'name': 'germey',
    'age': '22'
}
response2 = requests.get("http://httpbin.org/get", params=data)
print(response2.text)

# 4. 解析 json

response3 = requests.get("http://httpbin.org/get")
print(type(response3.text))
print(response3.json())
print(json.loads(response3.text))
print(type(response3.text))

# 5. 获取二进制数据
response4 = requests.get("https://github.com/10.png")
print(type(response4.text), type(response4.content))
print(response4.text)
print(response4.content)
with open("10.png", 'wb') as f:
    f.write(response4.content)
    f.close()


# 6. 添加头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
response5 = requests.get("https://www.zhihu.com/explore",headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, response5.text)
print(titles)
print('Hello, World!')

