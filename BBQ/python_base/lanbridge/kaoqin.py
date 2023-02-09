'''

考勤打卡，就是排序问题
'''

import os
import sys

# 请在此输入您的代码
n = int(input())

ids = []
lis = []
for i in range(2 * n):
    ids.append(input().split())
    if ids[i] != []:
      lis.append(ids[i][1])


print(ids[1][1], list.sort(list(lis)))