#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取PDF文件
# @Date    : 2019-07-18 22:45:27
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from PyPDF2 import PdfFileReader

with open('./res/Docker入门教程.pdf','rb') as f:
	reader = PdfFileReader(f,strict=False)
	print(reader.numPages)
	if reader.isEncrypted:
		reader.decrypy(' ')
	current_page = reader.getPage(5)
	print(current_page)
	print(current_page.extractTexts())

