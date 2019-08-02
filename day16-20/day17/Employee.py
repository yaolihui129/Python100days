#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
# @Date    : 2019-07-21 08:23:23
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
	"""docstring for Employee"""
	def __init__(self, name):
		self.name = name

	@abstractmethod
	def get_sarlary(self):
		pass

class Manager(Employee):
	"""docstring for Manager"""
	def get_sarlary(self):
		return 15000.00

class Programmer(Employee):
	"""docstring for Programmer"""
	def __init__(self,name,working_hour=0):
		self.working_hour = working_hour
		super().__init__(name)
	
	def get_sarlary(self):
		return 200.0 * self.working_hour


class Salesman(Employee):
	"""docstring for Salesman"""
	def __init__(self, name,sales=0.0):
		super().__init__(name)
		self.sales = sales
	
	def get_sarlary(self):
		return 1800.0 + self.sales * 0.05


class EmployeeFactory():
	"""创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
	@staticmethod
	def create(emp_type, *args,**kwargs):
		emp_type = emp_type.upper()
		emp = None
		if emp_type == 'M':
			emp = Manager(*args,**kwargs)
		elif emp_type == 'P':
			emp = Programmer(*args,**kwargs)
		elif emp_type == 'S':
			emp = Salesman(*args,**kwargs)
		return emp


def main():
	emps = [
		EmployeeFactory.create('M','曹操'),
		EmployeeFactory.create('P','荀彧',120),
		EmployeeFactory.create('P','郭嘉',85),
		EmployeeFactory.create('S','典韦',123000),
	]
	for emp in emps:
		print('%s:%.2f 元' % (emp.name,emp.get_sarlary()))


if __name__ == '__main__':
	main()
		

