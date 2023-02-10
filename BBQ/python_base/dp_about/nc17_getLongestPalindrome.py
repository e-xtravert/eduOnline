'''
nc17 最长回文子串

'''

from re import S


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    # 从中间向两边扩散
    def fun(self, s: str, begin: int, end: int) -> int:
        while begin >= 0 and end < len(s) and s[begin] == s[end]:  # 等于是为了判断回文
            begin -= 1
            end += 1

        return end - begin - 1

    def getLongestPalindrome(self, A: str) -> int:
        # write code here
        maxlen = 1

        for i in range(len(A) - 1):
            # 找到这么一个动态规划维护的式子， 把字符串中每一个字符都作为中心点
            maxlen = max(maxlen, max(self.fun(A, i, i), self.fun(A, i, i + 1)))

        return maxlen