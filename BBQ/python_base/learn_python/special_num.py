# @Time    : 2023/3/25 21:37
'''
特别数的和 要 2 0 1 9包含的
'''

n = int(input())
sum_ = 0
for i in range(1, n + 1):
    s = str(i)
    if '2' in s or '0' in s or '1' in s or '9' in s:
        sum_ += i

print(sum_)