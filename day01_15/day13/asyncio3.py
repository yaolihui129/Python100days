#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 异步I/O操作 - asyncio模块
# @Date    : 2019-07-15 22:37:00
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

import asyncio
async def wget(host):
	print('wget %s...' % host)
	connect =  asyncio.open_connection(host,80)
	# 异步方式等待连接结果
	reader,write = await connect
	hearer = 'GET / HTTP/1.0\r\nhost: %s\r\n\r\n' % host

	writer.write(hearer.encode('utf-8'))
	 # 异步I/O方式执行写操作
	await writer.drain()
	while True:
		# 异步I/O方式执行读操作
		line = await reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host,line.decofe('utf-8'.rstrip())))
	write.closs()

loop = asyncio.get_event_loop()
# 通过生成式语法创建一个装了三个协程的列表
hostsline = ['www.sina.com.cn','www.sohu.com','www.163.com']
tasks = [wget(host) for host in hostsline]
# 下面的方法将异步I/O操作放入EventLoop直到执行完毕
loop.run_until_complete(asyncio.wait(taslks))
loop.close()