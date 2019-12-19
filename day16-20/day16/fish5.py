#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 五人分鱼
# # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
# @Date    : 2019-07-19 10:12:52
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

fish = 6
while True:
	total = fish
	enough = True
	for _ in range(5):
		if (total - 1) % 5 == 0:
			total = (total - 1) // 5 * 4
		else:
			enough = False
			break
	if enough:
		print(fish)
	fish += 5
