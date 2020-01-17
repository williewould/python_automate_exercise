# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:07:13 2020

@author: zhaowu
@goals:  文件路径
"""

#%% 目录基本认识
import os
# 合并字符串生成路径
os.path.join('usr','bin','spam')

#eg:
myFiles=['a.txt','d.csv','i.docx']
for filename in myFiles:
    print(os.path.join('E:\\desktop',filename))
    
    

#%% 目录基本操作
import os    
#当前目录
os.getcwd()

#改变当前目录为
os.chdir('E:\\桌面')

#创建目录 【创建文件夹】
os.makedirs('.\\book')

# 返回绝对路径
os.path.abspath('.')

# 判定绝对路径和相对路径
os.path.isabs('.')

#(查找路径,start) 从start路径到查找路径的相对路径值
os.path.relpath('E:\\桌面\\book','E:\\pycharm')

# 目录名称和基本名称 返回值为元组
path = 'E:\\pythonlianxi\\zw\\test.py'
os.path.dirname(path)
os.path.basename(path)
a = os.path.split(path)
path.split(os.path.sep)

# 获得路径文件大小 单位是:字节 byte
os.path.getsize(path)

# 目录下的文件夹
os.listdir('E:\\pythonlianxi')

#%% 统计文件总大小
import os
totalSize = 0
path0 = 'E:\\pythonlianxi\\zw'
for filename in os.listdir(path0):
    totalSize = totalSize + os.path.getsize(os.path.join(path0,filename))
print('totalSize',totalSize,'bytes')
#%% 判定目录是否存在 是文件 还是文件夹

os.path.exists(path)
os.path.exists('E:\\B')
os.path.isdir('E:\\pythonlianxi')
os.path.isfile('E:\\pythonlianxi\\zw')

# %% 文件操作
# 使用路径方式新建文本文件
from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello,world!')
p.read_text()

# 打开文件，并得到一个file对象 【打开的同时也创建了文件】
helloFile = open('E:\\桌面\\spam.txt')
helloContent = helloFile.read()

# 按行读取，得到字符串列表，对文件读取只能进行一次，之后文件对象的会被清空
helloFile = open('E:\\桌面\\spam.txt')
helloFile.readlines()

# 打开文件，读写操作，w 写模式，直接覆盖
# a模式，在文本后追加
bbbFile = open('E:\\桌面\\bbb.txt','w')
bbbFile.write('you r beautiful\n')
bbbFile.close()
bbbFile = open('E:\\桌面\\bbb.txt','a')
bbbFile.write('you r beautiful')
content = bbbFile.read()
bbbFile.close()
print(content)
# 保存二进制变量 更方便 保存类型更丰富
import os, shelve
os.chdir('E:\\桌面')
shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()

#%% 以py文件保存
import pprint
# 构造一个字典列表 cats
cats = [{'name':'a','desc':'b'},{'name':'p','desc':'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py','w')
fileObj.write('cats = '+pprint.pformat(cats) +'\n')
fileObj.close()
import myCats
myCats.cats[0]['name']
# TODO 一个小项目
