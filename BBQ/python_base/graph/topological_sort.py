'''
牛客ab13
输入：第一行表示5个节点4条边，后面依次输出表示从前到后有一条有向边
5 4
1 2
2 3
3 4
4 5
输出 1 2 3 4 5
'''

n, m = map(int, input().split())
graph = dict((str(i), []) for i in range(1, n + 1))

for i in range(m):  # n个节点，m条边
    j, k = input().split()
    graph[j].append(k)  # 这个节点和谁相连指向谁

in_degree = dict((i, 0) for i in graph)  # use of dict
# 计算入度
for i in graph:
    for j in graph[i]:  # 每个hash值的数据取出来
        in_degree[j] += 1  # 如果有对应的节点

lis = [i for i in in_degree if in_degree[i] == 0]  # 找到入度为0的，就是没有边指向他的
res = []

while lis:
    c = lis.pop()
    res.append(c)
    for i in graph[c]:
        in_degree[i] -= 1
        if in_degree[i] == 0:  # 他这里好像只能输出一个边的吧？
            lis.append(i)

if len(res) == n:
    print(' '.join(res))
else:
    print(-1)
# print(n,m, graph, in_degree)
