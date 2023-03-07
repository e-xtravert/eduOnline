'''
问题描述
　　给出一个n长的数列，再进行m次询问，每次询问询问两个区间[L1,R1]，[L2,R2]，
　　询问数列第L2到R2个数字每一个数在数列第L1到R1个数中有多少个数字不大于它。
输入格式
　　第一行两个整数n,m
　　第二行n个整数，表示数列。
　　接下来m行，每行四个整数L1,R1,L2,R2，意义如上
输出格式
　　m行，每行R2-L2+1个整数，第一个整数表示第L2个数在数列第L1到R1个数中不大于它的个数，第一个整数表示第L2+1个数在数列第L1到R1个数中不大于它的个数，以此类推
样例输入
5 3
5 2 3 4 1
1 2 3 4
2 3 1 5
1 5 2 3
样例输出
1 1
2 1 2 2 0
2 3
'''
# 这题就一个需要注意的，就是数组下标问题，其他没了,可惜只有80分，不过就先这样吧，重要的是思想
n, m = map(int, input().split())
lis = [int(i) for i in input().split()]
inds = [[0] for _ in range(m)]
path = []
res = []
for i in range(m):
    inds[i] = input().split()

for i in range(len(inds)):
    for j in range(4):
        inds[i][j] = int(inds[i][j])


def compare(arr):
    for i in range(len(path)):  # path记录值弹出
        path.pop(-1)
    for i in range(arr[2], arr[3] + 1):
        cnt = 0
        for j in range(arr[0], arr[1] + 1):
            if lis[j - 1] <= lis[i - 1]:
                cnt += 1
        if cnt >= 0:  # 小于0就算了， 等于0也要啊
            path.append(cnt)

    # 下面一长串就是为了凑一个输出，唉呀，太没技术含量了，结果已经有了，还要在输出上磨蹭磨蹭
    for i in range(len(path)):
        if i == len(path) - 1:  # 如果是最后一个数了，那就输出，默认换行
            print(path[i])
        else:
            print(path[i], end=' ')  # 不是那就不换


for t in range(len(inds)):
    compare(inds[t])

# for i in range(len(res)):
#     for j in range(len(res[i])):
#         print(res[i][j], end=' ')
# print(n, m, lis, inds, res)