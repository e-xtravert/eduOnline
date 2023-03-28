# @Time    : 2023/3/28 15:55
'''二维数组前缀和
'''

arr = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
pre = [[0 for _ in range(len(arr))] for _ in range(len(arr))]  # 初始化的时候 这里可能还需要处理一下 至少数组空间要确定
pre[0][0] = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0 and j == 0:
            pre[i][j] = arr[i][j]
        # 先对第0行和第1行进行处理
        if i == 0:  # 上面处理了 同时为0的情况 下面就可以单独分析 就和一维数组前缀和一样
            pre[i][j] = pre[i][j - 1] + arr[i][j]
        if j == 0:
            pre[i][j] = pre[i - 1][j] + arr[i][j]
        else:
            pre[i][j] = pre[i][j - 1] + pre[i - 1][j] + arr[i][j] - pre[i - 1][j - 1]  # 减去是因为多加的 自己画个图就知道了

print(pre)
