# -*- coding: utf-8 -*-
'''
Created on 2020/01/16
@Version:    1.0
@author :    zhaowu
@Ref    :    book
@Desc   :    红绿灯模拟器和断言 assertion
'''

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    # \ 用来实现代码换行(空格+\)
    assert 'red' in stoplight.values(), 'Neither Light is red!' \
        + str(stoplight)
    print(stoplight)


switchLights(market_2nd)
