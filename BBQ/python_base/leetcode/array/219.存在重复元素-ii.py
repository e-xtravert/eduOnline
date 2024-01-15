#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if abs(i - j) <= k and nums[i] == nums[j]:
        #             return True
        # return False  # 注意return位置不要出错
        # 上面的方法最容易想到 但是超时了
        # 滑动窗口 + 哈希做法
        n = len(nums)
        s = set()

        for i in range(n):
            # i 是窗口右断点下表 如果 i <= k 说明还不到窗口大小 就往 s 里面添加 否则就把最左边元素移除
            if i > k:
                s.remove(nums[i - k - 1])
            # 如果 当前遍历元素在s中 则 true
            if nums[i] in s:
                return True
            s.add(nums[i])

        return False
            
            
        # print(nums)
# @lc code=end

