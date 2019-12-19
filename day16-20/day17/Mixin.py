#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 混入（Mixin）

# 例子：自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。
# @Date    : 2019-07-21 09:35:08
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

class SetOnceMappingMiXin(object):
	"""docstring for SetOnceMappingMiXin"""
	__slots__ = ()
	def __setitem(self,key,value):
		if key in self:
			raise KeyError(str(key) + 'already set')
		return super().__setitem__(key,value)

class SetOnceDict(SetOnceMappingMiXin,dict):
	pass


my_dict = SetOnceDict()
try:
	my_dict['username'] = 'jackfrued'
	my_dict['username'] = 'hellokitty'
except KeyError:
	pass
print(my_dict)
