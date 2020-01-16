# -*- coding: utf-8 -*-
'''
Created on 2020/01/15
@Version:    1.0
@author :    zhaowu
@Ref    :    book
'''
# %% try except; raise exception 来处理错误

# raise需要在try except[不中断程序，仅提示错误]中调用
raise Exception('This is the error message')

# %% 断言 会在检测到功能错误后，立刻终止程序
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
assert ages[0] <= ages[-1]
ages.reverse()
assert ages[0] <= ages[-1]
"""
运行python 时 跳过断言
Python script with python -O myscript.py instead of python
myscript.py, Python will skip assert statements
"""
