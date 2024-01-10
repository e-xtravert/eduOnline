#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
# https://leetcode.cn/problems/can-place-flowers/description/
#
# algorithms
# Easy (32.39%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    215.8K
# Total Submissions: 666.1K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 
# 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n
# ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 <= n <= flowerbed.length
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 可以先在数组中看看还有哪些相邻的位置是空缺的
        # 答案是用可以种花的情况来判断的
        # flowerbed = [0] + flowerbed + [0]
        # for i in range(1, len(flowerbed) - 1):
        #     if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
        #         flowerbed[i] = 1  # 种花！
        #         n -= 1
        # return n <= 0

        # 另外一个答案
        i = 0
        while i <= len(flowerbed) - 1:
            if flowerbed[i] == 1:
                i += 2
            # 因为到最后一个的时候前面一定是0 所以可以 这个条件就是flowerbed[i] == 0
            # 如果不是最后一个那就要考虑后面相邻那个是不是
            elif i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:  
                n -= 1
                i += 2
            else:
                i += 3
        
        return n <= 0

# @lc code=end

