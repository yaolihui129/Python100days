# ！ /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/3 15:54
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : collect.py
# @Version  : 0.1
# DESC      :collections模块下的工具类
# @Software : PyCharm

"""
找出序列中出现次数最多的元素
"""
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

