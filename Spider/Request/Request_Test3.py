# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Test one||| POST
'''

import requests
import logging
from requests.auth import HTTPBasicAuth
from requests import Request, Session
# 1. 基础用法
data = {'name': 'germey', 'age': '22'}
response = requests.post("http://httpbin.org/post", data=data)
print(response.text)

# 2. 响应
response1 = requests.get('http://www.baidu.com')
print(type(response1.status_code), response1.status_code)
print(type(response1.headers), response1.headers)
print(type(response1.cookies), response1.cookies)
print(type(response1.url), response1.url)
print(type(response1.history), response1.history)

# 3. 高级用法
    # 文件上传
files = {'file': open('10.png', 'rb')}
response2 = requests.post('http://httpbin.org/post', files=files)
print(response2.text)

    # 获取 Cookie

response3 = requests.get('https://www.baidu.com')
print(response3.cookies)
for key, value in response3.cookies.items():
    print(key + '=' + value)


    # 使用 cookie
headers = {
    'cookie': 'q_c1=f728a791bdac4bae9844a1f66d9f1db2|1507999787000|1507999787000; _zap=51153a2d-4210-45fc-8ec7-6d4845939979; d_c0="AJCCCUPtvAyPTisR62YFuprjmtQqhGQBeOc=|1511617093"; __DAYU_PP=3RvEjniAmfu6JjQmiUyY20dbadadcda4; __utmz=155987696.1521957184.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); z_c0="2|1:0|10:1524066705|4:z_c0|92:Mi4xUUVvb0F3QUFBQUFBa0lJSlEtMjhEQ1lBQUFCZ0FsVk5rYmZFV3dBQ19KVm5oUTVZVDRZRllrYUFSSHdHRE1YNjNn|59fa2cd09f85f7d2ed4d29d9a09779b726e3d3f494e4d86dec1a6cd121297159"; __utma=155987696.1913419481.1521957184.1521957184.1526829704.2; q_c1=f728a791bdac4bae9844a1f66d9f1db2|1530457421000|1507999787000; _xsrf=8ab7edb5e57aba8e37c5ed050270bf41; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response4 = requests.get("https://www.zhihu.com",headers=headers)
print(response4.text)


    # 使用 cookie
cookies = 'q_c1=f728a791bdac4bae9844a1f66d9f1db2|1507999787000|1507999787000; _zap=51153a2d-4210-45fc-8ec7-6d4845939979; d_c0="AJCCCUPtvAyPTisR62YFuprjmtQqhGQBeOc=|1511617093"; __DAYU_PP=3RvEjniAmfu6JjQmiUyY20dbadadcda4; __utmz=155987696.1521957184.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); z_c0="2|1:0|10:1524066705|4:z_c0|92:Mi4xUUVvb0F3QUFBQUFBa0lJSlEtMjhEQ1lBQUFCZ0FsVk5rYmZFV3dBQ19KVm5oUTVZVDRZRllrYUFSSHdHRE1YNjNn|59fa2cd09f85f7d2ed4d29d9a09779b726e3d3f494e4d86dec1a6cd121297159"; __utma=155987696.1913419481.1521957184.1521957184.1526829704.2; q_c1=f728a791bdac4bae9844a1f66d9f1db2|1530457421000|1507999787000; _xsrf=8ab7edb5e57aba8e37c5ed050270bf41; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8'
jar = requests.cookies.RequestsCookieJar()
headers1 = {
    'Host': 'https://www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
response5 = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
print(response5.text)

    # session 维持
requests.get('http://httpbin.org/cookies/set/number/123456789')
response6 = requests.get('http://httpbin.org/cookies')
print(response6.text)

    # session 维持
sess = requests.Session()
sess.get('http://httpbin.org/cookies/set/number/123456789')
response7 = sess.get('http://httpbin.org/cookies')
print(response7.text)

    # SSL证书验证
logging.captureWarnings(True)
response8 = requests.get('https://www.12306.cn', verify=False)
print(response8.status_code)

    # 设置代理
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
#requests.get('https://www.taobao.com', proxies=proxies)

    # 超时设置
response9 = requests.get('https://www.taobao.com', timeout=10)
print(response9.status_code)

    # 身份验证
#response10 = requests.get('http://localhast:5000', auth=('username', 'password'))
#print(response10.status_code)

    # Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers2 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
