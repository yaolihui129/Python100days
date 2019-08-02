#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-15 16:59:14
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from random import randint
from threading import Thread
from time import time,sleep

def download_task(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s 下载完成！耗费了%d秒' % (filename,time_to_download))



def main():
	start = time()
	t1 = Thread(target=download_task,args=('Python 从入门到住院.pdf',))
	t1.start()
	t2 = Thread(target=download_task,args=('Peking Hot.avi',))
	t2.start()
	t1.jion()
	t2.jion()
	end = time()
	print('总共耗费了%.3f 秒' % (end - start))

if __name__ == '__main__':
	main()