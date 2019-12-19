#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 不良内容过滤
# @Date    : 2019-07-14 21:38:50
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import re

def main():
	sentence = '你丫是傻叉吗？我操你大爷的.Fuck you.'
	purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
	print(purified)

if __name__ == '__main__':
	main()