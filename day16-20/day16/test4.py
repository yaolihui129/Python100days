#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 迭代工具 - 排列 / 组合 / 笛卡尔积
# @Date    : 2019-07-19 09:57:26
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import itertools

a = itertools.permutations('ABCD')
print(a)
b = itertools.combinations('ABCDE',3)
print(b)
c = itertools.product('ABC','123')
print(c)