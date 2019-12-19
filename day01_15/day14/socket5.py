#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用socketserver模块创建时间服务器
# @Date    : 2019-07-17 22:41:00
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socketserver import TCPServer,StreamRequestHandler
from time import *

class EchoRequestHandler(StreamRequestHandler):
	def handle(self):
		currtime = localtime(time())
		timestr = strftime('%Y-%m-%d %H:%M:%s',currtime)
		self.wfile.write(timestr.encode('utf-8'))

server = TCPServer(('127.0.0.1',6789),EchoRequestHandler)
server.serve_forever()
