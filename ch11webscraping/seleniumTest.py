# -*- coding: utf-8 -*-
'''
Created on 2020/01/22
@Version:    1.0
@author :    zhaowu
@Ref    :    测试selenium模块的功能
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 在网页上寻找 cover-thumb元素 并返回所属类型
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except Exception:
    print('Was not able to find an element with that name')
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()
# 在网页上登录
browser2 = webdriver.Firefox()
browser2.get('https://login.metafilter.com')
userElem = browser2.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')
passwordElem = browser2.find_element_by_id('user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()
# 在网页上 利用Key输入特殊字符 或者特殊键盘操作
browser3 = webdriver.Firefox()
browser3.get('https://nostarch.com')
htmlElem = browser3.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)
browser3.quit()
