#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串常用操作
# @Date    : 2019-07-14 16:45:09
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : $Id$

import pyperclip

#转义字符
print('My brother\'s name is \'007\'')

#原始字符
print(r'My brother\'s name is \'007\'')


str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和数字
print(str.isalnum())
# 字符串是否只包含数字
print(str.isdecimal())
print(str[0:5].isalpha())
print(str[5:8].isdecimal())


list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

print('-'.join(list))

sentence = 'You go your way I will go mine'
world_list = sentence.split()
print(world_list)
email = '     jackfrued@126.com          '
print(email)
#去除前后空格
print(email.strip())
#截取前边空格
print(email.lstrip())

# 将文本放入系统剪切板中
pyperclip.copy('老虎不发猫你当我病危呀')
# 从系统剪切板获得文本
print(pyperclip.paste())

