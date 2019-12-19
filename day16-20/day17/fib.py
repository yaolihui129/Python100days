#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 迭代器和生成器
# 和迭代器相关的魔术方法（__iter__和__next__）
# 两种创建生成器的方式（生成器表达式和yield关键字）
# @Date    : 2019-07-21 18:37:37
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

def fib(num):
	"""生成器"""
	a,b = 0,1
	for _ in range(num):
		a,b = b,a+b
		yield a

class Fib(object):
	""" 迭代器"""
	def __init__(self,num):
		self.sum = sum
		self.a ,self.b = 0,1
		self.idx = 0

	def __iter__(self):
		return self

	def next(self):
		if self.idx < self.num:
			self.a ,self.b = self.b,self.a + self.b
			self.idx += 1
			return self.a
		raise StopIteration()


