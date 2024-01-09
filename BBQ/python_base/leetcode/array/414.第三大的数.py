#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode.cn/problems/third-maximum-number/description/
#
# algorithms
# Easy (39.94%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    157K
# Total Submissions: 392.9K
# Testcase Example:  '[3,2,1]'
#
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。
# 
# 示例 2：
# 
# 
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
# 
#

# @lc code=start
class Solution:
   def thirdMax(self, nums: List[int]) -> int:
    first = second = third = float('-inf')  # 初始化为负无穷大
    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif second < num < first:
            third = second
            second = num
        elif third < num < second:
            third = num
    if third != float('-inf'):
        return third
    else:
        return first  # 如果没有第三大的唯一元素，则返回最大值

# @lc code=end

