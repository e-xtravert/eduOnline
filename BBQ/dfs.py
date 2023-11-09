# @Time    : 2023/4/26 17:22
from typing import List

# 定义无向图节点
class Node:
    def __init__(self, val: int):
        self.val = val          # 节点的值
        self.neighbors = []     # 节点的邻居

# 深度优先搜索函数
def dfs(node: Node, target: Node, path: List[Node], visited: List[bool]) -> bool:
    # 将当前节点标记为已访问
    visited[node.val] = True
    # 将当前节点加入路径
    path.append(node)

    # 如果当前节点是目标节点，返回 True 表示已找到路径
    if node == target:
        return True

    # 遍历当前节点的邻居节点
    for neighbor in node.neighbors:
        # 如果邻居节点未被访问过，则继续搜索
        if not visited[neighbor.val]:
            if dfs(neighbor, target, path, visited):
                return True

    # 如果无法到达目标节点，则将当前节点从路径中删除
    path.pop()
    return False

# 查找从源节点到目标节点的路径
def find_path(source: Node, target: Node) -> List[Node]:
    path = []                   # 存储路径
    visited = [False] * 100     # 存储节点是否被访问过，初始化为 False

    dfs(source, target, path, visited)

    return path

# 测试
if __name__ == '__main__':
    # 创建无向图
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node0.neighbors = [node1, node2]
    node1.neighbors = [node0, node3]
    node2.neighbors = [node0, node3]
    node3.neighbors = [node1, node2]

    # 查找从节点0到节点3的路径
    path = find_path(node0, node3)

    # 输出路径
    if not path:
        print("No path found.")
    else:
        print("Path:", end=" ")
        for node in path:
            print(node.val, end=" ")
        print()