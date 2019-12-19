#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:12
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test5.py
# @Version : 0.1
# @DESC    :  掷骰子决定做什么
# @Software: PyCharm

from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)