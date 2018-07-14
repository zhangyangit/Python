# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| Handler()
'''
#代理服务器的设置
#应用场景：使用同一个IP去爬取同一个网站上的网页，久了之后会被该网站服务器屏蔽。
#解决方法：使用代理服务器。 （使用代理服务器去爬取某个网站的内容的时候，在对方的网站上，显示的不是我们真实的IP地址，而是代理服务器的IP地址）

import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    "http": "http://127.0.0.1:9743",
    "https": "https://127.0.0.1:9743"
})

opener = urllib.request.build_opener(proxy_handler)
response = opener.open("https://www.baidu.com/")
print(response.read().decode("utf-8"))