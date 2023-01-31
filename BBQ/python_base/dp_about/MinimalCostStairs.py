'''
给定一个整数数组 cost \cost  ，其中 cost[i]\cost[i]  是从楼梯第i \i 个台阶向上爬需要支付的费用，下标从0开始。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
'''

import sys
import math

# 只能向上爬一个或者两个台阶哦
# 某一个点的最小费用就是前一个最小费用再加上一个最小费用是当前的最小费用
num = int(input())

cost = [int(i) for i in input().split()]


# def min_cost(lis):
#     # 思考了几百年总算知道了，为什么这里要多一个0给dp
#     # 一直以为第一层也需要费用，但是题目说可以从下标为0台阶开始，也可以从下标为1台阶开始
#     # 那么台阶0和台阶1都是费用为0，不需要花费费用就可以到达
#     # 这么看来根据题目的设置，台阶数为0或1都是没意义的
#     dp = [0 for i in range(num + 1)]
#     for i in range(2, num + 1):

#         dp[i] = min(dp[i - 1] + lis[i - 1], dp[i - 2] + lis[i - 2])
#     # print(dp)
#     return dp[num]
# # print(num, cost)
# print(min_cost(cost))


# 还有一种就是用一个res保存最小费用的,因为这里面没有涉及很多状态
def min_cost(lis):
    floor1 = 0  # 第一层费用
    floor2 = 0  # 第二层费用
    floorn = 0  # 第n层费用，即要维护的最小值res
    for i in range(2, num + 1):
        floorn = min(floor2 + lis[i - 1], floor1 + lis[i - 2])
        floor1 = floor2  # 就是很简单的斐波那契数列动态规划做法，应该算是最简单的动态规划写法
        floor2 = floorn
    return floorn


print(min_cost(cost))
