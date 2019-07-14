#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用tkinter创建GUI
# - 在窗口上制作动画
# @Date    : 2019-07-14 13:32:08
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import Tkinter
import time

# 播放动画效果的函数

def play_anination():
	canvas.move(oval,2,2)
	canvas.update()
	top.after(50,play_anination)

x = 10
y = 10
top = Tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False,False)
top.wm_attributes('-topmost',1)
canvas = Tkinter.Canvas(top,width=600,heigth=600,bd=0,highlightthickness=0)
canvas.create_rectangle(0,0,600,600,fill='gray')
oval = canvas.create_oval(10,10,60,fill='red')
canvas.pack()
top.update()
play_anination()
Tkinter.mainloop()
