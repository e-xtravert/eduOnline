# @Time    : 2023/11/9 17:34

# @lc app=leetcode.cn id=11 lang=golang
#
# [11] 盛最多水的容器
#
# https://leetcode.cn/problems/container-with-most-water/description/
#
# algorithms
# Medium (60.27%)
# Likes:    4354
# Dislikes: 0
# Total Accepted:    998.4K
# Total Submissions: 1.7M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。

n = int(input())
height = [int(i) for i in input().split(",")]

i, j = 0, n - 1
max_water = 0

while i < j:
    water = min(height[i], height[j]) * (j - i)
    max_water = max(max_water, water)

    if height[i] < height[j]:
        i += 1
    else: j -= 1

print(max_water)