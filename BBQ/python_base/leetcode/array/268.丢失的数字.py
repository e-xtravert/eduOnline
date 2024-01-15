#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#
# https://leetcode.cn/problems/missing-number/description/
#
# algorithms
# Easy (66.69%)
# Likes:    805
# Dislikes: 0
# Total Accepted:    335.1K
# Total Submissions: 502.5K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,0,1]
# 输出：2
# 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1]
# 输出：2
# 解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 
# 示例 3：
# 
# 
# 输入：nums = [9,6,4,2,3,5,7,0,1]
# 输出：8
# 解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
# 
# 示例 4：
# 
# 
# 输入：nums = [0]
# 输出：1
# 解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# nums 中的所有数字都 独一无二
# 
# 
# 
# 
# 进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
# 
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # 初始化为数组长度，因为缺失的数可能是 n
        for i, num in enumerate(nums):
            missing ^= i ^ num  # i 和 num 分别与当前索引和数组元素异或
        return missing

#     def missingNumber(self, nums: List[int]) -> int:
#         s = set(nums)
#         for i in range(1, len(nums) + 1):
#             if i not in s:
#                 return i
#         return 0
# @lc code=end

