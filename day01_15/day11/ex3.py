#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 异常机制 - 处理程序在运行时可能发生的状态
# @Date    : 2019-07-14 15:22:01
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import time
import sys

filename = input('请输入文件名： ')
try:
	with open(filename) as f:
		lines =f.readlines()
except FileNotFoundError as msg:
	print('无法打开文件',filename)
	print(msg)
except UnicodeDecodeError as msg:
	print('非文本无法解析')
	sys.exit()
else:
	for line in lines:
		print(line.rstrip())
		time.sleep(0.5)
finally:
	# 此处最适合做善后工作
	print('不管发生什么我都会执行')
	f.close()

