# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| Cookie
'''

import http.cookiejar, urllib.request

filename = "cookie.txt"
cookie2 = http.cookiejar.LWPCookieJar(filename)
cookie1 = http.cookiejar.MozillaCookieJar(filename)
cookie0 = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookie1)
opener = urllib.request.build_opener(handler)
response = opener.open("https://www.baidu.com/")
# 保存cookie
cookie1.save(ignore_discard=True, ignore_expires=True)

# 打印cookie
#for item in cookie1:
#    print(item.name+"="+item.value)


