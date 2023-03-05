'''
杨辉三角，画图就能看出来了，左边上边+上边
'''

m = int(input())
# 只是设置了100，得分是40，多设点就好了，只不过时间效率就下去了
n = 100
triangles = [[0] * n for i in range(n)]
res = []
for row in range(n):
    triangles[row][0] = 1
    triangles[row][row] = 1

for row in range(2, n):
    for column in range(1, row):
        triangles[row][column] = triangles[row - 1][column] + triangles[row - 1][column - 1]

for i in range(len(triangles)):
    for j in range(len(triangles[i])):
        if triangles[i][j] != 0:
            res.append(triangles[i][j])

ans = res.index(m)
print(ans + 1)
