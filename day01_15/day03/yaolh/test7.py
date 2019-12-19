#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:14
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test7.py
# @Version : 0.1
# @DESC    :  入三条边长如果能构成三角形就计算周长和面积
# @Software: PyCharm

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
