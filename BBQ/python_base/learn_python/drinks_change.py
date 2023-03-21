# @Time    : 2023/3/21 19:47
'''

'''

n = int(input())
nums = n
while n // 3 >= 1:
    nums += n // 3
    n = n // 3 + n - 3 * (n // 3)  # 加上由于整除向下取整丢失的数


print(nums)