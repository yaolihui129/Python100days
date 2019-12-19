#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 可插拔的哈希算法
# @Date    : 2019-07-21 18:25:29
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

class StreamHasher(object):
	"""哈希摘要生成器(策略模式)"""
	def __init__(self, alg='md5',size=4096):
		self.size = size
		alg= alg.lower()
		self.hasher = getattr(__import__('hashlib'),alg.lower())()
	def __call__(self,stream):
		return self.to_digest(stream)

	def to_digest(self,stream):
		"""生成十六进制形式的摘要"""
		for buf in iter(lambda:stream.read(self.size),b''):
			self.hasher.update(buf)
		return self.hasher.hexdigest()

def main():
	hasher1 = StreamHasher()
	with open('Python-3.7.1.tgz','rb') as stream:
		print(hasher1.to_digest(stream))
	hasher2 = StreamHasher('sha1')
	with open('Python-3.7.1.tgz','rb') as stream:
		print(hasher2(stream))

if __name__ == '__main__':
	main()

