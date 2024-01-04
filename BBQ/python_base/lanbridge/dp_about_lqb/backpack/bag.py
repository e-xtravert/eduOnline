# @Time    : 2024/1/4 13:32
# 01背包 物品只有一个 放还是不放
import os
import sys

# 请在此输入您的代码
n, v = map(int, input().split())
dp = [[0] * (v + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  vi, wi = map(int, input().split())
  for j in range(v + 1):
    if j >= vi:  # 如果用正序注意这个条件
      dp[i][j] = max(dp[i - 1][j - vi] + wi, dp[i - 1][j])  # 不选择或是选择
    else:
      dp[i][j] = dp[i - 1][j]  # 选择不了 和上一个物品的状态是一样的

print(dp[n][v])

# 上面的结果需要从0开始判断背包的容量
N, V = map(int, input().split())
dp = [0]*(V+1)
for _ in range(N):
  w, v = map(int, input().split())
  for j in reversed(range(w,V+1)):  # 从后往前覆盖
    dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])

# 完全背包问题
# 修改第一种判断条件的方式解决完全背包问题
n, v = map(int, input().split())
dp = [[0] * (v + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  vi, wi = map(int, input().split())
  for j in range(v + 1):
    if j >= vi:  # 如果用正序注意这个条件
      dp[i][j] = max(dp[i][j - vi] + wi, dp[i - 1][j])  # 选择在前一种的状态下 可以重复选
    else:
      dp[i][j] = dp[i - 1][j]  # 选择不了 和上一个物品的状态是一样的

print(dp[n][v])

# 修改上述逆序的方式为正序的方式可以解决 完全背包问题 物品数量不限制
N, V = map(int, input().split())
dp = [0]*(V+1)
for _ in range(N):
  w, v = map(int, input().split())
  for j in range(w, V+1):  # 区别在这里 这样会将重复的商品添加进去
    dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])

# 多重背包问题 就是说物品的数量是有限制的
import os
import sys

# 请在此输入您的代码
N, V = map(int, input().split())
dp = [[0] * (V + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    # 体积、价值、数量
    wi, vi, si = map(int, input().split())
    for j in range(1, V + 1):
        for k in range(0, si + 1):
            if j >= k * wi:  # 这里直接判断全部的重量就好了
                # 下面为什么不用dp[i - 1][j] 而是直接dp[i][j]先记住 后面做多了再理解
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * wi] + k * vi)

print(dp[N][V])


# 物品有无限多个情况 当si=0表示无限多的情况
import os
import sys

# 请在此输入您的代码
#一维数组表示:
n,v=map(int,input().split())
wd=[]
for i in range(n):
  wd.append(list(map(int,input().split())))
fd=[0]*(v+1)
for a in range(1,n+1):
  for b in range(v,-1,-1):
    if wd[a-1][2]==0:
      count=b//wd[a-1][0]
    else:
      count=min(b//wd[a-1][0],wd[a-1][2])
    fd[b]=max([fd[b-i*wd[a-1][0]]+wd[a-1][1]*i for i in range(count+1)])
print(fd[-1])




