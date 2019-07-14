#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 写文本文件
# 将100以内的素数写入到文件中
# @Date    : 2019-07-14 16:13:22
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from math import sqrt

def is_prime(n):
	for factor in range(2,int(sqrt(n)) + 1):
		if n % factor == 0:
			return False
	return True

# with open('prime.txt','a') as f:
with open('prime.txt','w') as f:
	for num in range(2,100):
		if is_prime(num):
			f.write(str(num)+ '\n')

f.close()
print('写入完成！')
