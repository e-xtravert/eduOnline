'''
问题描述
　　勇士们不小心进入了敌人的地雷阵（用n行n列的矩阵表示，'*'表示某个位置埋有地雷，'-'表示某个位置是安全的），
他们各自需要在规定的步数（一步代表走到和当前位置相邻的位置）内绕开地雷到达出口（第一行第一格，即坐标为（0,0）的位置）才能完成任务，告诉你每个勇士的位置（x，y）和规定的步数s，
请你判断每个勇士能否顺利完成任务（1代表“能”，-1代表“不能”）。
输入格式
　　输入数据的第一行为一个整数n；第二行至第n+1行是n行n列地雷阵的矩阵表示（见输入样例）；第n+2行至最后一行每行是一个勇士的位置x、y和到达出口规定的最大步数s，三个整数间用空格隔开。
输出格式
　　按顺序输出对每个勇士是否能顺利完成任务的判断（1代表“能”，-1代表“不能”），对每个勇士的判断占一行。
样例输入
5
-----
--*--
-**--
-**--
*-*--
0 1 1
0 4 3
1 1 3
1 4 2
2 0 3
3 0 4
3 3 2
4 1 3
样例输出
1
-1
1
-1
1
1
-1
-1
'''
n = int(input())
mine = [[] for _ in range(n)]


for i in range(n):
    for j in input():
        mine[i].append(j)

# 最容易想到的就是，如果当前位置和（0， 0）的距离大于给定的步数，那铁定过不去
def dis(x, y, dist):
    if x == 0 and y == 0:
        return 1
    if x + y > dist:
        return -1

# 实在不知道怎么把不确定行数的代码持久化，后来想了一下，不如放到函数里面，再对函数进行设定,
# 还是不对，放弃了，找人求助了需要


pos = [input()]


# 就先按照只能向上向左的方向走
def bfs(x, y, cnt):
    if x == 0 and y == 0 and cnt == 0:
        return 1

    while pos:
        size = len(pos)
        for _ in range(size):
            warrior = pos.pop(0)

            if mine[int(warrior[0])][int(warrior[1])] != '_':
                pos.append()
                # TODO





print(n, mine, pos)