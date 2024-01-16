# @Time    : 2024/1/16 15:58
# 反nim 需要判断必赢条件
import os
import sys

# 请在此输入您的代码

t = int(input())

for _ in range(t):
  n = int(input())
  a = [int(i) for i in input().split()]
  sm = 0
  ok = 0
  for i in a:
    if i > 1:  # 至少有一堆大于1
      ok = 1
    sm ^= i
  if ok == 1:
    if sm:
      print("NO")
    else:
      print('YES')
  else:
    if sm:
      print('YES')
    else:
      print('NO')
