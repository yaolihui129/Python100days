#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heapq、itertools等的用法
# 从列表中找出最大的或最小的N个元素
# 堆结构(大根堆/小根堆)
# @Date    : 2019-07-19 09:45:59
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

import heapq
list1 = [24,25,12,99,87,63,58,88,92]
list2 = [
	{'name':'IBM','shares':100,'price':91.1},
	{'name':'AAPL','shares':50,'price':543.22},
	{'name':'FB','shares':200,'price':21.29},
	{'name':'HPQ','shares':35,'price':31.75},
	{'name':'YHOO','shares':45,'price':16.35},
	{'name':'ACME','shares':75,'price':115.65},
]

#打印最大的三个
print(heapq.nlargest(3,list1))
#打印最小的 3 个
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2,key=lambda x:x['shares']))
print(heapq.nlargest(2,list2,key=lambda x:x['price']))



