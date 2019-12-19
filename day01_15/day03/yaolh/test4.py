#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:11
# @Author  : yaolh(yaolh@yonyou.com)
# @File    : test4.py
# @Version : 0.1
# @DESC    :  英制单位英寸和公制单位厘米互换
# @Software: PyCharm

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')