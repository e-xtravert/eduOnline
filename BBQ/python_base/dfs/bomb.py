'''
在一个n*n的方格地图上，某些方格上放置着炸弹。手动引爆一个炸弹以后，炸弹会把炸弹所在的行和列上的所有炸弹引爆，被引爆的炸弹又能引爆其他炸弹，这样连锁下去。
现在为了引爆地图上的所有炸弹，需要手动引爆其中一些炸弹，为了把危险程度降到最低，请算出最小手动引爆多少个炸弹可以把地图上的所有炸弹引爆。
输入：
第一行两个整数 n , m，表示地图行列数
接下来n行，每行输入一个长度为m的字符串，表示地图信息。0表示没有炸弹，1表示有炸弹
输出：
输出一个整数，表示最少需要手动引爆的炸弹数量
5 5
1 0 0 1 0
0 0 0 1 0
1 0 0 1 0
0 0 0 0 1
0 1 0 0 0
out： 3
'''
# 之前做过，但是好像没成功运行，再写一次
# 就是如果碰到1就 ++ ，然后进入dfs，碰到1就dfs，否则就退出，行和列分别dfs
n, m = map(int, input().split())
bomb = [0 for _ in range(m)]
vx = [0 for _ in range(m)]  # 表示第i列是否访问
vy = [0 for _ in range(n)]  # 表示行是否访问
res = 0

# 对访问过的数不需要再次用到则是dfs，这里用backtrack应该也可以？ -2023年3月8日
# 答案的做法是这里当前炸弹置0，然后无差别搜索当前行，列每一个元素，我直接从后面搜索
def dfs(row, column):
    if not vx[row]:
        vx[row] = 1
        for i in range(row, m):
            if bomb[row][i] == '1':
                dfs(row, i)  # 这里放入列

    if not vy[column]:
        vy[column] = 1
        for j in range(column, n):
            if bomb[j][column] == '1':
                dfs(j, column)


# 这就是昨天放二维数组的方法，用一个循环，但是这样好像不能快速处理成int类型，尝试了几下还是失败了，先不整了，后面再看，不过我需要的就是字符，笑死
for i in range(n):
    bomb[i] = input().split()

for i in range(n):
    for j in range(m):
        if bomb[i][j] == '1' and vx[j] == 0 and vy[i] == 0:  # 如果某个元素已经访问过了，说明就算是炸弹已经爆炸了，就不需要引爆了
            res += 1
            dfs(i, j)
print(n, m, bomb, vx, vy, res)
