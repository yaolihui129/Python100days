#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
加密和解密
对称加密 - 加密和解密是同一个密钥 - DES / AES
非对称加密 - 加密和解密是不同的密钥 - RSA
pip install pycrypto
"""
# @Date    : 2019-07-29 18:03:00
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import base64
from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES加密的密钥（长度32个字节）
# key = md5(b'1qaz2wsx').hexdigest()
# # AES加密的初始向量（随机生成）
# iv = Random.new().read(AES.block_size)

def main():
	# 生成密钥对
	key_pair = RSA.generate(1024)
	# 导入公钥
	pub_key = RSA.importKey(key_pair.PublicKey().exportKey())
	# 导入私钥
	pri_key = RSA.importKey(key_pair.exportKey())
	message1 = 'hello,word!'
	# 加密数据
	data = pub_key.encrypt(message1.e)


if __name__ == '__main__':
	main()
