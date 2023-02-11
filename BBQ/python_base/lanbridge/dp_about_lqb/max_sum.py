'''
最大和
小蓝在玩一个寻宝游戏, 游戏在一条笔直的道路上进行, 道路被分成了 nn 个方格, 依次编号 1 至 nn,
每个方格上都有一个宝物, 宝物的分值是一个整数 (包括正数、负数和零), 当进入一个方格时即获得方格中宝物的分值。
小蓝可 以获得的总分值是他从方格中获得的分值之和。
小蓝开始时站在方格 1 上并获得了方格 1 上宝物的分值, 他要经过若干步 到达方格 nn。
当小蓝站在方格 pp 上时, 他可以选择跳到 p+1p+1 到 p+D(n-p)p+D(n−p) 这些方格 中的一个,
其中 D(1)=1, D(x)(x>1)D(1)=1,D(x)(x>1) 定义为 xx 的最小质因数。
给定每个方格中宝物的分值, 请问小蓝能获得的最大总分值是多少。
输入格式
5

1 -2 -1 3 5
输出8
最优的跳跃方案为: 1 \rightarrow 3 \rightarrow 4 \rightarrow 51→3→4→5
'''

import os
import sys

# 请在此输入您的代码 没做出来，搜索类的算法还是不太行
n = int(input())
null = input()  # 空行
steps = list(map(int, input().split()))
# 奇数可以走两格，偶数位可以走一格
steps.append(0)
steps.append(0)
steps.append(0)
steps.append(0)
res = 0
for i in range(n):
    if i % 2 == 0:
        if res + steps[i] >= res and res + steps[i + 1] >= res:
            res = res + steps[i] + steps[i + 1]
            i += 3
        elif res + steps[i] >= res and res + steps[i + 1] < res:
            res = res + steps[i]
        if res + steps[i] < res and res + steps[i + 1] >= res:
            res = res + steps[i + 1]
            i += 3
        if res + steps[i] > res + steps[i + 1]:
            res += steps[i]
        if res + steps[i] < steps[i + 1]:
            res += steps[i + 1]
            i += 3

    else:
        res += steps[i]

print(0 % 2, n, steps, res)