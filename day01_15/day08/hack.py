#!/usr/bin/env python
# -*- coding: utf-8 -*
# 另一种创建类的方式
# @Date    : 2019-07-13 11:23:21
# @Author  : yaolh
# @Link    : http://example.org
# @Version : 0.1

def bar(self,name):
	self._name = name


def foo(self,course_name):
	print('%s 正在学习%s' % (self._name,course_name))

def main():
	Student = type('Student',(object,),dict(__init__=bar,study=foo))
	stu1 =Student('yaolh')
	stu1.study('Python 程序设计')

if __name__ == '__main__':
	main()
