'''
题目描述
给定一棵包含 NN 个节点的完全二叉树，树上每个节点都有一个权值，按从 上到下、从左到右的顺序依次是 A_1, A_2, ··· A_NA
现在小明要把相同深度的节点的权值加在一起，他想知道哪个深度的节点 权值之和最大？如果有多个深度的权值和同为最大，请你输出其中最小的深度。

注：根的深度是 1。
有一个测试用例没有通过，感觉应该是重复权值那个但是不清楚
'''
import os
import sys
import math

# 请在此输入您的代码
num = int(input())
# 多行输入可以用循环一行一个input()，他这里一个数输入就得用一个input，不像是别的oj里面直接给全部的数
s = [int(i) for i in input().split()]
res = []
has = dict()
ans = []
floor = int(math.log((num + 1), 2))

for i in range(1, floor + 1):
    # print(i)
    time = int(math.pow(2, i - 1))
    end = int(math.pow(2, i))
    floor_sum = 0
    for j in range(time, end):
        floor_sum += s[j - 1]
        # print(floor_sum)

    ans.append(floor_sum)
    if floor_sum not in has:
        has[floor_sum] = i
    # print(has)

# print(max(ans))
# print(has)
print(has[int(max(ans))])
# another method print(ans.index(max(ans)) + 1)




