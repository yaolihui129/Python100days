#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取JSON数据
# @Date    : 2019-07-14 16:27:27
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import json
import csv2

json_str ='{"name":"yaolh","age":35,"title":"叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# 把转换得到的字典作为关键字参数传入Teacher的构造器
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)
