'''
给一个节点数n， 输出有多少个二叉树搭配
'''


# 这题有点不太懂
inp = int(input())

dp = [0] * (inp + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, inp + 1):
    for j in range(1, i + 1):
        dp[i] += dp[j - 1] * dp[i - j]

print(dp[inp])