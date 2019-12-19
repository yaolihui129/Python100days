#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:20
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : for-in2.py
# @Version : 0.1
# @DESC    :  用for循环实现1~100之间的偶数求和
# @Software: PyCharm

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
