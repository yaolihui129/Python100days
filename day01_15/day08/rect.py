#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义和使用矩形类
# @Date    : 2019-07-13 11:30:44
# @Author  : yaolh
# @Link    : http://example.org
# @Version : 0.1

class Rect(object):
	"""docstring for Reat"""
	def __init__(self, width=0,height=0):
		self._width = width
		self._height = height

	def perimter(self):
		#计算周长
		return (self._width + self._height) *2
	def area(self):
		#计算面积
		return self._width * self._height

	def __str__(self):
		#矩形对象的字符串表达式
		return '矩形[%f,%f]' % (self._width,self._height)

	def __del__(self):
		#析构器
		print('销毁矩形对象')

if __name__ == '__main__':
	rect1 = Rect()
	print(rect1)
	print(rect1.perimter())
	print(rect1.area())
	rect2 = Rect(3,5)
	print(rect2)
	print(rect2.perimter())
	print(rect2.area())


