#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:21
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : for-in3.py
# @Version : 0.1
# @DESC    :  用for循环实现1~100之间的偶数求和
# @Software: PyCharm

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
