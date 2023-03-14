'''
问题描述
　　一个8×8的棋盘上有一个马初始位置为(a,b)，他想跳到(c,d)，问是否可以？如果可以，最少要跳几步？
输入格式
　　一行四个数字a,b,c,d。
输出格式
　　如果跳不到，输出-1；否则输出最少跳到的步数。
样例输入
1 1 2 3
样例输出
1
测试用例2
1 1 8 8
6
'''
# 在每一点都是可以往8个方向跳的
a, b, c, d = map(int, input().split())
# 8个方向，到哪个方向直接循环这个数组然后加上每个元素就行
dir = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]
min_step = float('inf')
vis = [[0] * 9 for _ in range(9)]


def dfs(x, y, step):
    global min_step
    if step > min_step:
        return

    if x == c and y == d:
        min_step = step
        return

    for i in range(8):
        nx = x + dir[i][0]
        ny = y + dir[i][1]

        if 0 <= nx <= 8 and 0 <= ny <= 8:
            # dfs(nx, ny, step + 1)
            # 加这个好像能减少一些深度计算 不加有可能会报这个错：maximum recursion depth exceeded in comparison
            # 因为当跳到某个位置不合适，往回跳的时候，跳到回到七点的路径上的某个位置还有可能会往上跳到曾经跳过的位置
            # 而那个位置已经遍历过，显然是不合适的，因此没必要重复跳了，同时有可能避免
            # 最重要是避免step的错误增加
            if vis[nx][ny] == 0:
                vis[nx][ny] = 1
                dfs(nx, ny, step + 1)
                vis[nx][ny] = 0


dfs(a, b, 0)
if min_step == float('inf'):
    print(-1)
else:
    print(min_step)


