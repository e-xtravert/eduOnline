'''
砝码称重 蓝桥杯训历年真题
输入
3
1 4 6
输出
10
'''

# 乍一看没思路，想法是把所有数两两相加减，三三相加减，减的话大于0，只要是结果集中没出现的就+1，不好处理的地方在于几个数相加减不好整
# 看了一下网上的答案，用的是动态规划，还真没想到，确实挺牛

n = int(input())
weights = [int(i) for i in input().split()]
weights.sort(reverse=True)
weights = [0] + weights

dp = [[0] * (sum(weights) + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(sum(weights)):  # 遍历最大和里面的数，有多少是可以得到的
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            dp[i][j + weights[i]] = 1  # weights是砝码重量，j是当前重量
            if j > weights[i]:
                dp[i][j - weights[i]] = 1

print(sum(dp[n]) - 1)
