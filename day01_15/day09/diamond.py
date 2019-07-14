#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 多重继承
# - 菱形继承(钻石继承)
# - C3算法(替代DFS的算法)
# @Date    : 2019-07-13 19:41:29
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

class A(object):
	def foo(self):
		print('foo of A')

class B(A):
	pass

class C(A):
	def foo(self):
		print('foo of C')

class D(B,C):
	pass

class E(D):
	def foo(self):
		print('foo in E')
		# super().foo()
		super(B,self).foo()
		super(C,self).foo()

if __name__ == '__main__':
	d = D()
	d.foo()
	e = E()
	e.foo()
