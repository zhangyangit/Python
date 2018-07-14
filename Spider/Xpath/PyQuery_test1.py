# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- PyQuery
'''
from pyquery import PyQuery as pq
# 1. 初始化
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
print(doc('li'))

## 1 URL 初始化
doc = pq(url='http://cuiqingcai.com')
print(doc('title'))

## 2. 文本初始化
doc = pq(filename='test.html')
print(doc('li'))

# 2. 基本CSS选择器
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# #container .list li，意思是选取 id 为 container 的节点内部的 class 为 list 的节点内部的所有 li 节点
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 3. 查找节点
## 子节点
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
# 调用了 find() 方法，传入了 CSS 选择器，选取其内部的 li 节点
lis = items.find('li')
print(type(lis))
print(lis)
## 父节点
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
items = doc('.list')
# parent() 方法来获取某个节点的父节点
container = items.parent()
print(type(container))
print(container)
## 祖父节点
doc = pq(html)
items = doc('.list')
# parents() 方法来获取某个节点的祖父节点
parents = items.parents()
print(type(parents))
print(parents)
## 兄弟节点
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())

# 4. 遍历
doc = pq(html)
#  items() 方法后，会得到一个生成器，遍历一下
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

# 5. 获取信息
## 获取属性
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
# 调用 attr() 方法来获取属性
print(a.attr('href'))

## 获取文本
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('li')
# html() 方法返回的是第一个 li 节点的内部 HTML 文本
print(li.html())
# 调用了 text() 方法，就可以获取其内部的文本信息
print(li.text())
print(type(li.text()))

# 6. 节点操作
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# 第三个 li 节点，然后调用了 removeClass() 方法
li.removeClass('active')
print(li)
# 调用了 addClass() 方法，又将 class 添加回来
li.addClass('active')
print(li)


html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# 调用 attr() 方法来修改属性，第一个参数为属性名，第二个参数为属性值
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# 3. 伪类选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)