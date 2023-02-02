'''
连续子数组最大和，找到一个递推式就可以了，很简单
'''




n = int(input())
lis = [int(i) for i in input().split()]
dp = [-100]*n
dp[0] = lis[0]
res = 0
# dp[i] = max(dp[i - 1] + lis[i], lis[i])

for i in range(1, n):
    dp[i] = max(dp[i - 1] + lis[i], lis[i])


print(max(dp))