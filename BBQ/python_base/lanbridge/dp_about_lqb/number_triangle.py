'''
从三角形的顶部到底部有很多条不同的路径。对于每条路径，把路径上面的数加起来可以得到一个和，你的任务就是找到最大的和。
input：
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
output：
27
'''

import os
import sys

# 请在此输入您的代码  蓝桥杯训练赛冲刺题 也有这道 2023年3月22日11点20分
inp = int(input())

map1 = [[*map(int, input().split())] for _ in range(inp)]
dp = [[0]*(len(map1[inp - 1]) + 2) for _ in range(inp + 1)]
# dp[i][j] = map1[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j + 1])
res = 0

for i in range(inp):
    for j in range(1, len(map1[inp - 1]) - len(map1[i]) + 1):
        map1[i].append(0)
# 判断条件“向左下走的次数与向右下走的次数相差不能超过 1”的方法是
# 当前数据下标值和最顶层数据下标值必须有一个 <= 1，画图可以找出规律
# 最顶层下标就为(0, 0)吧,看人家的代码原来还有规律
# 如果是奇数行只能是最后一行最中间的值,偶数行是中间两个值,我说怎么这么奇怪

for i in range(1, inp + 1):
    for j in range(1, len(map1[inp - 1]) + 1):
        dp[i][j] = map1[i - 1][j - 1] + max(dp[i - 1][j], dp[i - 1][j - 1])


# 奇数行是最中间那个数，偶数行是中间两个数里面的较大值
size = int(len(dp[inp])/2)
if inp % 2 == 0:
    res = max(dp[inp][size - 1], dp[inp][size + 1])
if inp % 2 == 1:
    res = dp[inp][int(size + 0.5)]
print(inp, map1[4][4], res)
