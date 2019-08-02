#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 套接字 - 基于TCP协议创建时间服务器
# @Date    : 2019-07-17 22:25:42
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socket import *
from time import *
server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',6789))
server.listen()
print('服务器已经启动正在监听客户连接.')
while True:
	client,addr = server._accept()
	print('客户端%s:%d连接成功.' % (addr[0],addr[1]))
	currtime = localtime(time())
	timestr = strftime('%Y-%m-%d %H:%M:%S',currtime)
	client.send(timestr.encode('utf-8'))
	client.close()
server.close()
