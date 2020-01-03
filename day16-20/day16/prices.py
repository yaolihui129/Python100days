# ！ /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/3 15:09
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : prices.py
# @Version  : 0.1
# DESC      : 使用生成式（推导式）语法
# @Software : PyCharm

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典

prices2 = {key:value for key,value in prices.items() if value >100}
print(prices2)


