#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取圆周率文件判断其中是否包含自己的生日
# @Date    : 2019-07-14 16:05:19
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

birth = input('请输入你的生日： ')
with open('pi_million_digits.txt') as f:
	lines =f.readlines()
	f.close()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()
	if birth in pi_string:
		print('Bingo!!!')
