# @Time    : 2024/3/1 20:43
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # # 看懂那个高赞回答了 但是 感觉不太好想

        # n = len(nums)
        # f = [True] + [False] * n
        # for i, x in enumerate(nums):
        #     if i > 0 and f[i - 1] and x == nums[i - 1] or \
        #         i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
        #                                 x == nums[i - 1] + 1 and x == nums[i - 2] + 2):
        #         f[i + 1] = True

        # return f[n]

        # 这个是官方题解里面的 定义函数的解释 感觉好理解一点
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if i >= 2:
                dp[i] = dp[i - 2] and self.validTwo(nums[i - 1], nums[i - 2])
            if i >= 3:
                dp[i] = dp[i] or (dp[i - 3] and self.validThree(nums[i - 3], nums[i - 2], nums[i - 1]))

        return dp[-1]

    def validTwo(self, num1: int, num2: int) -> bool:
        return num1 == num2

    def validThree(self, num1: int, num2: int, num3: int) -> bool:
        return (num1 == num2 == num3) or (num1 + 2 == num2 + 1 == num3)