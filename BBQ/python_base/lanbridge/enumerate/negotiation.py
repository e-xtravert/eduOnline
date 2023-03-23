# @Time    : 2023/3/23 21:47
'''
谈判
input
4
9 1 3 5
output
31
'''
n = int(input())
people = [int(i) for i in input().split()]
people.sort()  # 默认就是升序 reverse=False应该是降序

for i in range(1, len(people)):
    people[i] = people[i - 1] + people[i]

print(sum(people) - people[0])  # 第一个数多加了一次
