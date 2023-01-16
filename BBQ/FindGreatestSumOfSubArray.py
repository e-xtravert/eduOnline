'''
描述
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，子数组最小长度为1。求所有子数组的和的最大值。
数据范围:
1 <= n <= 2\times10^51<=n<=2×10
5

-100 <= a[i] <= 100−100<=a[i]<=100

要求:时间复杂度为 O(n)O(n)，空间复杂度为 O(n)O(n)
进阶:时间复杂度为 O(n)O(n)，空间复杂度为 O(1)O(1)
'''
# 连续子数组的最大和
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> int:
        # 记录到下标i为止的最大连续子数组和
        # 就是搞一个数组，然后记录到下标i为止的最大连续子数组和保存到对应的数组值
        dp = [0 for i in range(len(array))] # 这个是全0格式化
        dp[0] = array[0] # 第0就是数组第一个的值
        maxsum = dp[0] # 也是做动态分析，选择最大值
        for i in range(1, len(array)):
            # 状态转移：连续子数组和最大值
            # 原理是前i项和第i项相加若是更大则选，变小说明第i项是更大的
            dp[i] = max(dp[i - 1] + array[i], array[i])
            # 维护最大值
            maxsum = max(maxsum, dp[i])
        return maxsum
