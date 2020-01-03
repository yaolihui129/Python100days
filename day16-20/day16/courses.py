# ！ /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/3 15:12
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : courses.py
# @Version  : 0.1
# DESC      :嵌套的列表
# @Software : PyCharm
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)

scores = [[None]* len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
print(scores)


