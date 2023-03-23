# @Time    : 2023/3/23 21:26
'''
小蓝面前有 N 件物品, 其中第 i 件重量是 , 价值是 。她还有一个背包, 最大承重是
小蓝想知道在背包称重范围内, 她最多能装总价值多少的物品?
特别值得一提的是, 小蓝可以使用一个魔法 (总共使用一次), 将一件物品 的重量增加 K, 同时价值秝倍。(当然小蓝也可以不使用魔法)
input
3 10 3
5 10
4 9
3 8
output
26
describe:
选择第二件和第三件物品, 同时对第二件物品使用魔法。
'''
# 求价值最高的物品
n, m, k = map(int, input().split())
goods = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    goods[i].append(a)
    goods[i].append(b)

# md背包还是不熟悉，写到这懵逼了，改天找个时间把以前写过的代码好好看看
# dp[i] =
dp = [0 for _ in range(n + 1)]  # 放第i件物品的最大价值


print(goods)