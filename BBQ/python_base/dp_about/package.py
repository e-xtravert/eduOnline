'''

牛客dp41，背包问题
'''



while True:
    try:
        n, V = map(int, input().split())
        lv, lw = [], []
        for i in range(n):
            l = list(map(int, input().split()))
            lv.append(l[0])  # 物品重量列表
            lw.append(l[1])  # 物品价值列表
        # 2 双结果dp[j]
        dp = [0 for _ in range(V + 1)]
        # dp[j]表示背包容量为j时装满背包的最大价值。
        # 最终输出时，问题1的答案是整个dp的最大值，问题2的答案是dp的最后一个数，初始化时数字是0所以最后如果的不到结果也满足答案要求。
        for i in range(n):
            for j in range(V, -1, -1):  # 从后向前算，防止数据混淆
                if lv[i] <= V and(j == lv[i] or (dp[j - lv[i]] != 0 and j - lv[i] > 0)):
                    # 条件首先剔除无法放入背包的物品。然后如果新加入的物品可以单独放入某一个j、或者与已存在的值可以组成j的值进行计算。
                    #  由于Python的特性dp需剔除负坐标j - lv[i] > 0
                    dp[j] = max(dp[j], dp[j - lv[i]] + lw[i])
                    # dp[j]的值只与其当前值、能与lv[i]重量组合成j重量的dp[j - lv[i]]，两个数中的较大值
        print(max(dp))
        print(dp[-1])
    except:
        break




n, V = map(int, input().split())
# map1 = [ [ *map(int, input().split())] for _ in range(n)]
v = []
w = []
for i in range(n):
    lis = list(map(int, input().split()))
    v.append(lis[1])
    w.append(lis[0])

dp = [0] * (n + 1)
for i in range(n):
    if V - v[i] >= 0:
        dp[i] = max(dp[i - 1], dp[V - v[i]] + w[i])



# dp[i] = max(dp[i - 1], dp[V - v[i]] + w[i])，当背包恰好装满就多一个i <= 容量的条件就行了呗？



print(n, V, v, w, dp)