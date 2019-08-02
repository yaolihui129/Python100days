#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generator2
# @Date    : 2019-07-17 16:24:47
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

def fib(num):
	n,a,b = 0,0,1
	while n < num:
		yield b
		a,b = b,a+b
		n +=1

for x in fib(20):
	print(x)
