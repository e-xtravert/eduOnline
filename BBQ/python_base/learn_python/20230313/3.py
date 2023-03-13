'''
有多少个优雅数组
'''
from random import random
n, k = map(int, input().split())
lis = [int(i) for i in input().split()]
res = 0
has = dict()
# 把所有的子数组都枚举出来，然后再计算
arr_ = [[] for _ in range(n * (n - 1) * 2)]

# for i in range(n - 1):


def c(arr, h):
    global res
    for i in range(len(arr)):
        if arr[i] in has:
            h[arr[i]] += 1
        else:
            h[arr[i]] = 1

    for j in h:
        if h[j] >= 3:
            res += 1

    return res


print(int(random() * 10))