# @Time    : 2023/3/22 9:41
'''
递增三元组 蓝桥杯集训二分第二题
输入：
3
1 1 1
2 2 2
3 3 3
输出
27
'''

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
res = 0

# # 先写一个暴力 原本给定的就是从1开始 所以他的要求是 1到n 暴力有一半测试用例没通过
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if a[i] < b[j] < c[k]:
#                 res += 1

# 试试二分
# def dicho(n1, n2, mid):
#     if n1 < n2[mid]:
#         return True
#     else:
#         return False
#
#
# for i in range(n):
#     for j in range(n):
#         if a[i] < b[j]:
#             l = 0
#             r = len(c)
#             mid = (l + r) // 2
#             while l < r:
#                 if dicho(b[j], c, mid):
#                     res += 1
#                 else:
#                     mid =

# 枚举b，然后在a里面找一个小于b，在c里面找一个大于b的，对于每一个bi有几个数 结果就是 ai * ci
a.sort()
b.sort()
c.sort()
ai = 0
ci = 0

for i in range(n):
    while ai < n and b[i] > a[ai]:
        ai += 1
    while ci < n and b[i] >= c[ci]:  # 加了个等于结果就完全不一样了 不知道这题目出得是啥意思 换成小于等于也不行 换成小于等于 然后后面使用 ai * ci 也不行
        ci += 1
    res += ai * (n - ci)


print(res)
