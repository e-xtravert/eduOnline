# @Time    : 2023/4/8 11:29
'''
4 5
2 9 2
4 5 6
3 2 2
4 1 3
38
'''
n, m = map(int, input().split())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))


print(lis)