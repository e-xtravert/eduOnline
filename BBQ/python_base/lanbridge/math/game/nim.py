# @Time    : 2024/1/16 15:57
# nim
import os
import sys

# 请在此输入您的代码
t=int(input())
for _ in range(t):
    n=int(input())
    test=list(map(int,input().split()))
    sum1=0
    for i in test:
        sum1^=i
    if not sum1:#异或和为0，后手胜利；
        print('YES')
    else:#异或和不为0，先手胜利
        print('NO')

