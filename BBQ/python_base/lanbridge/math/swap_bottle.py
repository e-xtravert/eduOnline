# @Time    : 2023/4/5 22:03
'''
交换瓶子
5
3 1 2 5 4
output
3
'''
n = int(input())
lis = [int(i) for i in input().split()]
ans = 0

for i in range(n):
    while i + 1 != lis[i]:
        j = i + 1
        lis[lis[j]], lis[i] = lis[i], lis[lis[j]]  # 是交换这两个下标对应的数 比如第1 和 第1个数对应的下标3 的数交换
        ans += 1
print(ans)
