#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (65.81%)
# Likes:    1294
# Dislikes: 0
# Total Accepted:    303.1K
# Total Submissions: 460.6K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums
# 中的数字，并以数组的形式返回结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,1]
# 输出：[2]
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# 1 
# 
# 
# 进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。
# 
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 直接使用set秒了
        # res = []
        # nums.sort()
        # s = set(nums)
        # for i in range(1, len(nums) + 1):
        #     if i not in s:
        #         res.append(i)

        # return res
        
        # 直接使用数组相减试试 集合是可以相减的 数组不可以 当然数组有别的方式
        tmp = []
        for i in range(1, len(nums) + 1):
            tmp.append(i)
        s = set(nums)
        s_res = set(tmp)
        res = list(s_res - s)
        return res

        # 数组相减的方式 但是没有完全通过 因为他的位置可能不是对应的
        # tmp = []
        # for i in range(1, len(nums) + 1):
        #     tmp.append(i)
        
        # s = set(nums)
        # s_rev = list(s)
        # res = [i for i in tmp if i not in s_rev]
        # return res
# @lc code=end

