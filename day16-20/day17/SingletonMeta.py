#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用元类实现单例模式
# @Date    : 2019-07-21 18:18:17
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import threading
class SingletonMaeta(type):
	"""docstring for SingletonMaeta"""
	def __init__(cls, *args,**kwargs):
		cls.__instance = None
		cls.__lock = threading.Lock()
		super().__init__(*args,**kwargs)

	def __call__(cls,*args,**kwargs):
		if cls.__instance is None:
			with cls.__lock:
				if cls.__instance is None:
					cls.__instance = super().__call__(*args,**kwargs)
		return cls.__instance

class President(metaclass=SingletonMaeta):
	pass



'''
面向对象设计原则

单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息
说明：上面加粗的字母放在一起称为面向对象的SOLID原则。

GoF设计模式

创建型模式：单例、工厂、建造者、原型
结构型模式：适配器、门面（外观）、代理
行为型模式：迭代器、观察者、状态、策略

'''

