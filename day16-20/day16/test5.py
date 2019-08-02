#!/usr/bin/env python
# -*- coding: utf-8 -*-
# collections模块下的工具类
# 找出序列中出现次数最多的元素
# 穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
# 贪婪法 - 在对问题求解时，总是做出在当前看来
# 最好的选择，不追求最优解，快速找到满意解。
# 分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
# 回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
# 动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。
# @Date    : 2019-07-19 10:06:25
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from collections import Counter
words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
wod='look'
counter= Counter(wod)
print(counter.most_common(3))

