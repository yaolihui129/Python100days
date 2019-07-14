#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 21:45:54
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from abc import ABCMeta,abstractmethod

class Pet(object, metaclass=ABCMeta):
	"""docstring for Pet"""
	def __init__(self, nickname):
		self._nickname = nickname

	@abstractmethod
	def make_voice(self):
		pass

class Dog(Pet):
	"""docstring for Dog"""
	def make_voice(self):
		print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
	"""docstring for Cat"""
	def make_voice(self):
		print('%s: 喵..喵..喵..' % self._nickname)

def main():
	pets = [Dog('旺财'),Cat('凯蒂'),Dog('大黄')]
	for pet in pets:
		pet.make_voice()


if __name__ == '__main__':
	main()
