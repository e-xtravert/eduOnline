# @Time    : 2023/4/3 19:36
'''
分考场
5
8
1 2
1 3
1 4
2 3
2 4
2 5
3 4
4 5
output
4
'''
n = int(input())
m = int(input())
# 两两认识 有点像图 原本想用map 但是突然想到用数组  数组表达是可以 但是用图更方便，省去对下标的关注
peo = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    peo[a].append(b)
print(peo)
res = 0
vis = [0 for _ in range(n)]
path = []


# 先写一个check函数判断是否是满足都不认识的条件
def check(p):
    for i in range(5):
        if i in peo[p]:
            return False
        else:
            return True

# 先选一个人 然后找一个跟他不认识的 再找这个人不认识的 如果不能再找到了就退出 对除去这些人的集合再分
# def dfs(path_):
#     for i in path_:
#         if not check(i):
#
