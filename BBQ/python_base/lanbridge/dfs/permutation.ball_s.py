'''
还是排列小球题目，没结果！！！烦死了
'''

a, b, c = [int(i) for i in input().split()]
res = 0


def dfs(x, y, z, leng, color):
    global res
    if x == 0 and y == 0 and z == 0:
        res += 1
    for i in range(leng + 1, x + 1):
        if color != 0:
            dfs(x - 1, y, z, i, 0)
    for i in range(leng + 1, y + 1):
        if color != 1:
            dfs(x, y - 1, z, i, 1)
    for i in range(leng + 1, z + 1):
        if color != 2:
            dfs(x, y, z - 1, i, 2)


dfs(a, b, c, 0, 0)
dfs(a, b, c, 0, 1)
dfs(a, b, c, 0, 1)
print(res // 2)
