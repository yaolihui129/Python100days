#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将这个任务分解到8个进程中去执行的时候
# @Date    : 2019-07-15 18:01:23
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from multiprocessing import process,queues
from random import randint
from time import time

def task_handler(curr_list,result_queue):
	total = 0
	for number in curr_list:
		total += number
	result_queue.put(total)

def main():
	processes = []
	number_list = [x for x in range(1,100000001)]
	result_queue =queues()
	index = 0
	# 启动8个进程将数据切片后进行运算
	for _ in range(8):
		p = process(target=task_handler,args=(number_list[index:index + 12500000],result_queue))
		index += 12500000
		processes.append(p)
		p.start()
	# 开始记录所有进程执行完成花费的时间
	start = time()
	for p in processes:
		p.jion()
	#合并执行结果
	total = 0
	while not result_queue.empty():
		total += result_queue.get()
	print(total)
	end = time()
	print('Execution time: ',(end - start), 's',sep='')

if __name__ == '__main__':
	main()