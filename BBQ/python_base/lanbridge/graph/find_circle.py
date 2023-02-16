'''
发现环，这题是给定几个带边的数据，然后从小到大输出环里面的节点
牛客ab13是输出拓扑，那是没环的
主要方法是用哈希
'''
n = int(input())  # 只需要一个还需要split()干嘛呢？
graph = dict((str(i), []) for i in range(1, n + 1))  # 这里n是字符来的，从键盘获取的

for i in range(n):
    j, k = input().split()
    graph[j].append(k)

in_degree = dict((i, 0) for i in range(1, n + 1))
out_degree = dict((i, 0) for i in range(1, n + 1))  # 计算所有度，然后删除度<=1的节点，再把相关的节点度数-1，再删除

for i in graph:
    if graph[i]:
        out_degree[int(i)] += len(graph[i])
        # for j in graph[i]:
        #     in_degree[j] += 1


print(n, graph, in_degree, out_degree)