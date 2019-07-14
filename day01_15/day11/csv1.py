#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取CSV文件
# @Date    : 2019-07-14 14:55:30
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import csv

filename = 'example.csv'

try:
	with open(filename) as f:
		reader = csv.reader(f)
		data = list(reader)
		f.close()
except FileNotFoundError:
	print('无法打开文件',filename)
else:
	for item in data:
		print('%-30s%-20s%-10s' % (item[0],item[1],item[2]))