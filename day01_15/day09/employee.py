#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 抽象类 / 方法重写 / 多态
# 实现一个工资结算系统 公司有三种类型的员工
# - 部门经理固定月薪12000元/月
# - 程序员按本月工作小时数每小时100元
# - 销售员1500元/月的底薪加上本月销售额5%的提成
# 输入员工的信息 输出每位员工的月薪信息
# @Date    : 2019-07-13 19:57:07
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
	"""docstring for Employee"""
	def __init__(self, name):
		self._name = name
	@property
	def name(self):
		return self._name
	@abstractmethod
	def get_salary(self):
		pass

class Manager(Employee):
	"""docstring for Manager"""
	def __init__(self, name):
		super().__init__(name)
	def get_salary(self):
		return 12000

class Programer(Employee):
	"""docstring for Programer"""
	def __init__(self, name):
		super(self).__init__(name)

	def set_working_hour(self,working_hour):
		self._working_hour = working_hour

	def get_salary(self):
		return 100 * self._working_hour

class Salesman(Employee):
	"""docstring for Salesman"""
	def __init__(self, name):
		super().__init__(name)
	def set_sales(self,sales):
		self._sales = sales

	def get_salary(self):
		return 1500 + self._sales * 0.05
if __name__ == '__main__':
	emps = [Manager('武则天'),Programer('狄仁杰'),Salesman('白元芳')]
	for emp in emps:
		if isinstance(emp,Programer):
			working_hour = int(input('请输入%s 本月工作时间： ' % emp.name))
			emps.set_working_hour(working_hour)
		elif isinstance(emp,Salesman):
			sales = float(input('请输入%s本月销售额： ' % emp.name))
			emp.set_sales(sales)
		print('%s 本月月薪为：￥%.2f 元' % (emp.name,emp.get_salary()))


