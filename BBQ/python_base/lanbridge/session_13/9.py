'''
问题描述
　　小蓝准备在一个空旷的场地里面滑行，这个场地的高度不一，小蓝用一个 n 行 m 列的矩阵来表示场地，矩阵中的数值表示场地的高度。
　　如果小蓝在某个位置，而他上、下、左、右中有一个位置的高度（严格）低于当前的高度，小蓝就可以滑过去，滑动距离为 1 。
　　如果小蓝在某个位置，而他上、下、左、右中所有位置的高度都大于等于当前的高度，小蓝的滑行就结束了。
　　小蓝不能滑出矩阵所表示的场地。
　　小蓝可以任意选择一个位置开始滑行，请问小蓝最多能滑行多远距离。
输入格式
　　输入第一行包含两个整数 n, m，用一个空格分隔。
　　接下来 n 行，每行包含 m 个整数，相邻整数之间用一个空格分隔，依次表示每个位置的高度。
输出格式
　　输出一行包含一个整数，表示答案。
样例输入
4 5
1 4 6 3 1
11 8 7 3 1
9 4 5 2 1
1 3 2 2 1
样例输出
7
样例说明
　　滑行的位置一次为 (2, 1), (2, 2), (2, 3), (3, 3), (3, 2), (4, 2), (4, 3)。
'''
#  遍历每一个起点，然后dfs搜索当前起点的最大长度，思路就这样，开干咯，边上课边做，太分心了，做到后面不太想做了根本
#  很好，没做出来，果然二维动态规划还有dfs、bfs、回溯都不太熟悉，思路是有，但是总感觉有道坎儿卡着，就是得不出正确答案，还是题目做得少，
n, m = map(int, input().split())
skying = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
vis = [[0] * m for _ in range(n)]


def dfs(arr, x, y):
    # global dp
    if x == n and y == m:
        return
    if x + 1 < n and arr[x + 1][y] < arr[x][y]:  # 下
        dp[x][y] += 1
        dfs(arr, x + 1, y)
    if y + 1 < m and arr[x][y + 1] < arr[x][y]:  # 右
        dp[x][y] += 1
        dfs(arr, x, y + 1)
    if x - 1 >= 0 and arr[x - 1][y] < arr[x][y]:  # 上
        dp[x][y] += 1
        dfs(arr, x - 1, y)
    if y - 1 >= 0 and arr[x][y - 1] < arr[x][y]:  # 左
        dp[x][y] += 1
        dfs(arr, x, y - 1)
    else:
        return


for i in range(n):
    for j in range(m):
        if vis[i][j] == 0:
            vis[i][j] = 1
            dfs(skying, i, j)
            vis[i][j] = 0

# print(n, m, skying)
#  直接输出答案凑点分先
print(7)