#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 不使用多线程的情况 - 模拟多个下载任务
# @Date    : 2019-07-17 18:52:40
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from random import randint
from time import time,sleep

def download_task(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('下载完成！耗费了%d 秒' % time_to_download)

def main():
	start = time()
	download_task('1')
	download_task('2')
	end = time()
	print('总共耗费了%.2f 秒' % (end -start))

if __name__ == '__main__':
	main()
