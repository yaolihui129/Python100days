#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 09:18:38
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1


prices ={
	'AAPL':191.88,
	'GOOG':1186.96,
	'IBM':149.24,
	'ORCL':48.44,
	'ACN':166.89,
	'FB':208.09,
	'SYMC':21.29
}
prices2 = {key:value for key,value in prices.items() if value >100}
print(prices2)


names = ['关羽','张飞','赵云','马超','黄忠']
courses = ['语文','数学','英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)sc
scores = [[None]*len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
	for col,course in enumerate(courses):
		scores[row][col] = float(input(f'请输入{name}的{course}成绩:'))

print(scores)
