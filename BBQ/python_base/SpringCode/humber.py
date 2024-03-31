import sys

INF = 10 ** 17

# 函数作用
def solve():
    n, k, p = map(int, input().split())
    sty = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pre = [0] * (n + 1)
    dp = [0] * (n + 1)
    pos = [[] for _ in range(int(1e6 + 10))]

    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + a[i - 1]
        dp[i] = dp[i - 1]
        for j in pos[sty[i - 1]]:
            if i - j + 1 < p:
                continue
            dp[i] = max(dp[i], dp[j - 1] + pre[i] - pre[j - 1])
        pos[sty[i - 1]].append(i)
    print(dp[n])

#
sys.setrecursionlimit(10 ** 6)
solve()