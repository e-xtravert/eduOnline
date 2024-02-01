# @Time    : 2024/2/1 17:08
# 第一行输入三个整数n，m，k分别表示小岛大小（不包括大海）和城墙的数量；
# 接下来k行，每行4个数x1,y1,x2,y2分别表示城墙的起始位置和结束位置，左上角位置为（1,1）；
# 最后一行2个数sx、sy，表示火山口的位置（只会在平地上）；

n, m, k = map(int, input().split())

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
#     process function
    print(x1, y1, x2, y2)


sx, sy = map(int, input().split())
