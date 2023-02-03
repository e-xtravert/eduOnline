'''


'''



n, V = map(int, input().split())

for i in range(n):
    package = list(map(int, input().split()))

# dp[i] = max(dp[i], dp[i - v[i]] + w[i])



print(n, V)

