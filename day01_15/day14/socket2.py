#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 套接字 - 基于TCP协议创建时间客户端
# @Date    : 2019-07-17 22:40:03
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socket import *
client = socket(AF_INET,SOCK_STREAM)
client.connect(('128.0.0.1',6789))
while True:
	data = client.recv(1024)
	if not data:
		break
	print(data.decode('utf-8'))
	client.close()
