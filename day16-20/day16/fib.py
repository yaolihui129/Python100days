#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 动态规划 - 适用于有重叠子问题和最优子结构性质的问题
# 使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
# @Date    : 2019-07-19 11:48:09
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

def fib(num,tem={}):
	#用递归计算Fibonacci数
	if num in (1,2):
		return 1
	try:
		return temp[num]
	except KeyError:
		temp[num] = fib(num-1) + fib(n-2)
		return temp[num]
