# -*- coding: utf-8 -*-
'''
Created on 2020/01/06
@Version:    1.0
@author :    zhaowu
@Ref    :    book
'''
import numpy as np
import matplotlib.pyplot as plt

# braunch 功能测试，在github上操作
msg = 'hello,word'
print("hello word\n")
print(msg)


# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
