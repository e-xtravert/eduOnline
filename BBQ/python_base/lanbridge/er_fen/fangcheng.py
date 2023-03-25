# @Time    : 2023/3/25 10:46
'''
一元三次方程求解
1 -5 -4 20
-2.00 2.00 5.00 保留两位小数
'''

# 但是没有通过所有的测试用例 todo
a, b, c, d = map(int, input().split())


def fun(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def check(x, y):
    if x - y < 0.0001:
        return x

    mid = (x + y) / 2
    if fun(x) * fun(mid) > 0:  #
        return check(mid, y)  # 这个函数有return注意格式统一
    else:
        return check(x, mid)


for i in range(-100, 100 + 1):
    if fun(i) == 0:
        print('%.2f' % i, end=' ')

    if fun(i) * fun(i + 1) < 0:  # 这里不是说 只能在 x 和 x + 1 之间的点， 而 x 和 x + n 的点就不行。是找到 x 这个位置， 换一种表达方式 x - 1 也是一样的结果 经过测试
        print('%.2f' % check(i, i + 1), end=' ')



