# @Time    : 2023/4/6 9:58
'''
进击的青蛙 http://lx.lanqiao.cn/problem.page?gpid=T2662
input
5

1

0

0

1

0
output
3
'''

n = int(input())
pos = []
for i in range(n):  # n 个数字 n 个空行 循环 n 此即可
    nl = input()
    num = int(input())
    pos.append(num)
ans = 0


def dfs(step):
    global ans
    if step >= n:
        if step == n:
            ans += 1
        else:
            return

    for i in range(step, n):
        if pos[i] == 1:
            dfs(step + 1)
            dfs(step + 2)


print(pos)