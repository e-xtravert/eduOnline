# @Time    : 2024/3/1 22:19
# 删除一个字符后是否是回文
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 只能删除一个 那么最多只能有两个奇数个字符在里面
        # count = list(collections.Counter(s).values())

        # res = collections.Counter(count)

        # i, j = 0, len(s) - 1
        # while i < j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     elif res[1] > 2 and s[i] != s[j]:
        #         return False

        # return True

        # 直观模拟一下 如果删除一个判断删除后左右两边是不是回文
        isHuiwen = lambda x: x == x[::-1]  # 回文
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isHuiwen(s[l + 1: r + 1]) or isHuiwen(s[l:r])

        return True
