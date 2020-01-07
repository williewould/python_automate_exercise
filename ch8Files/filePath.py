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

#创建目录
#os.makedirs('.\\book')

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

# TODO GOOD











