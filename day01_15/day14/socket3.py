#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 套接字 - 基于UDP协议Echo服务器
# @Date    : 2019-07-17 22:40:17
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1
# 


from socket import *
from time import *
server = socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',6789))
while True:
	data,addr = server.recvfrom(1024)
	server.sendto(data,addr)

server.close()

