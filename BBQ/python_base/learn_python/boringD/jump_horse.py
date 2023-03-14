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
'''
# 这不是典型的dfs吗？注意一下剪枝条件就完了
# 深度超标了，代码不对，先吃饭，谢谢
import sys
sys.setrecursionlimit(100000)
posi = [int(i) for i in input().split()]
x, y = posi[0], posi[1]
x1, y1 = posi[2], posi[3]
step = 0


def dfs(x_, y_, x1_, y1_):
    global step
    if x_ > 8 or y_ > 8 or x_ < 0 or y < 0:
        return
    if x_ == x1_ and y_ == y1_:
        return

    if x_ > x1_ or y_ > y1_:
        return

    # 如果目标在右上角，那么往左边遍历肯定是到不了的， 往对应方向遍历
    if x_ < x1_ and y_ < y1_:
        dfs(x_ + 1, y_ + 2, x1_, y1_)  # 在这里加step其实是不合理的，因为不知道这个点是不是真的通过了
        dfs(x_ + 2, y_ + 1, x1_, y1_)

    if x_ < x1_ and y_ > y1_:
        dfs(x_ + 1, y1_ - 2, x1_, y1_)
        dfs(x_ + 2, y1_ - 1, x1_, y1_)

    if x_ > x1_ and y_ < y1_:
        dfs(x_ - 1, y_ + 2, x1_, y1_)
        dfs(x_ - 2, y_ + 1, x1_, y1_)

    if x_ < x1_ and y_ < y1_:
        dfs(x_ - 1, y_ - 2, x1_, y1_)
        dfs(x_ - 2, y_ - 1, x1_, y1_)

    step += 1

dfs(x, y, x1, y1)
print(step)
