# @Time    : 2023/4/8 10:45
'''
给定 n 个正整数 Ai，请找出两个数 i, j 使得 i < j 且 Ai 和 Aj 存在大于 1 的
公因数。
如果存在多组 i, j，请输出 i 最小的那组。如果仍然存在多组 i, j，请输出 i
最小的所有方案中 j 最小的那组
5
5 3 2 6 9
2 4
'''
# 反正输出下标最小的 直接输出第一个就行 zai +1
n = int(input())
lis = [int(i) for i in input().split()]
ans = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(2, j + 1):
            if lis[i] % k == 0 and lis[j] % k == 0:
                ans.append(i + 1)
                ans.append(j + 1)

print(ans[0], end=' ')
print(ans[1], end='')




