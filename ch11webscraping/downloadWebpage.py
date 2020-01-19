# -*- coding: utf-8 -*-
'''
Created on 2020/01/19
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    利用requests.get() 下载网页信息
'''
# %% 获得网页信息问题代码 https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# 判定requests 是否正确地获得了网页
print(res.status_code == requests.codes.ok)
# 获得文件字节数
print(len(res.text))
print(res.text[:250])
playFile = open('RomeoAndJuliet.txt', 'wb')
# 以chunk形式写入数据，防止一次RAM进大量数据导致内存消耗过大
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
# %% 判定请求错误
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
# 抛出异常 如果是200则没有问题
except Exception as exc:
    print('There was a problem: %s' % (exc))
