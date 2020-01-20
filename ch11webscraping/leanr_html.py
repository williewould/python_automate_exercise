# -*- coding: utf-8 -*-
'''
Created on 2020/01/20
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    能够快速定位到我们想要的元素就好，解析HTML页面可以用bs4
- https://developer.mozilla.org/en-US/learn/html/
- https://htmldog.com/guides/html/beginner/
- https://www.codecademy.com/learn/learn-html
'''
# CSS tutorial https://nostarch.com/automatestuff2/
import requests
import bs4
import os

res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))
print(os.getcwd())
# 将example.html放在工作目录下
exampleFile = open('example.html')
# 得到bs4 对象，并分析
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))
# 进行筛选 并返回列表 .select 方法
elem = exampleSoup.select('#author')
print(type(elem))
print(len(elem))
print(str(elem[0]))
# .getText获得 tag标签内的内容
print(elem[0].getText())
print(elem[0].attrs)

pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
# 查找这个标签 发现没有
print(spanElem.get('some_nonexistent_addr') == None)
print(Elem.attrs)
