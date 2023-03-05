'''
问题描述
　　小蓝有一个序列 a[1], a[2], ..., a[n]。
　　给定一个正整数 k，请问对于每一个 1 到 n 之间的序号 i
    a[i-k], a[i-k+1], ..., a[i+k] 这 2k+1 个数中的最小值是多少？当某个下标超过 1 到 n 的范围时，数不存在，求最小值时只取存在的那些值。
输入格式
　　输入的第一行包含一整数 n。
　　第二行包含 n 个整数，分别表示 a[1], a[2], ..., a[n]。
　　第三行包含一个整数 k 。
输出格式
　　输出一行，包含 n 个整数，分别表示对于每个序号求得的最小值。
样例输入
5
5 2 7 4 3
1
样例输出
2 2 2 3 3
'''

n = int(input())
lis = [int(i) for i in input().split()]
k = int(input())
path = [[] * (n + 1) for i in range(n + 1)]
res = []
# 调试了一下，结果是2, 2, 3, 3, 3应该是这里出问题，题目说是序号，而我这里是数组下标，只要数量正确就行，n个数嘛
for i in range(0, n):
    for j in range(0, 2 * k + 1):
        if 0 <= i - k + j <= n - 1:
            path[i].append(lis[i - k + j])

    res.append(min(path[i]))

# print(path)
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end='')  # 最后一个不换行咯
    else:
        print(res[i], end=' ')  # 不换行，空格结尾
