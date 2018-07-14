# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Beautiful Soup
'''
from bs4 import BeautifulSoup
import re


# 1. example
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 初始化 BeautifulSoup 对象， 以 lxml 作为解释器
soup = BeautifulSoup(html, 'lxml')
# 将要解析的字符串以标准缩进格式输出
# 其中HTML字符串自动更正在初始化过程完成
print(soup.prettify())
# 输出节点内容
print(soup.title.string)

### 1. 节点选择器
# 2. 选择元素

html1 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup1 = BeautifulSoup(html1, 'lxml')
# title 节点
print(soup1.title)
# title 类型
print(type(soup1.title))
# 节点内容
print(soup1.title.string)
# head 节点
print(soup1.head)
# p 节点
print(soup1.p)

# 3. 提取信息
# (1. 名称)
print(soup1.title.name)
# (2. 属性)
print(soup1.p.attrs)
# (3. 内容)
print(soup1.p.string)

# 4. 嵌套选择
html2 = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.head.title)
print(type(soup2.head.title))
print(soup2.head.title.string)

# 5. 关联选择

html3 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup3 = BeautifulSoup(html3, 'lxml')
print(soup3.p.contents)
# (1. 子节点)
print(soup3.p.children)
for i, child in enumerate(soup3.p.children):
    print(i, child)
# (2. 父节点与祖先节点)

html4 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
soup4 = BeautifulSoup(html4, 'lxml')
# 直接父节点
print(soup4.a.parent)
print(type(soup4.a.parents))
# 所有祖先节点
print(list(enumerate(soup4.a.parents)))
# (3. 兄弟节点)

html5 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
from bs4 import BeautifulSoup
soup5 = BeautifulSoup(html5, 'lxml')
print('Next Sibling', soup5.a.next_sibling)
print('Prev Sibling', soup5.a.previous_sibling)
print('Next Siblings', list(enumerate(soup5.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup5.a.previous_siblings)))
# (4. 提取信息)

html6 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
soup6 = BeautifulSoup(html6, 'lxml')
print('Next Sibling:')
print(type(soup6.a.next_sibling))
print(soup6.a.next_sibling)
print(soup6.a.next_sibling.string)
print('Parent:')
print(type(soup6.a.parents))
print(list(soup6.a.parents)[0])
print(list(soup6.a.parents)[0].attrs['class'])

### 2. 方法选择器
# 1. find_all()
# 原型： find_all(name, attrs, recursive, text, **kwargs)
html7 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# name
soup7 = BeautifulSoup(html7, 'lxml')
print(soup7.find_all(name='ul'))
print(type(soup7.find_all(name='ul')[0]))

# attrs
html8 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup8 = BeautifulSoup(html8, 'lxml')
print(soup8.find_all(attrs={'id': 'list-1'}))
print(soup8.find_all(attrs={'name': 'elements'}))

# text
html9 = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup9 = BeautifulSoup(html9, 'lxml')
print(soup9.find_all(text=re.compile('link')))

# 2. find() 发现单个元素，意思是匹配到的第一个元素

html10 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup10 = BeautifulSoup(html10, 'lxml')
print(soup10.find(name='ul'))
print(type(soup10.find(name='ul')))
print(soup10.find(class_='list'))

# 其他的一下方法
'''
find_parents() find_parent()
find_parents() 返回所有祖先节点，find_parent() 返回直接父节点。
find_next_siblings() find_next_sibling()
find_next_siblings() 返回后面所有兄弟节点，find_next_sibling() 返回后面第一个兄弟节点。
find_previous_siblings() find_previous_sibling()
find_previous_siblings() 返回前面所有兄弟节点，find_previous_sibling() 返回前面第一个兄弟节点。
find_all_next() find_next()
find_all_next() 返回节点后所有符合条件的节点, find_next() 返回第一个符合条件的节点。
find_all_previous() 和 find_previous()
find_all_previous() 返回节点后所有符合条件的节点, find_previous() 返回第一个符合条件的节点
'''

### 3. CSS选择器
html11 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup11 = BeautifulSoup(html11, 'lxml')
print(soup11.select('.panel .panel-heading'))
print(soup11.select('ul li'))
print(soup11.select('#list-2 .element'))
print(type(soup11.select('ul')[0]))
# 嵌套选择
for ul in soup11.select('ul'):
    print(ul.select('li'))
# 获取属性
for ul in soup11.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
# 获取文本
for li in soup11.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)


