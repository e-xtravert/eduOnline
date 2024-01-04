# @Time    : 2024/1/4 13:32
# 01背包
import os
import sys

# 请在此输入您的代码
n, v = map(int, input().split())
dp = [[0] * (v + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  vi, wi = map(int, input().split())
  for j in range(v + 1):
    if j >= vi:
      dp[i][j] = max(dp[i - 1][j - vi] + wi, dp[i - 1][j])  # 不选择或是选择
    else:
      dp[i][j] = dp[i - 1][j]  # 选择不了

print(dp[n][v])

# 上面的结果需要从0开始判断背包的容量
N, V = map(int, input().split())
dp = [0]*(V+1)
for _ in range(N):
  w, v = map(int, input().split())
  for j in reversed(range(w,V+1)):  # 从后往前覆盖
    dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])