#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-17 21:45:02
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socket import socket
from threading import Thread
def main():
	class ClientHandle(Thread):
		"""docstring for ClientHandle"""
		def __init__(self,client):
			super().__init__()
			self._client = client

		def run(self):
			try:
				while True:
					try:
						data = self._client.recv(1024)
						if data.decode('utf-8') == 'byebye':
							client.remove(self._client)
							self._client.close()
							break
						else:
							for client in clients:
								client.send(data)
					except Exception as e:
						print(e)
						client.remove(self._client)
						break
			except Exception as e:
				print(e)
	
	server = socket()
	server.bind(('127.0.0.1',12345))
	server.listen(512)
	client = []
	while True:
		curr_client,addr = server.accept()
		print(addr[0],'连接到服务器')
		client.append(curr_client)
		ClientHandle(curr_client).start()

if __name__ == '__main__':
	main()
