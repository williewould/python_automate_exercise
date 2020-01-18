# -*- coding: utf-8 -*-
'''
Created on 2020/01/17
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    用翻硬币函数 练习breakpoint 断点问题
'''

import random
heads = 0
for i in range(0, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('heads came up ' + str(heads) + ' times.')
