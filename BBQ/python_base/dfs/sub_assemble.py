# @Time    : 2024/1/17 9:23
# 子集和 小明拥有一个大小为 N 集合 S，S 中的元素依次为 s1，s2，，，，sn
# 给出一个数 X，请你判断是否能从 S 中挑选任意个元素使得它们的和为 X

import os
import sys

# 请在此输入您的代码
# 把所有可能的和的值都求出来 这样肯定会超时
# 题目要求是折半查找 先用动态规划试一下

n, x = map(int, input().split())
s = [int(i) for i in input().split()]

# dp = [[False] * (x + 1) for _ in range(n + 1)]  # 一种固定用法 把 0 计算进去

# # 初始状态，空集合的和为0
# for i in range(n + 1):
#   dp[i][0] = True

# # 动态规划转移
# for i in range(1, n + 1):
#   for j in range(1, x + 1):
#     dp[i][j] = dp[i-1][j]
#     if j >= s[i-1]:
#       dp[i][j] |= dp[i-1][j - s[i-1]]

# res = dp[n][x]
# if res:
#   print('Y')
# else:
#   print('N')

# 回溯法
# github change test
def dfs(cur, sums):
  if cur == n:
    return sums == x
  if sums > x:
    return False
  if dfs(cur + 1, sums + s[cur]):
    return True
  if dfs(cur + 1, sums):
    return True
  return False

res = dfs(0, 0)
if res:
  print('Y')
else:
  print('N')