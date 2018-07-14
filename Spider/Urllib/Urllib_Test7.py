# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| parse
'''

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote

# 1. urllib.parse.urlparse(urlstring, scheme='',allow_fragments=True) URL 识别与分段
# scheme : 协议 、 netloc : 域名 、 path: 路径 、 params:参数 、 query:查询条件 、GET下还有参数 fragment:锚点
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# 2. urllib.parse.urlunparse   拼接URL 长度必须为6
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))

# 3.urllib.parse.urlsplit  拆解URL
result1 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result1)
print(result1.scheme, result1[0])

# 4.urllib.parse.urlunsplit 拼接URL  长度必须为5
data2 = ['http','www.baidu.com','index.html','a=7','comment']
print(urlunsplit(data2))

# 5.urllib.parse.urljoin 合并URL，拼接 base_url
# base_url:作为第一个参数，new_url:作为第二参数
# 分析base_url 对新连接缺失部分进行补充
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))

# 6.urllib.parse.urlencode 构造参数
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# 7.urllib.parse.parse_qs 反序列化参数
query = 'name=germey&age=22'
print(parse_qs(query))

# 8.urllib.parse.parse_sql 参数转反序列化
query = 'name=germey&age=22'
print(parse_qsl(query))

# 9.urllib.parse.quote 将内容转化为URL编码格式
keyword = '壁纸'
url1 = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url1)

# 10.urllib.parse.unquote 将内容URL 解码
url2 = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url2))