#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 从文本文件中读取数据
# @Date    : 2019-07-14 15:56:07
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

import time

filename = '致橡树.txt'

def main():
	# 一次性读取整个文件内容
	with open(filename,'r',encoding='utf-8') as f:
		print(f.read())
		f.close()
	# 通过for-in循环逐行读取
	with open(filename,mode='r') as f:
		for line in f:
			print(line,end=' ')
			time.sleep(0.5)
		f.close()
	# 读取文件按行读取到列表中
	with open(filename) as f:
		lines = f.readlines()
		f.close()
	print(lines)

if __name__ == '__main__':
	main()