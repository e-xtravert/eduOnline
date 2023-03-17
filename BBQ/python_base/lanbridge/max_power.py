# @Time    : 2023/3/17 9:39
'''
问题描述
　　逗志芃励志要成为强力党，所以他将身上所以的技能点都洗掉了重新学技能。现在我们可以了解到，每个技能都有一个前提技能，只有学完了前提技能才能学习当前的技能（有一个最根本的技能不需要前提技能）。学习每个技能要消耗一个技能点，然后可以获得这个技能的威力值。由于逗志芃要陪妹子，所以他希望你教他如何点技能使得威力值最大从而成为强力党。
输入格式
　　第一行两个数n，m表示有n个技能和m个技能点。第二行有n个数，第i个数表示第i个技能的威力值。
　　之后的n-1行，每行两个数x,y，表示y技能的前提技能是x，也就是说先学第x个技能才能学弟y个技能。
输出格式
　　一个数，最大的威力值。
样例输入
3 2
1 10 20
1 2
1 3
样例输出
21
'''
# 最开始是想着判断技能点是几个，一个就选前导技能里面最大的那个，两个就要选前导技能相同，技能和最大的
# 后来感觉有点复杂，想着是不是用dfs，回溯找一个最大的和，但是不知道怎么操作，，，
# 看了解析是用到了树型dp，这种题以前见到过，但是没做过
# 下面的答案是来源于网上
# dp[i][j]表示以i为根，消耗j个技能点，最多能换取的v
# 状态转移方程：
# dp[pos][k]=max(dp[son][h]+dp[pos][k-h],dp[pos][k])
n, q = map(int, input().split())  # n m 的值
we = list(map(int, input().split()))  # 技能数组
we.insert(0, 0)  # 技能数组里面开头插入0
gen = [0 for i in range(n)]

dp = [[0 for i in range(n+1)] for j in range(n+1)]  # 动态规划 dp二维数组
sum = [0 for i in range(n+1)]  # 记录技能和


def dfs(u, father):
    for i in range(len(edge[u])):  # edge数组中保存的是以某个技能编号为下标的一个个数组，数组内容是后续技能编号和 技能值
        v = edge[u][i][0]
        w = edge[u][i][1]
        if v == father:
            continue
        dfs(v, u)
        sum[u] += sum[v]+1
        for j in range(min(q, sum[u]), -1, -1):  # 这里看不太懂
            for k in range(min(sum[v], j-1), -1, -1):
                dp[u][j] = max(dp[u][j], dp[u][j-1-k]+dp[v][k]+w)


# 下面 一种图的表示方式
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    gen[b-1] = 1
    edge[a].append((b, we[b]))  # 这里其实是一种拓扑写法吧
    edge[b].append((a, we[b]))

for i in range(n):
    if gen[i] == 0:
        w = we[i+1]
        dfs(i+1, 0)
        break
print(dp[1][q-1] + w)
