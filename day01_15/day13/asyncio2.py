#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 异步I/O操作 - async和await
# @Date    : 2019-07-15 22:30:33
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import asyncio
import threading

# 通过async修饰的函数不再是普通函数而是一个协程
# 注意async和await将在Python 3.7中作为关键字出现
async def hello():
	print('%s: hello,word!' % threading.current_thread())
	await asyncio.sleep(2)
	print('%s: goodbye,word!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()