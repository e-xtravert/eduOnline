# @Time    : 2024/1/15 11:23
# 蓝桥杯模板题走迷宫 给定出口和入口判断是否能达到 最小步数是多少
# bfs解法
from collections import deque  # 引入队列 其实用list也可以啦

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# dirs=[(1,0),(0,1),(-1,0),(0,-1)] # 这不就是上下左右四个位置嘛


labyrinth = []
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    labyrinth.append(row)


def bfs(x1, y1, x2, y2, labyrinth):
    row, column = len(labyrinth), len(labyrinth[0])
    visited = [[False for _ in range(column)] for _ in range(row)]
    queue = deque([(x1, y1, 0)])
    visited[x1][y1] = True

    while queue:
        x, y, steps = queue.popleft()
        # x, y, dis = my_list_1.pop(0)  # 直接用队列模拟出队
        if x == x2 and y == y2:
            return steps

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < row and 0 <= ty < column and labyrinth[tx][ty] == 1 and not visited[tx][ty]:
                visited[tx][ty] = True
                queue.append((tx, ty, steps + 1))

    return -1

x1, y1, x2, y2 = map(int, input().split())
res = bfs(x1 - 1, y1 - 1, x2 - 1, y2 - 1, labyrinth)  # 这里减1考虑是bfs中的坐标都是从 0 开始的
print(res)