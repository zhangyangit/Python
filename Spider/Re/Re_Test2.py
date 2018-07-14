# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python Scrapy ||| 爬取猫眼电影TOP100
'''
# 1. 目标： 爬取猫眼电影TOP100

# 2. 要求： 爬取的信息包括： 电影名称， 时间， 排名， 图片， 主演，评分等

# 3. 结果： 提取爬取结果，以文件的方式保存

import re
import requests
import time
import json
from requests.exceptions import RequestException


# 爬取信息
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None
    except RequestException:
        return None


# 解析网页
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a'
        +'.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>'
        +'.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'star': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip()
        }


# 写入文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 轮询
def get_mutli_page(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


# 测试
if __name__ == '__main__':
    for i in range(10):
        get_mutli_page(offset=i * 10)
        time.sleep(1)
