#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现进程间的通信
# @Date    : 2019-07-17 16:59:24
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import multiprocessing
import os

def sub_task(queue):
	print('子进程进程号：',os.getpgid())
	counter = 0
	while counter < 1000:
		queue.put('Pong')
		counter +=1

if __name__ == '__main__':
	print('当前进程号：',os.getpid())
	queue = multiprocessing.queues()
	p = multiprocessing.process(target=sub_task,args = (queue,))
	p.start()
	counter = 0
	while counter < 1000:
		queue.put('Ping')
		counter +=1
	p.jion()
	print('子任务已完成.')
	for _ in range(2000):
		print(queue.get(),end='')
