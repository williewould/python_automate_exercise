# -*- coding: utf-8 -*-
'''
Created on 2020/01/19
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    输入地址 在网页中打开这个地址( 或从剪切板中的地址 打开高德地图 网页)
'''
# 只有文件放入环境变量中，才能在 win+r 中直接运行
import webbrowser
import sys
import pyperclip
# argv 读取命令行的字符
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# 山西省 太原市
webbrowser.open('http://www.amap.com/search?query=' + address)
