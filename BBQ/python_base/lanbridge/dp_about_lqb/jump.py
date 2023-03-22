'''
小蓝在一个 nn 行 mm 列的方格图中玩一个游戏。
开始时，小蓝站在方格图的左上角，即第 11 行第 11 列。
小蓝可以在方格图上走动，走动时，如果当前在第 rr 行第 cc 列，他不能走到行号比 rr 小的行，也不能走到列号比 cc 小的列。
同时，他一步走的直线距离不超过 33。
例如，如果当前小蓝在第 33 行第 55 列，他下一步可以走到第 33 行第 66 列、第 33 行第 77 列、第 33 行第 88 列、
第 44 行第 55 列、第 44 行第 66 列、第 44 行第 77 列、第 55 行第 55 列、第 55 行第 66 列、第 66 行第 55 列之一。
小蓝最终要走到第 nn 行第 mm 列。
在图中，有的位置有奖励，走上去即可获得，有的位置有惩罚，走上去就要接受惩罚。奖励和惩罚最终抽象成一个权值，奖励为正，惩罚为负。
小蓝希望，从第 11 行第 11 列走到第 nn 行第 mm 列后，总的权值和最大。请问最大是多少？

3 5
-4 -5 -10 -3 1
7 5 -9 3 -10
10 -2 6 -10 -4
'''

import os
import sys

# import numpy as np

# 请在此输入您的代码,他这里的机制是一行输入，使用一个input（）
# 用dp[i]表示当前最大的权值
# 蓝桥杯冲刺题目，组队赛 2023年3月22日11点37分
n, m = map(int, input().split())

# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]
# # 数组纵向合并？一闪而过的,可惜没有这个库， 但是你上面一行一行打印这种方式也太蠢了，
# 多在评论区看看人家的写法吧
# # s =  np.vstack((a, b, c))
# 这里的*是收集列表中多余的值，也是为了将map转成列表形式

map1 = [[*map(int, input().split())] for _ in range(n)]
# 还是用一个另外相似结构的数据结构来保存状态
# 多设几个数，是为了防止数组越界，会造成取值有误
# 这里为什么要设置一个很小的值，是因为在边界值会有负数，如果设成0，就会取0，而不是边界的实际值

dp = [[-100] * (m + 3) for i in range(n + 3)]
# for i, j in [(0, 1), (0, 2), (0, 3)]:
#   print(i, j) # 会输出0 1； 0 2这样的形式，应该是结构了
for i in range(n):
    for j in range(m):
        # if i - 3 < 0 or j - 3 < 0:
        #   dp[i][j] = 0
        # 其实可以直接写dp[0][0] = map1[0][0]
        # 目的是第一个值在取值时会从我们设置的dp里面找较大值，但是我们dp都是-100
        if i == 0 and j == 0:
            dp[i][j] = map1[i][j]
        else:
            dp[i][j] = map1[i][j] + max(dp[i - 1][j], dp[i - 2][j],
                                        dp[i - 3][j], dp[i - 2][j - 1], dp[i][j - 1], dp[i - 1][j - 2], dp[i][j - 3],
                                        dp[i][j - 2], dp[i - 1][j - 1])

# dp[i][j] = dp[i][j] + max(dp[i- 1][j], dp[i][j - 1])
print(dp[n - 1][m - 1])
