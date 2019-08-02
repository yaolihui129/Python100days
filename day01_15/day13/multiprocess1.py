#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用Process类创建多个进程
# @Date    : 2019-07-17 16:28:40
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$


# 通过下面程序的执行结果可以证实 父进程在创建子进程时复制了进程及其数据结构
# 每个进程都有自己独立的内存空间 所以进程之间共享数据只能通过IPC的方式
from multiprocessing import Process,Queue
from time import sleep

def sub_task(string,q):
	number = q.get()
	while number:
		print('%d:%s' % (number,string))
		sleep(0.001)
		number =q.get()

def main():
	q = Queue(10)
	for number in range(1,11):
		q.put(number)
	Process(target=sub_task,args=('Ping',q)).start()
	Process(target=sub_task,args=('Pong',q)).start()

if __name__ == '__main__':
	main()
