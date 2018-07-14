# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Xpath
'''

from lxml import etree

# 1. explame
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# etree 转化并 填充 html,结果为 bytes
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

# 2. 获取所以节点
# // 开头为获取所有符合要求的节点
html1 = etree.parse('./test.html', etree.HTMLParser())
result1 = html1.xpath('//*')
print(result1)

# 3. 获取子节点
# / 或者 // 可以查找元素的子节点或者子孙节点
html2 = etree.parse('./test.html', etree.HTMLParser())
result2 = html2.xpath('//li/a')
print(result2)

# 4. 获取父节点
#  .. 查找元素父节点
html3 = etree.parse('./test.html', etree.HTMLParser())
result3 = html3.xpath('//a[@href="link4.html"]/../@class')
#result4 = html3.xpath('//a[@href="link4.html"]/parent::/@class') 有问题
print(result3)
#print(result4)

# 5. 属性匹配
# @class="item-0"  匹配属性
result4 = html1.xpath('//li[@class="item-0"]')
print(result4)

# 6. 文本获取
# text() 获取文本
result5 = html1.xpath('//li[@class="item-0"]/a/text()')
result6 = html1.xpath('//li[@class="item-0"]//text()')
print(result5)
print(result6)

# 7. 属性获取
# @ 获取属性
result7 = html1.xpath('//li/a/@href')
print(result7)

# 8. 属性值多匹配
text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html4 = etree.HTML(text1)
result8 = html4.xpath('//li[contains(@class, "li")]/a/text()')
print(result8)

# 9. 多属性匹配
text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html5 = etree.HTML(text2)
result9 = html5.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result9)

# 10. 按序选择
text3 = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html6 = etree.HTML(text3)
result10 = html6.xpath('//li[1]/a/text()')
print(result10)
result10 = html6.xpath('//li[last()]/a/text()')
print(result10)
result10 = html6.xpath('//li[position()<3]/a/text()')
print(result10)
result10 = html6.xpath('//li[last()-2]/a/text()')
print(result10)

# 11. 节点周选择
text4 = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html7 = etree.HTML(text4)
# ancestor 获取祖先节点
result11 = html7.xpath('//li[1]/ancestor::*')
print(result11)
result11 = html7.xpath('//li[1]/ancestor::div')
print(result11)
# attribute 获取属性值
result11 = html7.xpath('//li[1]/attribute::*')
print(result11)
# child 获取子节点
result11 = html7.xpath('//li[1]/child::a[@href="link1.html"]')
print(result11)
# descendant 子孙节点
result11 = html7.xpath('//li[1]/descendant::span')
print(result11)
# following 当前节点之后的所有节点
result11 = html7.xpath('//li[1]/following::*[2]')
print(result11)
# following-sibling  当前节点之后的所有同级节点
result11 = html7.xpath('//li[1]/following-sibling::*')
print(result11)