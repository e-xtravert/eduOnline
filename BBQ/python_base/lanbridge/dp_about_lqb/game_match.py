# @Time    : 2023/3/26 10:00
'''
给定n, k 表示用户和积分差
积分序列
输出最多有几名用户同时在线匹配无法成功
input
10 0
1 4 2 8 5 7 1 4 2 8
output
6
'''

n, k = map(int, input().split())
game = [int(i) for i in input().split()]

res = [[] for _ in range(n)]

# 暴力 应该是能出来结果的
# 看了一下答案 非常interesting 详见game_match new
for i in range(n):
    res[i].append(game[i])
    for j in range(n):
        if abs(game[i] - game[j]) <= k:
            continue
        if (game[j] + k) or (game[j] - k) in res[i]:  # 这也不行
            break
        # for l in range(len(res[i])):
        #     if abs(game[j] - res[i][l]) <= k:
        #         break
        else:
            res[i].append(game[j])

print(res)