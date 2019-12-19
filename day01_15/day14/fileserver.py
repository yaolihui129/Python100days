#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-17 22:14:57
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode
from json import dumps
def main():
	#自定义线程类
	class FileTransferHandler(Thread):
		"""docstring for FileTransferHandler"""
		def __init__(self, cclient):
			super().__init__()
			self.cclient = cclient
		def runnrt(self):
			my_dict = {}
			my_dict['filename'] = 'guido.jpg'
			# JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            
			
