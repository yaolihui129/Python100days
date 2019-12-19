#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-17 20:11:54
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socket import socket
from threading import Thread


def main():
	class RefreshScreenThread(Thread):
		"""docstring for RefreshScreenThread"""
		def __init__(self, client):
			super().__init__()
			self._client = client
			
		def run(self):
			while running:
				data = self._client.recv(1024)
				print(data.decode('utf-8'))

	nickname = input('请输入你的昵称： ')
	myclient = socket()
	myclient.connect(('127.0.0.1',12345))
	running = True
	RefreshScreenThread(myclient).start()
	while running:
		connect = input('请发言： ')
		if connect == 'byebye':
			myclient.send(connect.encode('utf-8'))
			running =False
		else:
			msg = nickname + ':'+ connect
			myclient.send(msg.encode('utf-8'))

if __name__ == '__main__':
	main()