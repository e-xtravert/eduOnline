'''
题意：给定整数a1,a2,a3,a4,a5,an。判断是否可以从中选出若干数，使它们的和恰好为k。
思路：从a1开始按顺序决定每个数加或者不加，在全部n个数都决定后再判断它们的和是不是k即可，因为状态数是2^(n+1) 。 所以复杂度为O(2 ^ n)。
'''
n, k = map(int, input().split())
lis = list(map(int, input().split()))
res = []


def dfs(i, sum0):
    if i == n:
        return sum0 == k
    if dfs(i + 1, sum0):  # not plus ith number
        return True
    if dfs(i + 1, sum0 + lis[i]):  # plus ith number
        res.append(lis[i])
        return True
    return False


def check():
    if dfs(0, 0):
        print('yes')
        print(res)
    else:
        print('no')


check()
print(lis, n, k, )