# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:28:30 2020

@author: zhaowu
"""

def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message.')

spam()

#%%报错信息打印， 生成日志信息
try:
    raise Exception('This is the error messgage.')
except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')