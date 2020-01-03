# ！ /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/3 14:57
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : sort.py
# @Version  : 0.1
# DESC      :排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
# @Software : PyCharm

def select_sort(origin_items,comp=lambda x,y :x<y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index=j
        items[i],items[min_index] = items[i],items[min_index]
    return items


items=[4,78,65,897,65,876,98]
print(select_sort(items))
