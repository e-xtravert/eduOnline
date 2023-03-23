# @Time    : 2023/3/23 10:59
'''
数组和 下标和 截取数组
in
3
1 1
1 3
5 8
out
1
4
8
'''

# 没有通过全部的测试用例，现在的水平只能通过一部分，还是一小部分 可见还得再练
n = int(input())
num = [[] for _ in range(50)]
for i in range(1, 51):
    for j in range(1, i + 1):
        num[i - 1].append(j)
num = sum(num, [])

res = 0

seq = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    seq[i].append(a)
    seq[i].append(b)
    # print(sum(num[a - 1:b]))  # 这种情况 是换行一下输出一行
for arr in seq:
    print(sum(num[arr[0] - 1:arr[1]]))
# print(seq)