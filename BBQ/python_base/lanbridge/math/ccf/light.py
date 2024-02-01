# coding=utf-8
# coding=utf-8
n, m = map(int, input().split())
if n == m:
    print(n, m)

if n < m:
    if m < 2 * n:
        print(0, 2 * m - 2 * n)
    elif m == 2 * n:
        print(n, n)
    elif 2 * n < m < 3 * n:
        print(m - 2 * n, m)
    else:
        print(n, 3 * n)
elif n > m:
    if n < 2 * m:
        print(2 * n - 2 * m, 0)
    elif n == 2 * m:
        print(m, m)

    elif 2 * m < n < 3 * m:
        print(n, n - 2 * m)
    else:
        print(3 * m, m)