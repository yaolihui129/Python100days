#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取CSV文件
# @Date    : 2019-07-14 15:03:00
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import csv

class Teacher(object):
	"""docstring for Teacher"""
	def __init__(self, name,age,title):
		self.__name = name
		self.__age = age
		self.__title = title
		self.__index = -1
	@property
	def name(self):
		return self.__name
	@property
	def age(self):
		return self.__age
	@property
	def title(self):
		return self.__title

filename = 'teacher.csv'
teachers = [Teacher('yaolh',35,'叫兽'), Teacher('狄仁杰', 25, '砖家')]

try:
	with open(filename,'w') as f:
		writer = csv.writer(f)
		for teacher in teachers:
			writer.writerow([teacher.name,teacher.age,teacher.title])
except BaseException as e:
	print('无法写入文件：',filename)
else:
	print('保存数据完成！')
finally:
    f.close()
	

