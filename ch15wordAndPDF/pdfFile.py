# -*- coding: utf-8 -*-
'''
Created on 2020/02/19
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Funcion:    操作PDF 和 word文档
'''

# %% 打开PDF文档
import PyPDF2

pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
# %% 有密码的情况下，打开机密的PDF文档
pdfReader2 = PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
pdfReader2.isEncrypted
print(pdfReader2.getPage(0))
pdfReader2.decrypt('rosebud')
pageObj2 = pdfReader2.getPage(0)
print(pageObj2.extractText())

