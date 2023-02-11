'''
分巧克力
儿童节那天有 K 位小朋友到小明家做客。小明拿出了珍藏的巧克力招待小朋友们。
小明一共有 NN 块巧克力，其中第 ii 块是 H_i \times WiH
i
​
 ×Wi 的方格组成的长方形。为了公平起见，
小明需要从这 NN 块巧克力中切出 K 块巧克力分给小朋友们。切出的巧克力需要满足：
形状是正方形，边长是整数;
大小相同;
例如一块 6x5 的巧克力可以切出 6 块 2x2 的巧克力或者 2 块 3x3 的巧克力。
当然小朋友们都希望得到的巧克力尽可能大，你能帮小明计算出最大的边长是多少么？
输入：
2 10
6 5
5 6
输出：2
'''

import os
import sys

# 请在此输入您的代码
# 面积相同

n, k = map(int, input().split())

cholo = [[*map(int, input().split())] for _ in range(n)]


def check(w):
    nums = 0
    for wid, hig in cholo:
        nums += (wid // w) * (hig // w)

        if nums >= k:
            return True

    return False


# 二分法逐个测试,左右指针
l, r = 1, 1000000
while l <= r:  # 这里不写等于只能通过62.5%
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1  # 如果满足，则左边界向右移动，尽可能找最大的
    else:
        r = mid - 1

print(l - 1)