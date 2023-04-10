# @Time    : 2023/4/9 11:26
'''
leetcode 340期赛
'''


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0

        def check(n):
            for i in range(2, floor(sqrt(n)) + 1):  # 判断质数的方法
                if n % i == 0:
                    return False
            return True

        for j in range(len(nums)):
            if check(nums[j][j]):
                ans = max(ans, nums[j][j])
            if check(nums[j][len(nums) - j - 1]):
                ans = max(ans, nums[j][len(nums) - j - 1])
        # a = check(841)
        # print(a)
        return ans


# 第一次超时 第二次错了一个测试用例