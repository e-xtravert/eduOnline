'''

'''

import os
import sys

# 思路不对，这是一个计算题，先找规律，多观察数据，拆开去分析，观察得知就是等差数列求和的问题

# 请在此输入您的代码
n = int(input())

# 一共k张卡片，总共有多少种

for i in range(n):
  if (1 + i) * i // 2 >= n:
    print(i)
    break
# def getn(n: int):
#     for i in range(2, n):
#         for j in range(i):
#             i = i * (i - 1)
#             if i < n:
#                 break
#         if i >= n:
#             return i
