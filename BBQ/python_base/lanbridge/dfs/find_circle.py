'''
小明的实验室有 NN 台电脑，编号 1 \cdots N1⋯N。原本这 NN 台电脑之间有 N-1N−1 条数据链接相连，恰好构成一个树形网络。
在树形网络上，任意两台电脑之间有唯一的路径相连。
不过在最近一次维护网络时，管理员误操作使得某两台电脑之间增加了一条数据链接，于是网络中出现了环路。
环路上的电脑由于两两之间不再是只有一条路径，使得这些电脑上的数据传输出现了 BUG。
为了恢复正常传输。小明需要找到所有在环路上的电脑，你能帮助他吗？
输入范围：
第一行包含一个整数 NN 。
以下 NN 行每行两个整数 a,ba,b，表示 aa 和 bb 之间有一条数据链接相连。
enter:
5
1 2
3 1
2 4
2 5
5 3
outer:
1 2 3 5
'''

# 借鉴代码学习dfs先
n = int(input())
edge = [[] for i in range(n + 1)]  # 邻接表
pre = [0] * (n + 1)
ring = []
vis = [False] * (n + 1)
for i in range(n):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)


def dfs(x, fa):
    vis[x] = True
    for son in edge[x]:
        if len(ring) > 0:
            return
        if not vis[son]:
            pre[son] = x
            dfs(son, x)
        elif son != fa:
            temp = x
            while temp != son:
                ring.append(temp)
                temp = pre[temp]
            ring.append(son)


dfs(1, 0)
ring.sort()
for k in ring:
    print(k, end=' ')
