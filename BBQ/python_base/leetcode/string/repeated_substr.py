# # @Time    : 2024/2/29 21:38
# from collections import Counter
# def repeatedSubstringPattern(s: str) -> bool:
#     if len(s) % 2:
#         return False
#
#     for i in list(Counter(s).values()):
#         if not i % 2:
#             return False
#
#     return True
#
# res = repeatedSubstringPattern("abab")
# print(res)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 不一定是偶数的 3 个的重复 3 次也可以
        # if len(s) % 2 != 0:
        #     return False

        # for i in list(collections.Counter(s).values()):
        # if i % 2 != 0:
        #     return False
        # 应该是全部都相等
        # if len(set(list(collections.Counter(s).values()))) == 1:
        #     return True
        # else:
        #     return False

        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # 如果到i的子串不整除 长度 n 那铁定不是
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True

        return False

res = Solution().repeatedSubstringPattern("babbabbabbabbab")
print(res)