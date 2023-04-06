# @Time    : 2023/4/6 14:12
'''
https://leetcode.cn/problems/jump-game-ii/
输入: nums = [2,3,1,1,4]
输出: 2
2 3 0 1 4
output 2
'''

nums = [int(i) for i in input().split()]

# 也就是说只能向前跳 最大的距离是值 不跳那么远也可以 从下标为0开始
# 不要思维定式
ans = 0
end = 0
max_p = 0

for i in range(len(nums) - 1):
    max_p = max(max_p, i + nums[i])
    if i == end:
        end = max_p
        ans += 1  # 在本次跳跃的范围内起跳 都算一次起跳 知道进入边界 需要再跳 上面 i 循环范围也是 如果到了末尾就不要跳了


print(ans)

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         ans = 0
#         end = 0
#         max_p = 0
#         for i in range(len(nums) - 1):  # max_p 是最大距离 而不能到数组的最后一个位置 那肯定超标 而且似乎都是能够超远距离跳的数据
#             max_p = max(max_p, i + nums[i])
#             if i == end:
#                 end = max_p
#                 ans += 1
#
#         return ans
