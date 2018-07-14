# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python 爬虫 -- Tencent
'''

import requests
from bs4 import BeautifulSoup


url = "http://news.qq.com/"
# 请求URL，获取text文本
webdata = requests.get(url).text
# 文本解析
soup = BeautifulSoup(webdata, 'lxml')
# 解析文件，select选择器定位元素，返回列表
news_titles = soup.select("div.text > em.f14 > a.linkto")

# 遍历列表
for n in news_titles:
    # 提取标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = {
        'Title': title,
        'Link': link
    }
    print(data)