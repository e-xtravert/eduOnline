'''
牛客dp39
有一个 n∗m 的矩形方阵，每个格子上面写了一个小写字母。
小红站在矩形的左上角，她每次可以向右或者向下走，走到某个格子上就可以收集这个格子的字母。
小红非常喜欢 "love" 这四个字母。她拿到一个 l 字母可以得 4 分，拿到一个 o 字母可以得 3 分，拿到一个 v 字母可以得 2 分，拿到一个 e 字母可以得 1 分。
她想知道，在最优的选择一条路径的情况下，她最多能获取多少分？

'''

import sys

n, m = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
map1 = []
for i in range(n):
    map1.append(input())


def score(char):
    if char == "l":
        return 4
    if char == "o":
        return 3
    if char == "v":
        return 2
    if char == "e":
        return 1
    return 0

for i in range(n):
    for j in range(0, m):
        dp[i + 1][j + 1] = max(dp[i][j + 1] + score(map1[i][j]), dp[i + 1][j] + score(map1[i][j]))

print(dp[n][m])
