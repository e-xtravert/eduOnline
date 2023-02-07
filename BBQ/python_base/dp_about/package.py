'''

牛客dp41，背包问题
'''

n, V = map(int, input().split())
# map1 = [ [ *map(int, input().split())] for _ in range(n)]
v, w = [], []
for i in range(n):
    lis = list(map(int, input().split()))
    v.append(lis[1])
    w.append(lis[0])



# dp = [[0] * (V + 1) for i in range(n)]
dp0 = [0 for i in range(V + 1)]
dp1 = [float('-inf') for _ in range(V + 1)]
dp1[0] = 0
for i in range(n):
    for j in range(V, w[i] - 1, -1):
        dp0[j] = max(dp0[j], dp0[j - w[i]] + v[i])
        dp1[j] = max(dp1[j], dp1[j - w[i]] + v[i])

print(dp0[-1])
print(dp1[-1] if dp1[-1] != float('-inf') else 0)
# dp[i] = max(dp[i - 1], dp[V - v[i]] + w[i])，当背包恰好装满就多一个i <= 容量的条件就行了呗？
# 为什么这样不行，因为i原本只表示状态，不表示其他含义，上面这样写需要复杂一点操作，还需要对V-v[i]进行判断，不如用下面的dp,表示第i个物品放与不放和背包容量为j时的状态
# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]),
# 选dp数组，初始化，双循环设置,一个遍历背包，一个遍历物品

# for i in range(n):
#     for j in range(V, -1, -1):
#         if j - w[i] >= 0:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
#         else:
#             dp[i][j] = dp[i - 1][j]
# print(n, V, v, w, dp0, dp1)