# ！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/19 18:38
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : test1.py
# @Version  : 0.1
# DESC      : 输入M和N计算C(M,N)
# @Software : PyCharm

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)


