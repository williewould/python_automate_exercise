# -*- coding: utf-8 -*-
'''
Created on 2020/01/15
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Function:   用来打印方框，练习使用 try except 处理错误
'''
# try except 在检测到错误后，不会立刻终止程序，而是提示报错信息，然后继续执行后面的代码


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol+(' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
