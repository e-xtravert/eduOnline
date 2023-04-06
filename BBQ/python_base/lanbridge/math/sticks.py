# @Time    : 2023/4/6 8:47
'''
扫描游戏 顺时针 方向同时覆盖 按覆盖到的时间排序
input
5 2
0 1 1
0 3 2
4 3 5
6 8 1
-51 -33 2
output
1 1 3 4 -1
'''

n, l = map(int, input().split())
# 这应该是模拟类型 把实际情况转化为代码形式
posi = []
for i in range(n):
    path = list(map(int, input().split()))
    # print(path)
    posi.append(path)
# print(posi)

order = [[] for _ in range(n)]


# 先按排好序的方法做  他的长度的末端实在坐标的位置 理解错题目了
for j in range(n):
    if l >= posi[j][2]:
        l += posi[j][2]
        order[j].append(j)
    if j >= 1:
        if l >= posi[j][2]:
            if posi[j - 1][0] == posi[j][0]:
                order[j].append(j - 1)
        else:
            continue

    else:
        continue

print(order)