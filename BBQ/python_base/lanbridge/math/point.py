# @Time    : 2023/4/1 22:39
'''
小数点后第 n 位开始的3位数
input
1 8 1
output
125
'''

a, b, n = map(int, input().split())
res = a / b
res = str(res)


def check(s):
    if len(s) < n + 3:
        return res + '0' * (n + 3 - len(s))
    else:
        return res


res = check(res)[2:]


print(res[n:n + 3])
