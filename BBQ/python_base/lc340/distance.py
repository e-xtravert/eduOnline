# @Time    : 2023/4/9 10:39
'''
leetcode340期赛
'''


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            # print(nums[i])
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    ans[i] += abs(j - i)

        return ans

# 但是超时了，有几十个用例没通过 想了一个优化方案
# 就是用哈希保存有重复的元素 然后一次for 循环找到重复的元素， 再把下标差保存再对应的key值下