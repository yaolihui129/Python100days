#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用多进程对复杂任务进行“分而治之”。
# @Date    : 2019-07-15 17:17:02
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from time import time
def main():
	total = 0
	number_list = [x for x in range(1,10000001)]
	start = time()
	for num in number_list:
		total += num
	print(total)
	end = time()
	print('Execution time: %.3fs' % (end - start))

if __name__ == '__main__':
	main()
