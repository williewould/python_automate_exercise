# -*- coding: utf-8 -*-
'''
Created on 2020/01/17
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    用factorial来测试logging模块
'''
# %% 简单的日志打印
import logging
# asctime 时间  levelname 日志等级的划分 message 是debug中的字符串内容
# logging.disable(层级) 不再打印该层级及以下的日志
# logging.disable(logging.CRITICAL)
logging.basicConfig(filename='myProgramlog.txt', level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')


# %% logging 日志的分类层级 利用config中的level参数
# 可以控制什么显示什么不显示
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('some debugging details')
logging.info('the logging module is working')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred')
logging.critical('The program is unable to recover')

# ERROR 以下的不打印 但 ERROR以上的层级critical还会打印
logging.disable(logging.ERROR)
logging.error('error error')
logging.critical('Critical error ')

# 打印日志
logging.basicConfig(filename='myProgramlog.txt', level=logging.DEBUG,
                    format='%(asctime)s- %(levelname)s- %(message)s')
