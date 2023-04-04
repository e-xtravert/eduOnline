# @Time    : 2023/4/4 8:31
'''
python 版答案
'''


def dfs(x, room):  # 第 x 个学生 和考场数
    global num, p
    if room >= num:  # 剪枝
        return
    if x > n:
        num = min(room, num)  # 更新最优解
        return
    for j in range(1, room + 1):  # 枚举考场，把第x个人放到第i个考场里面
        k = 0  # 第k个座位
        while p[j][k] and a[x][p[j][k]] == 0:  # 如果k位子有人而且不认识x
            k += 1  # 下一个位子
        if p[j][k] == 0:
            p[j][k] = x  # 第j个考场的第k个位子让第x个学生坐
            dfs(x + 1, room)  # 继续
            p[j][k] = 0  # 回溯
    p[room + 1][0] = x  # 如果1-room的考场都不能坐，就到第room+1个考场的第一个位子
    dfs(x + 1, room + 1)
    p[room + 1][0] = 0  # 回溯


n = int(input())
m = int(input())
num = 110
a = [[0 for j in range(n + 1)] for i in range(n + 1)]  # 关系表
p = [[0 for j in range(n + 1)] for i in range(n + 1)]  # 考场状态
for i in range(m):
    u, v = map(int, input().split())
    a[u][v] = 1
    a[v][u] = 1  # 表示x和y认识
dfs(1, 0)
print(num)