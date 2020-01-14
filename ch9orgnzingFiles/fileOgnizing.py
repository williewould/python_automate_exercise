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
shutil.copy(p/'spam.txt',p/'some_folder/eggs.txt')

# 可以实现文件夹下的所有内容，复制到新的文件夹
shutil.copytree(p/'spam',p/'spam_backup')

# 移动文件(剪切命令)， 必须要制定到文件名否则不运行？
shutil.move(p/'spam.txt',p/'eggs/spam.txt')

# 删除文件的两种方法
# 永久删除 os.unlink()
import shutil,os
from pathlib import Path
#得到目录中后缀为.rxt的所有文件
for filename in Path.home().glob('*.rxt'):
    print(filename)
    #os.unlik(filename)    #确定删除的目录是要删除的文件后，再执行永久删除

# 送到回收站 send2trash
import send2trash
baconFile = open('bacon.txt','a')    #新建文件
baconFile.write('bacon is not a vegetable')
baconFile.close()
send2trash.send2trash('bacon.txt')

# 遍历文件树 os.walk() 函数
for folderName, subfolders, filenames in os.walk('C:\\Users\\zhaowu\\spam'):
    print('The current folder is '+folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ':' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ':' + filename)
    print('')

#%% 压缩文件
import zipfile,os
from pathlib import Path
p = Path.home()
# 得到一个zip的对象
exampleZip = zipfile.ZipFile(p/'spam.zip')
# 得到zip对象的信息参数，目录信息 需要与list中的格式一致
spamInfo = exampleZip.getinfo('spam/spam.txt')
spamInfo.file_size
# 关闭zip对象
exampleZip.close()
# 显示压缩率 file_size是文件原始大小 compress_size是压缩后的大小
exampleZip = zipfile.ZipFile(p/'spam2.zip')
spamInfo = exampleZip.getinfo('spam/spam.txt')
spamInfo.file_size
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size,2)} x smaller'

# 解压缩文件
exampleZip = zipfile.ZipFile(p/'spam2.zip')
exampleZip.extractall(p)    #p是文件目录 C:\Users\zw
exampleZip.close()

# 新建压缩文件 压缩内容精确到后缀，否则知识压缩文件夹，却不包含里面的文件
newZip = zipfile.ZipFile(p/'new.zip','w')
newZip.write(p/'eggs.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
# 添加新文件到压缩文件
newZip = zipfile.ZipFile(p/'new.zip','a')
newZip.write('eggs\\bb.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()