#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用subprocess模块中的类和函数来创建和启动子进程
# @Date    : 2019-07-15 16:52:10
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from multiprocessing import Process
from time import sleep

def sub_task(string):
	global counter
	while counter < 10:
		print(string,end='',flush=True)
		counter += 1
		sleep(0.01)

def main():
	Process(target=sub_task, args=('Ping',)).start()
	Process(target=sub_task, args=('Pong',)).start()

if __name__ == '__main__':
	main()

