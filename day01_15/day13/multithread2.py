#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用多线程的情况 - 模拟多个下载任务
# @Date    : 2019-07-17 18:10:44
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

from random import randint
from threading import Thread
from time import time,sleep

def download_task(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s下载完成！耗费了%d 秒' % (filename,time_to_download))

def main():
	start = time()
	thread1 = Thread(target=download_task,args=('Python 从入门到住院.pdf'))
	thread1.start()
	thread2 = Thread(target=download_task,args=('Peking Hot.avi'))
	thread2.start()
	thread1.jion()
	thread2.jion()
	end = time()
	print('总共耗费了%.3f秒' % (end -start))

if __name__ == '__main__':
		main()