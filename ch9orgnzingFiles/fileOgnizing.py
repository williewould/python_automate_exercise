# -*- coding: utf-8 -*-
'''
Created on 2020/01/11
@Version:    1.0
@author :    zhaowu
@Ref    :    book
'''
#%% 文件复制操作
import shutil,os
from pathlib import Path
os.getcwd()
p = Path.home()
# 将已经存在的文件复制到新目录，如果文件夹不存在，则是复制为这个文件名
shutil.copy(p/'spam.txt',p/'some_folder')

# 完全制定到文件名，测可以保证复制到米想要的结果
hutil.copy(p/'spam.txt',p/'some_folder/eggs.txt')

# 可以实现文件夹下的所有内容，复制到新的文件夹
shutil.copytree(p/'spam',p/'spam_backup')

# 移动文件(剪切命令)， 必须要制定到文件名否则不运行？
shutil.move(p/'spam.txt',p/'eggs/spam.txt')