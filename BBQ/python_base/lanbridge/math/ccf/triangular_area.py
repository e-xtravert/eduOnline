# @Time    : 2024/1/31 21:33
# print("%.2f" % 0)
# s = str(input())

# coding=utf-8
n, m = map(int, input().split())
if n == m:
 print(n, m)

if n < m:
    if m < 2*n:
        print(0, 2*m-2*n)
    elif m == 2*n:
        print(n,n)
    else:
        print(n,3*n)
elif n > m:
    if n < 2*m:
        print(2 * n - 2 * m, 0)
    elif n == 2*m:
        print(m,m)
    else:
        print(3*m,m)


