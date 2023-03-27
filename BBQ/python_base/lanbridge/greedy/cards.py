# @Time    : 2023/3/27 16:36
'''
4 5
1 2 3 4
5 5 5 5
3
'''
# 这是贪心 但是没有通过
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res = []
a.sort(reverse=True)
m_ = -float('inf')
for i in range(n):
    if m_ >= 0:
        res.append(a[i - 1])
    if m_ < 0:
        m_ = m
    for j in range(i + 1, n):
        gap = a[i] - a[j]
        m_ -= gap

print(res[0])
