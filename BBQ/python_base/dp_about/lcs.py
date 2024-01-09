'''
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。

数据范围： 1 \le |str1|,|str2| \le 50001≤∣str1∣,∣str2∣≤5000
要求： 空间复杂度 O(n^2)O(n
2
 )，时间复杂度 O(n^2)O(n
2
 )
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, str1: str, str2: str) -> str:
        # write code here
        # 滑动窗口维护一个最长的，一般就是双指针，好理解
        # res = ''
        # left = 0
        # for i in range(len(str1) + 1):
        #     # 这里有个数组的新鲜用法
        #     if str1[left:i + 1] in str2:
        #         res = str1[left: i + 1]
        #     else:
        #         left += 1

        # return res

        # 动态规划 ,显示是超时了
        # class Solution:
        #   def LCS(self, str1: str, str2: str) -> str:
        #   dp_about_lqb[i][j]表示到str1第i个个到str2第j个为止的公共子串长度
        #   请注意 最长公共子串和最长公共子序列是不一样得
        dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
        max = 0
        pos = 0
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                # 如果该两位相同
                if str1[i - 1] == str2[j - 1]:
                    # 则增加长度
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 该位置为0
                    dp[i][j] = 0  # 最长公共子串这里是0 最长公共子序列则这里是两个字符串的最大值
                    # 更新最大长度
                if dp[i][j] > max:
                    max = dp[i][j]
                    pos = i - 1
        return str1[pos - max + 1: pos + 1]

# 数组的最长公共子序列不能直接使用上面的滑动窗口（那个 in 好像不使用）
# 下面是数组的最长公共子序列的公式 注意这是子序列 不是子串
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))  # 加个0和后面的对应
b=[0]+list(map(int,input().split()))
dp=[[0]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

# 最长公共上升序列 不太懂下面这个
import os
import sys

# 请在此输入您的代码
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0 for _ in range(1001)]
for i in range(N):
    value = 0
    for j in range(M):
        if a[i] == b[j]:
            dp[j] = max(dp[j], value + 1)
        if a[i] > b[j]:
            value = max(value, dp[j])
    count = max(dp)
    # print(dp)
print(count)


# 2024年1月8日11点25分 蓝桥杯一道前缀问题使用了双指针 很舒服
