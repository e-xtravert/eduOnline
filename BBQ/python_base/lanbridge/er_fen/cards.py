# @Time    : 2023/3/27 17:20
'''
4 5
1 2 3 4
5 5 5 5
3
还是没有通过全部的测试用例
'''

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res = 0


def check(x):
    sum_ = 0  # 用了几张空白排
    for i in range(n):
        if x - a[i] > b[i]:  # 如果需要构成的套数 x 比当前的数量和手写的加起来还要多， 说明不够
            return False
        sum_ += max(x - a[i], 0)  # 如果够了，那就要减去用掉的手写了的空牌

    if sum_ <= m:  # 如果总共用掉的手写牌 小于给定的空牌 则true
        return True
    return False


l = min(a)
r = max(a) + max(b)

while l <= r:  # 加上等于洛谷多通过一道题
    mid = (l + r) // 2
    if check(mid):
        res = mid  # 如果符合条件 说明 x 即 mid 还可以更大 试试更大的值 即满足条件最大的嘛
        l = mid + 1
    else:
        r = mid - 1

print(res)
