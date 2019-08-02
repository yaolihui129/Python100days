#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用多进程和不使用多进程到底有什么差别
# @Date    : 2019-07-15 16:36:30
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from random import randint
from time import time,sleep


def download_task(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s 下载完成！耗费了%d秒' % (filename,time_to_download))

def main():
	start = time()
	download_task('Pytthon从入门到住院.pdf')
	download_task('Peking Hot.avi')
	end = time()
	print('总共耗费了%.2f 秒' % (end - start))

if __name__ == '__main__':
	main()
