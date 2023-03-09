'''
问题描述
　　在N*N的方格棋盘放置了N个皇后，使得它们不相互攻击（即任意2个皇后不允许处在同一排，同一列，也不允许处在与棋盘边框成45角的斜线上。你的任务是，对于给定的N，求出有多少种合法的放置方法。
输入格式
　　输入中有一个正整数N≤10，表示棋盘和皇后的数量
输出格式
　　为一个正整数，表示对应输入行的皇后的不同放置数量。
样例输入
5
样例输出
10
'''
# 先用二维数组试试吧，一维数组也有方法
# 2023年3月9日初稿，感觉没啥问题，无非就是多了很多的重复搜索，然后一些不确定的问题，这题为什么需要回溯，目前还没确定，不是用dfs吗？
# 知道原因啦，回溯是因为他们的要求需要输出每一个 1 放置好的结果，而我只需要计数就好啦， 拉个屎再来解决上面的问题
n = int(input())
board = [[0] * n for _ in range(n)]
# board[0][0] = 1
res = 0


# 先写一个判断条件
def check(row, col):
    for i in range(n):
        for j in range(n):  # 如果在棋盘中已经放好了一个1，然后遍历所有的1，如果放入的值行列是在 1 同行同列或是斜对角，那就不能放1了，会攻击的
            if board[i][j] == 1 and (row == i or col == j or abs(row - i) == abs(col - j)):
                return 0
            else:
                return 1


def dfs(row, col):
    global res
    if row == n or col == n:
        return
    if row == n and col == n:
        res += 1

    for i in range(n):
        for j in range(n):
            if check(row, col) == 1:
                board[i][j] = 1
                dfs(row + 1, col)
                dfs(row, col + 1)

            dfs(row + 1, col)
            dfs(row, col + 1)


dfs(0, 0)
print(n, board)
