#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:09
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test2.py
# @Version : 0.1
# @DESC    :  分段函数求值
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
# @Software: PyCharm

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))