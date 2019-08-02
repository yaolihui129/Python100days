#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 不使用多线程的情况 - 耗时间的任务阻塞主事件循环
# @Date    : 2019-07-17 18:58:01
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import time
import tkinter
import tkinter.messagebox

def download():
	time.sleep(10)
	tkinter.messagebox.showinfo('提示','下载完成！')

def show_about():
	tkinter.messagebox.showinfo('关于','作者：yaolh')

def main():
	top = tkinter.Tk()
	top.geometry('200x150')
	top.wm_attributes('-topmost',True)

	panel = tkinter.Frame(top)
	button1 =tkinter.Button(panel,text='下载',command=download)
	button1.pack(side='left')
	button1 =tkinter.Button(panel,text='关于',command= show_about)
	button1.pack(side='right')
	panel.pack(side='bottom')

	tkinter.mainloop()

if __name__ == '__main__':
	main()


# 在不使用多线程的情况下 一旦点击下载按钮 由于该操作需要花费10秒中的时间
# 整个主消息循环也会被阻塞10秒钟无法响应其他的事件
# 事实上 对于没有因果关系的子任务 这种顺序执行的方式并不合理


