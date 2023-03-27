# @Time    : 2023/3/27 14:59
'''
给定数列
11135917⋯
1,1,1,3,5,9,17,31⋯，从第 4 项开始，每项都是前 3 项的和。
求第 20190324 项的最后 4 位数字。
'''

# memory 不够了  网上看的答案 两个很大的数相加的和几个尾数就是对10的几次方取余的结果 这样不会越界
n = 20190324
res = [1, 1, 1]

for i in range(3, n):
    num = (res[i - 1] + res[i - 2] + res[i - 3]) % 10000
    res.append(num)
print(res[n - 1])


# n = 20190324
# res = [1, 1, 1, 3]

# 运行了很长时间
# for i in range(4, n):
#     if i % 4 == 0:
#         res[i % 4] = res[1] + res[2] + res[3]
#     if i % 4 == 1:
#         res[1] = res[0] + res[2] + res[3]
#     if i % 4 ==2:
#         res[2] = res[0] + res[1] + res[3]
#     if i % 4 == 3:
#         res[3] = res[1] + res[2] + res[3]
#
# print(res[n % 4])