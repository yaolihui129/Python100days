#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:24
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : range9.py
# @Version : 0.1
# @DESC    :  输出乘法口诀表(九九表)
# @Software: PyCharm

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
