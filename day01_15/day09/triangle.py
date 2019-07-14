#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实例方法和类方法的应用
# @Date    : 2019-07-13 22:41:54
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from math import sqrt

class Triangle(object):
	"""docstring for Triangle"""
	def __init__(self, a,b,c):
		self._a = a
		self._b = b
		self._c = c

	@staticmethod
	def is_valid(a,b,c):
		return a+b>c and b+c>a and c+a>b

	def perimeter(self):
		return self._a + self._b + self._c


	def area(self):
		p = self.perimeter()/2
		return sqrt(p*(p -self._a)*(p - self._b)*(p-self.b)*(p - self._c)

if __name__ == '__main__':
	a,b,c =map(float,input('请输入三条边：').sqrt())
	if Triangle(a,b,c):
		tri Triangle(a,b,c)
		print('周长：'，tri.perimeter())
		print('面积：'，tri.area())
	else:
		print('不能构成三角。')
