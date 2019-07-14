#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 多重继承
# - 通过多重继承可以给一个类的对象具备多方面的能力
# - 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
# @Date    : 2019-07-13 21:27:36
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

class Father(object):
	"""docstring for Father"""
	def __init__(self, name):
		self._name = name
	def gamble(self):
		print('%s 在打麻将.' % self._name)
	def eat(self):
		print('%s 在大吃大喝.' % self._name)

class Monk(object):
	"""docstring for Monk"""
	def __init__(self, name):
		self._name = name
	def eat(self):
		print('%s 在吃斋.' % self._name)
	def chant(self):
		print('%s 在念经.' % self._name)

class Musician(object):
	"""docstring for Musician"""
	def __init__(self, name):
		self._name = name
	def eat(self):
		print('%s 在细嚼慢咽.' % self._name)
	def play_piano(self):
		print('%s 在弹钢琴.' % self._name)



class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):
# class Son(Father,Monk,Musician):
	"""docstring for Son"""
	def __init__(self, name):
		Father.__init__(self,name)
		Monk.__init__(self,name)
		Musician.__init__(self,name)


son = Son('王大锤')
son.gamble()

son.eat()
son.chant()
son.play_piano()



						