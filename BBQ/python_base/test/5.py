# @Time    : 2023/4/8 10:28
'''
阶乘的和
给定 n 个数 Ai，问能满足 m! 为
∑n
i=1(Ai
!) 的因数的最大的 m 是多少。其中
m! 表示 m 的阶乘，即 1 × 2 × 3 × · · · × m 。
'''
def jie(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


n = int(input())
a = [int(i) for i in input().split()]
s = 0
for i in range(n):
    s += jie(a[i])

# print(s)

def check(n):
    s0 = 1
    for i in range(1, n + 1):
        s0 *= i

    if s % s0 == 0:
        return True
    return False


l = 1
r = s
while l < r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid


print(l - 1)
