#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:25
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test2.py
# @Version : 0.1
# @DESC    :  输入两个正整数计算最大公约数和最小公倍数
# @Software: PyCharm


x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break