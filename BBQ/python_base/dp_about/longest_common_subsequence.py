# @Time    : 2023/3/22 19:01
'''
最长公共子序列 注意这和最长公共字串是不一样得
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text2)][len(text1)]  # leetcode用下面输出方式报错，一般是return值，和需要输入输出下面的方式 是不一样的
        # print(dp[len(text2)][len(text1)], end='')
