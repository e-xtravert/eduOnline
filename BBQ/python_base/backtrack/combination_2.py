'''
给定两个整数n和k，返回1…n中所有可能的k个数的组合。
如输入为n = 4, k = 2，则返回结果为[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]。
'''

n, k = [int(i) for i in input().split()]
path = []
res = []


def backtrack(start, leng, num):
    if len(path) == leng:
        res.append(path.copy())
        return

    for i in range(start, n + 1):
        path.append(i)
        backtrack(i + 1, k, num)
        path.pop(-1)


backtrack(1, k, n)
print(res)


