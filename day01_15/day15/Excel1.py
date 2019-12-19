#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 创建Excel文件
# @Date    : 2019-07-18 22:16:23
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from openpyxl import Workbook
from openpyxl.worksheet.table import Table,TableStyleInfo


workbook = Workbook()
sheet = workbook.active

data = [
	[1001,'白元芳','男','13123456789'],
	[1002,'白洁','女','13233445566']
]

sheet.append(['学号','姓名','性别','电话'])
for row in data:
	sheet.append(row)

tab = Table(displayName='Table1',ref="A1:E5")
tab.tableStyleInfo = TableStyleInfo(
	name = "TableStyleMedium9",showFirstColumn=False,
	showLastColumn=False,showRowStripes=True,showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./全班学生数据.xlsx')