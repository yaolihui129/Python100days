#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:12
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test6.py
# @Version : 0.1
# @DESC    :  百分制成绩转等级制
# 90分以上    --> A
# 80分~89分    --> B
# 70分~79分	   --> C
# 60分~69分    --> D
# 60分以下    --> E
# @Software: PyCharm

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)