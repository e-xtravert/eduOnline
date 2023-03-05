'''
ALGO-981过河马
看了一下题解，说使用动态规划
但是结果不对，应该还需要优化
'''

n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(m + 1)]
dp[3][2] = 1
dp[2][3] = 1
for i in range(3, m):
    for j in range(1, n + 1):
        if j - 2 >= 1:
            dp[i][j] = dp[i][j - 2] + dp[i][j]
        if j - 1 >= 1:
            dp[i][j] += dp[i][j - 1]
        if i + 1 <= m and j - 2 >= 1:
            dp[i][j] += dp[i + 1][j - 2]
        if i + 2 <= m and j - 1 >= 1:
            dp[i][j] += dp[i + 2][j - 1]
        else:
            continue

print(n, m, dp)
