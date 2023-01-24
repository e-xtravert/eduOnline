# import os
# import sys

# 做完的感受就是，在刷题之前先看一下题目对应考的算法或是结构，比如说考双指针，动态规划，list，数组啊，列表啊什么的，去看一下参考文档，再做题


# # 请在此输入您的代码
# char = str(input())
# pre = 0
# cur = 0
# arr = [0 for i in range(len(char))]
# hsh1 = dict()
# hsh2 = dict()

# for i in range(len(char)):
#   for j in range(len(char)):
#     if char[i] == char[j]:
#       arr[i] += 1
#     else:
#       j += 1
#   i += 1


# for i in range(len(char)):
#   if char[i] not in hsh1:
#     hsh1[char[i]] = 1
#   else:
#     hsh1[char[i]] += 1

# for i in range(len(char)):
#   if char[i] not in hsh2:
#     hsh2[char[i]] = i

# # while hsh1

# print(arr)
# print(hsh2)
# print(hsh1)
import os
import sys

# 请在此输入您的代码
word = input()
a = 0
b = []
for i in word:
    c = word.count(i)
    if c >= a:
        a = c
for j in word:
    if word.count(j) == a:
        b.append(j)
b.sort()
print(b[0])
print(a)

# 做完的感受就是，在刷题之前先看一下题目对应考的算法或是结构，比如说考双指针，动态规划，list，数组啊，列表啊什么的，去看一下参考文档，再做题

