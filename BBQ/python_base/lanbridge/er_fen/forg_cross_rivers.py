# @Time    : 2023/4/7 17:15
'''
5 1
1 0 1 0
4
'''
import sys

readline = sys.stdin.readline

read = lambda: [int(x) for x in readline().split()]

n, m = read()

arr = read()
s = [0] * n
for i, x in enumerate(arr):
    s[i + 1] = s[i] + x


def check(y):
    for i in range(n - y):
        if s[i + y] - s[i] < 2 * m: return False
    return True


l = 0
r = n

while l < r:
    mid = l + r >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1

print(l, s, arr)