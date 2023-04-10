# @Time    : 2023/4/8 11:11
'''
试题H
3
1 2 1
11 3 4
74 5 3
1
2
24
'''
# 几叉树就是几个节点铺满之后
n = int(input())
req = []
for i in range(n):
    req.append(input().split())

# def tree(arr):
#     if arr[0] >= int(arr[1]) - 1:
#         return int(arr[0])



print(req)