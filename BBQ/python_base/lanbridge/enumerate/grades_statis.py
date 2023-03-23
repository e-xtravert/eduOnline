# @Time    : 2023/3/23 9:13
'''
成绩统计 工作日a 双休日b 总数n
'''
import math

a, b, n = map(int, input().split())
res = 0

# if 5 * a > n:
#     res = int(n / a) + 1
# if 5 * a <= n <= 5 * a + 2 * b:
#     res = int((n - 5 * a) / b) + int(n / 5) + 2
# if 5 * a + 2 * b <= n:
#     if n - n // (5 * a + 2 * b) * (5 * a + 2 * b) < 5 * a:
#         res = n // (5 * a + 2 * b) * 7 + int((n % (5 * a + 2 * b)) / a) + 1
#     if 5 * a <= n - n // (5 * a + 2 * b) * (5 * a + 2 * b) <= 5 * a + 2 * b:
#         res = n // (5 * a + 2 * b) * 7 \
#               + int((n - n // (5 * a + 2 * b) * (5 * a + 2 * b)) / a) + 1 \
#               + int(((n - n // (5 * a + 2 * b) * (5 * a + 2 * b)) / a - 5 * a) / b) + 1\
#               + int(int((n - n // (5 * a + 2 * b) * (5 * a + 2 * b)) / a) / 5) + 1

# 出问题了 不想搞了
# def check(num):
#     if num < 5 * a:
#         return int(num / a) + 1
#     if 5 * a <= num <= 5 * a + 2 * b:
#         return int((num - 5 * a) / b) + int(num / 5) + 2
#     if 5 * a + 2 * b <= num:
#         nu = num % (5 * a + 2 * b)
#         return check(nu) + int(num / (5 * a + 2 * b)) + 1
#
#
# res = check(n)

print(res)