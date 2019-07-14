#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 写入JSON文件
# @Date    : 2019-07-14 16:36:24
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import json

teacher_dict = {'name':'白元芳','age':25,'title':'讲师'}
json_str =json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple','orange','strawberry','banana','pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))