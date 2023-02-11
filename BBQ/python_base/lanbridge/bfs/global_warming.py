'''
全球变暖
岛屿 沉没 单个叫陆地，至少连两个叫同一个岛屿
https://www.lanqiao.cn/problems/178/learning/
'''

# bfs做的，其实不太熟练，还要多看看

n = int(input())
# grids = [ [*map(str, input().split())] for _ in range(n)]
# 二维数组用上面的格式可能会得到数组里面只有一个作为整体的字符，建议下面的形式
grids = []
for i in range(n):
    grids.append(input())

vis = [[0] * n for i in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = True
q = []  # 差点忘了，这里好像用不了队列


def bfs(x, y):
    global flag
    q.append((x, y))
    vis[x][y] = 1
    while len(q):
        temp = q.pop(0)
        tx = temp[0]
        ty = temp[1]
        if grids[tx][ty + 1] == '#' and grids[tx][ty - 1] == '#' and grids[tx + 1][ty] == '#' and grids[tx - 1][
            ty] == '#':
            flag = False

        for i in range(4):
            nx = tx + dir[i][0]
            ny = ty + dir[i][1]
            if vis[nx][ny] == 0 and grids[nx][ny] == '#':
                vis[nx][ny] = 1
                q.append((nx, ny))  # 如果实在bfs里面一定要有一个往队列里面或者数组里面加元素的操作，dfs就是调用函数操作


res = 0
for i in range(n):
    for j in range(n):
        if grids[i][j] == '#' and vis[i][j] == 0:
            flag = True
            bfs(i, j)
            if flag:
                res += 1

print(res)