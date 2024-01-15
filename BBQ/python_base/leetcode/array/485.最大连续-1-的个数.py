#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
# https://leetcode.cn/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (61.11%)
# Likes:    428
# Dislikes: 0
# Total Accepted:    226K
# Total Submissions: 369.8K
# Testcase Example:  '[1,1,0,1,1,1]'
#
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 
# 
# 示例 2:
# 
# 
# 输入：nums = [1,0,1,1,0,1]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                index = i
            else:
                res = max(res, i - index)
        
        return res
                
# @lc code=end

