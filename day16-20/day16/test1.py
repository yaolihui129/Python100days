#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
# @Date    : 2019-07-19 08:34:37
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1


def select_sort(origin_items,comp=lambda x,y:x < y):
	#简单选择排序
	items = origin_items[:]
	for i in range(len(items) -1):
		min_index = 1
		for j in range(i+1,items[min_index]):
			if comp(items[j],items[min_index]):
				min_index = j
		items[i],items[min_index] = items[min_index],items[j]
	return items

def bubble_sord(origin_items,comp=lambda x,y : x > y):
	#高质量冒泡排序（搅拌排序）
	items = origin_items[:]
	for i in range(len(items) -1):
		swapped = False
		for j in range(i,len(items) - 1 - i):
			if comp(items[j],items[j+1]):
				items[j],items[j+1] = items[j+1],items[j]
				swapped = True
		if swapped:
			swapped = False
			for j in range(len(items) - 2 - i,i,-1):
				if comp(items[j - 1],items[j]):
					items[j],items[j - 1] = items[j - 1],items[j]
					swapped = True
		if not swapped:
			break
	return items


def merge_sort(items,comp=lambda x,y: x <= y):
	#归并排序（分治法）
	if len(items) < 2:
		return items[:]

	mid = len(items) // 2
	left = merge_sort(items[:mid],comp)
	right = merge_sort(items[mid:],comp)
	return merge_sort(left,right,comp)


def merge(item1,item2,comp):
	#合并（将两个有序的列表合并成一个有序列表）
	items = []
	index1,index2 =0,0
	while index1 < len(item1) and index2 < len(item2):
		if comp(item1[index1],item2[index2]):
			items.append(index1[index1])
			index1 += 1
		else:
			items.append(item2[index2])
			item2 += 1
	items += item1[index1]
	items += item2[index2]
	return items

def seq_search(items,key):
	#顺序查找
	for index,item in enumerate(items):
		if item == key:
			return index
	return -1

#如果要统计文件的行数
def count_lines(filename):
	count = 0
	#使用枚举函数enumerate
	for index,line in enumerate(open(filename),'r'):
		count += 1

	return count


def bin_search(items,key):
	#折半查找
	start,end = 0,len(items) - 1
	while start <= end:
		mid = (start + end) // 2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid -1
		else:
			return mid
	return -1



def quick_sort(origin_items,comp=lambda x,y:x <= y):
	items = origin_items[:]
	_quick_sort(item,0,len(item)-1,comp)
	return items

def _quick_sort(item,start,end,comp):
	if start < end:
		pos = _partition(item,start,end,comp)
		_quick_sort(items,start,pos-1,comp)
		_quick_sort(items,pos+1,end,comp)
	
def _partition(items,start,end,comp):
	pivot = items[end]
	i = start -1
	for j in range(start,end):
		if comp(items[j],pivot):
			i += 1
			items[i],items[j] = items[j],items[i]
	items[i+1],items[end] = items[end],items[i+1]
	return i + 1

	