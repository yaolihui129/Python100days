#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 引发异常和异常栈
# @Date    : 2019-07-14 15:38:25
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

def f1():
	raise AssertionError('发生异常')

def f2():
	f1()

def f3():
	f2()

f3()
