#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 异常机制 - 处理程序在运行时可能发生的状态
# @Date    : 2019-07-14 15:14:24
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

input_again = True
while input_again:
	try:
		a = int(input('a= '))
		b = int(input('b= '))
		print('%d / %d = %f' % (a,b,a/b))
		input_again = False
	except ValueError:
		print('请输入整数')
	except ZeroDivisionError:
		print('除数不能为 0')
