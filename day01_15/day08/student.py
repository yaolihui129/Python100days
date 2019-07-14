#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义和使用学生类
# @Date    : 2019-07-13 11:58:19
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

def _foo():
	print('test')

class Student(object):
	# __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
	def __init__(self, name,age):
		self.name = name
		self.age  = age
	def study(self,course_name):
		print('%s正在学习%s.' % (self.name,course_name))
	# PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
	def watch_tv(self):
    	 if self.age < 18:
    		print('%s 只能观看《熊出没》。' % self.name)
    	 else:
    		print('%s 正在观看岛国大电影。' % self.name)



def main():
	stu1 = Student('yaolh',35)
	stu1.study('python程序设计')
	stu1.watch_tv()
	stu2 = Student('络络',1.5)
	stu2.study('思想品德')
	stu2.watch_tv()

if __name__ == '__main__':
	main()
