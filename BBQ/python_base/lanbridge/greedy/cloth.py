# @Time    : 2024/1/31 0:37

# # 请在此输入您的代码
# # 尽量先把邮费高的染成不同色 那就可以不用重复邮寄花费最高邮费的衣服
# n = int(input())
# lis = list(map(int, input().split()))
# # print(lis)
# lis.sort()
#
# def pre_n_sum(li, n):
#   return sum(li[0:n])
#
# # print(pre_n_sum(lis, 3))
#
# res = 0
# for i in range(n - 1, 0, -1):
#   res += pre_n_sum(lis, i + 1)
#
# print(res)

# 哈夫曼树求和 列表法
# 关键 pop append

# 通过 60%
# n = int(input())
# lis = list(map(int, input().split()))
# lis.sort()
# res = 0
# while len(lis) > 1:
#     t = lis.pop(0) + lis.pop(0)
#     res += t
#     lis.append(t)
#     lis.sort()


# print(res)

# 通过80%
def binary_insert(lst, item):
    """Insert an item into a sorted list."""
    lo, hi = 0, len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if item < lst[mid]:
            hi = mid
        else:
            lo = mid + 1
    lst.insert(lo, item)

# Read input
n = int(input())
lis = list(map(int, input().split()))
lis.sort()  # Initial sort

res = 0
# Continue combining the two smallest elements.
while len(lis) > 1:
    # Combine the two smallest elements, which are at the beginning
    # after initial sorting.
    t = lis.pop(0) + lis.pop(0)
    res += t
    # Insert the sum back into the list, maintaining the sorted order.
    binary_insert(lis, t)

print(res)