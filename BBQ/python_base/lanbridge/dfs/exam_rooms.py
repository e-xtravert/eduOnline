# @Time    : 2023/4/3 20:33
'''
exam_room答案 https://blog.csdn.net/timelessx_x/article/details/115468647 用python重构了结果没出结果 笑死
M是存放关系的矩阵；
room是考场的关系矩阵；
对于当前问题dfs(x,kc);
即是第x个考生，kc个考场；
从第一个考场开始找，
该考场没人，直接入考场；
该考场有人，遍历这些人，如果没有认识的入考场；
如果有认识的就找下一个考场；
一但入了考场，就递归dfs找下一规模问题，知道找到一个解，和当前值比较，如果更优就更新；
'''

M = [[0 for _ in range(101)] for _ in range(101)]  # 等效于 int M[101][101];//关系矩阵 int room[101][101];//考场矩阵
room = [[0 for _ in range(101)] for _ in range(101)]
ans = 9999
n = int(input())
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    M[a][b] = 1
    M[b][a] = 1


def dfs(num, kcs):
    global ans
    if kcs >= n:
        return
    if num > n:
        ans = kcs
    else:
        for i in range(1, kcs + 1):
            k = 0
            while room[i][k] and M[num][room[i][k]] == 0:
                k += 1

            if room[i][k] == 0:
                room[i][k] = num
                dfs(num + 1, kcs)
                room[i][k] = 0

        room[kcs + 1][0] = num
        dfs(num + 1, kcs + 1)
        room[kcs + 1][0] = 0


dfs(1, 1)
print(ans)