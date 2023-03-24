# @Time    : 2023/3/24 10:57
'''
3
10000 10000 10000
20000 50000 20000
30000 20000 30000
280000
按照1 3 2的顺序安排学生答疑 时刻分别是 20000 80000 18000
'''
# 注意这题，撒谎给你一个同学在收拾东西的时候 下一个同学是不能准备的
# 也就是说前两个数的和是固定的 群里发消息的时刻之和最小 首先要三个数和最小 然后是前两个数和最小 这就是贪心
# 做得浮躁 改天更新
n = int(input())
stu = []
sum_ = []
for i in range(n):
    stu[i].append(input().split())

sum_1 = 0
for j in range(len(stu)):
    for k in range(len(stu[j])):
        sum_1 += int(''.join(stu[j][k]))
    sum_.append(sum_1)

print(stu, sum_)
