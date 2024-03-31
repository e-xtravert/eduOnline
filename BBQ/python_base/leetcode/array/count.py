# @Time    : 2024/3/10 18:52
# import collections
#
# a = '123123'
# count = collections.Counter(a)
# print(count['5'])
#
# s = 'capiTalIze tHe titLe'
# s1 = 'intention'
# s2 = 'execution'
# num = 111
# f = lambda s: s.title() if len(s) > 2 else s.lower()
# print(' '.join(s), ' '.join(map(f, s.split())))
# print(s.replace('a', ''), s)
#
# print(list(str(num)))
# s = s.join('fds')
# print(s)
#
# count_0 = 2
# s0 = '0' * count_0
# # while count_0 >= 0:
# #     s0 = s0.join('0')
# #     count_0 -= 1
#
# print(s0)
# print(min(float('inf'), 3))
# res = [x for x in s2 if x not in s1]
# print(res)
# print(ord('0'))  # 48
#
# a = [1, 2, 3]
# print(a[1:3])
# print(a.reverse())
# a.pop(1)
# print(a)
# print(5 // 3)
# print(int(5 / 2))
# import collections
#
#
# def encrypt(num):
#     n = len(str(num))
#     num_new = [0] * n
#     tmp = max(list(str(num)))
#     # print(tmp)
#     for i in range(n):
#         num_new[i] = tmp
#     return int(''.join(num_new))
#
# res = encrypt(124)
# print(res)
#
# s = 'fdsafa'
# print(''.join(set(list(s))) == '?')
# print(s[3])
# count1 = collections.Counter(s)['f']
# print(count1)
import collections
import math

# def countSubstrings(s: str, c: str) -> int:
#     # 双指针拿捏一下
#     # count = collections.Counter(s)[c]
#     ans = 0
#     i, j = 0, 0
#     while i < len(s):
#         tmp = []
#         if s[i] == c:
#             for j in range(i, len(s)):
#                 if s[j] == c:
#                     tmp.append(j)
#                     ans += 1
#         if len(tmp) >= 2:
#             i = tmp[1]
#         else:
#             i += 1
#     return ans
#
# res = countSubstrings("abada", "a")
# print(res)
nums = [1,2,3,4,5]
target = 11
res = []
for i in range(len(nums)):
    for j in range(len(nums) + 1):
        if sum(nums[i:j]) == target:
            res.append(j - i)
# print(min(res) if not res else 0)
# return min(res) if not res else 0
if len(res) != 0:
    print(min(res))
else:
    print(0)

o = 0
print(not o)

nums = [8407,5626,9236,4362,9678,6568,4170,5691,7865,4067,2094,9451,9667,1400,5093,6191,7286,7368,6461,4309,9751,3672,4165,4940,3726,7003,6263,4250,1950,9536,61,1486,6009,6977,7084,2472,7921,1913,117,3543,5075,1582,7987,6710,1331,3023,6856,1125,1475,4158,3422,7864,9178,7255,4997,2128,5441,5910,6719,1308,4444,9746]
k = 30
if not nums:
    print(0)
n = len(nums)
res = nums[0]
for i in range(n):
    for j in range(i, n):
        if i <= k <= j:
            res = max(res, min(nums[i: j + 1])  * (j - i + 1))

print(res)

stock = [2,5,7,4]
stock.sort()
print(stock[:3])
print(collections.Counter(stock))
for i, val in collections.Counter(stock).items():
    print(val)
count = collections.Counter(stock).items()
stocks = [1, 2, 3, 4, 4]
stocks.pop()
print(stocks)
print(set(stocks))

# s = input()
# dp = [0] * len(s)
# # print(dp)
# #
# # print(len(set(s)))
#
# def strs(s):
#     # if len(s) > 2 * len(set(s)):
#     #     return False
#     # return True
#     for i, val in collections.Counter(s).items():
#         if val > 2:
#             return False
#     return True
# tmp = 0
# i, j = 0, 1
# while i < len(s) and j < len(s):
#     if j == len(s) - 1 and strs(s[i:j + 1]):
#         tmp = max(tmp, j - i + 1)
#     if strs(s[i:j + 1]):
#         j += 1
#     else:
#         tmp = max(tmp, j - i)
#         i += 1
#         j = i + 1
#
# print(tmp)

# nums = [1]
# k = 11
# tmp = 0
# mins = k
# if nums[0] == k:
#     print(0)
# for i in range(1, math.ceil(k / 2)):
#     cnt = math.ceil(k / i)
#     mins = min(i + cnt - 1, mins)
# print(mins - 1)

print('---------------------------------')

k = 1.5
print(k / 2)
while k != 1 and k % 2 ==0:
    k /= 2