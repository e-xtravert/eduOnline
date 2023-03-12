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
# mmp这题应该用bfs的，结果整了个dfs，明天再做吧，头脑不清晰
n = int(input())
mine = [[] for _ in range(n)]
warrior = [[] for _ in range(3)]
for i in range(n):
    for j in input():  # 又掌握一个新知识点喔，如果输入是有空格，或者换行的，那就用split(),没有空格就直接input()
        mine[i].append(j)


# 这里本来想保存的，但是题目没有给多少勇士的位置，所以灵光一闪，不如不保存了，直接作为函数参数
# for i in input().split('\n'):  # 这里就是以换行结尾的情况，他会把每一行放进去
#     for j in len(i):
#         warrior[j].append(i)

# 先写一个判断的
def check(x, y, arr):
    if arr[x][y] == '-':
        return 1
    else:
        return 0


def dfs(row, col, cnt):
    if cnt >= 0 and row ==0 and col == 0:
        return 1
    elif cnt == 0 and (row != 0 or col != 0):
        return -1

    for i in range(row):  # 我在这里就可以定范围啊，为什么还要考虑那些边界值，哎呀，做完没睡好，精神状态太差，思路都是混乱的。每次写下几行代码，又有新的思路，然后删掉重写
        for j in range(col):
            if check(i - 1, j):
                cnt -= 1
                dfs(i - 1, j, cnt)
            if check(i, j - 1):
                cnt -= 1
                dfs(i, j - 1, cnt)
            # 如果上边，左边都走不了，那走右边或是下边，反正先走上边或左边，能走通那自然好，走不通那没办法
            # 但是这样有可能会越界, 设个条件
            if i + 1 < n and j + 1 < n:
                if check(i + 1, j):
                    cnt -= 1
                    dfs(i + 1, j, cnt)
                if check(i, j + 1):
                    cnt -= 1
                    dfs(i, j + 1, cnt)

            return -1


for num in input().split("\n"):
    arr = num.split()
    # print(num.split()[0])  # 笑死，我把这个取出来了。
    print(dfs(int(arr[0]), int(arr[1]), int(arr[3])))

print(n, mine, warrior)
