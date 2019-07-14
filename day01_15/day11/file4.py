#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读写二进制文件
# @Date    : 2019-07-14 16:20:59
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import base64

with open('mm.jpg','rb') as f:
	data = f.read()
	f.close()
	print('字节数：',len(data))
	# 将图片处理成BASE-64编码
	print(base64.b64encode(data))

with open('girl.jpg','wb') as f:
	f.write(data)

f.close()
print('写入完成！')
