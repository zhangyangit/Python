# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python Scrapy ||| re
'''

import re

# 1. re.match()
    # 基础示例 \d+ --- 至少一个数字
content = 'Hello 123 4567 World_this is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

content3 = 'Hello 1234567 World_this is a Regex Demo'
    # 匹配目标 () -- 匹配分组
result1 = re.match('^Hello\s(\d+)\sWorld', content3)
print(result1)
print(result1.group(1))
print(result1.span())

    # 通用匹配   ^ - 匹配开头 、$ - 匹配结尾
result2 = re.match('^Hello.*Demo$', content)
print(result2)
print(result2.group())
print(result2.span())

    # 贪婪匹配   (.*) --- 尽可能多的匹配
result3 = re.match('^He.*(\d+).*Demo$', content3)
print(result3)
print(result3.group(1))

    # 非贪婪匹配 （.*?）--- 尽可能少的匹配
result4 = re.match('^He.*?(\d+).*Demo$', content3)
print(result4)
print(result4.group(1))

content1 = '''Hello 1234567 world_this
is a Regex Demo
'''
    # 修饰符匹配
# re.S --- 修正，匹配换行符在内的所有字符
# re.I ---  是匹配对大小写不敏感
# re.L ---  做本地化识别匹配
# re.M ---  多行匹配
# re.U ---  根据Unicode 字符集解析字符
# re.X
result5 = re.match('^He.*?(\d+).*?Demo$', content1, re.S)
print(result5)
print(result5.group(1))

content2 = '(百度)www.baidu.com'
    # 转义匹配
result6 = re.match('\(百度\)www\.baidu\.com', content2)
print(result6)

# 2. re.search()

content4 = 'Extra stings Hello 1234567 World_this is a Regex Demo Extra stings'
result7 = re.search('Hello.*?(\d+).*?Demo', content4)
print(result7)
print(result7.group(1))

# 3. re.findall() 搜索整个字符串

# 4. re.sub()  replace 字符串中的某些信息
content5 = '54aK54yr5oiR54ix5L2g'
content5 = re.sub('\d+', '', content5)
print(content5)

# 5. re.compile() 将 正则字符串编译成正则表达式
content6 = '2018-07-02 12:00'
content7 = '2018-07-03 12:55'
content8 = '2018-07-04 13:21'
pattern = re.compile('\d{2}:\d{2}')
result8 = re.sub(pattern, '', content6)
result9 = re.sub(pattern, '', content7)
result10 = re.sub(pattern, '', content8)
print(result8, result9, result10)