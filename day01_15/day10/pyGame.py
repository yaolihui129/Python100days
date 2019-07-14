# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 23:04:07
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

import pyGame

def main():
	pyGame.init()
	screen = pyGame.display.set_mod((800,600))
	pyGame.display.ser_caption('大球吃小球')
	running = True
	while running:
		for event in pyGame.event.get():
			if event.type == pyGame.QUIT:
				running = False

if __name__ == '__main__':
	main()
