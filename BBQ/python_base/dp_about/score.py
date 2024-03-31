# @Time    : 2024/3/31 0:18
# leetcode100250 https://leetcode.cn/problems/minimum-levels-to-gain-more-points/

p = [1, 1]
# 元素是0 减1分 元素是1 加1分
score = 0
# 计算数组的得分
def count_score(p):
    score = 0
    for i in range(len(p)):
        if p[i] == 0:
            score -= 1
        else:
            score += 1
    return score

i = 0
res = 0
while i < len(p):
    # 比较的数组至少要有一个元素
    if i == len(p) - 1:
        break
    if count_score(p[:i + 1]) > count_score(p[i + 1:]):
        res = i + 1
        print(i + 1)
        break
    else:
        i += 1
if res == 0:
    print(-1)
else:
    print(res)

# 上面题解超时了 动态规划法 是一个降低复杂度的方式
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + (1 if possible[i - 1] == 1 else -1)
        for i in range(1, n):
            if dp[i] > dp[-1] - dp[i]:
                return i
        return -1