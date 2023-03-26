# @Time    : 2023/3/26 10:55
'''
利用动态规划求解 game_match  国赛题名不虚传
input
10 0
1 4 2 8 5 7 1 4 2 8
output
6
10 1
2 1 1 1 1 4 4 3 4 4
9
https://www.cnblogs.com/flyawayl/p/8305203.html
设共有x
种分数，将其分为k
组，每个分数满足相邻的分数值相差为k
。正如样例2中所示，共有4种分数，将其分为1组：{1,2,3,4},这个组中任何相邻的两个分数都不能同时取，因为它们相差k
，该分组还对应了一个人数分组：{4,1,1,4},要想使得人数尽量多，而且分数不能相差1，那么选择分数分别为{1,4},人数是4+4=8.

　　上述是只有一个分组的情况，当有多个分组的时候也是同样的处理方法--尽量选择不相邻且人数最多。对于一个人数分别为{a1,a2,...,an}
的分组，可以利用动态规划算法来选择最多人数，且都不相邻。每个ai
只有选择与不选择两种可能，假设dp(i)
表示前i个人数能获得的最多人数，那么选择第i个人数的话，dp(i)=dp(i−2)+ai
，如果不选择第i个人数的话，dp(i)=dp(i−1)
，这样得到转移方程dp(i)=max{dp(i−1),dp(i−2)+ai}
。
'''
# 蓝桥杯似乎很喜欢考这种动态规划 二维数组压缩成以为数组的题目
n, k = map(int, input().split())
ans = 0
# 用一维数组cnt保存每一个下标对应的人数 这种做法可以压缩空间
cnt = [0 for _ in range(n)]  # 如果不用 0 占位 不好操作
for i in input().split():
    num = int(i)
    cnt[num] += 1

# 将cnt中 下标值相差为 k 的 也就是积分相差为 k 的人数分为 1 组，存放进part
part = [0 for i in range(n)]

# dp 表示动态数组
dp = [0 for i in range(n + 1)]

# 当差值为0 即k为0的情况 只需要判断不重复数个数即可
if k == 0:
    for i in cnt:
        if i:
            ans += 1

# 当差值不为 0 需要先分组
# 将积分差值为 k 的分为一组 最多分 k 组的
for i in range(k):
    pos = 0
    for j in range(0, len(cnt), k):
        part[pos] = cnt[j]
        pos += 1

        dp[0] = part[0]
        for l in range(1, pos):  # pos 已经是最大值了
            if l == 1:  # 处于dp[l - 2] 防止越界s
                dp[l] = max(dp[0], part[l])
            else:
                dp[l] = max(dp[l - 2] + part[l], dp[l - 1])  # 选第l个 就不能选相邻的 不选第 l 个 当前状态就是前一个状态
    # 注意位置
    ans += dp[pos - 1]


print(ans)
