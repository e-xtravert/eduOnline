'''
从n个数里面选出k个数和为sum,题目是从n个数中选取k个数使得和为s，求出方案个数。同的思路会对应不同的搜索方法，相应的搜索树也不同。
我们先来研究从1~30里面选择8个数，和为200的情况，其他类似。
1.从30个数中选8个数，那么这8个数可以按照从大到小的顺序排列，例如1，6，9，...或者3，9，10....。选第一个数的时候可以是1~23；
二个数就从第一个数的后面那些数中选，然后以此类推。这样不会漏掉哪一个组合。
搜索树：
5 3 9
1 2 3 4 5
输出有2两种
'''

n, k, sum0 = map(int, input().split())
lis = [int(i) for i in input().split()]
res = 0


def dfs(s, pos, cnt):
    global res
    if s > sum0 or cnt > k:
        return
    if cnt == k and s == sum0:
        res += 1
        return
    for i in range(pos, n):
        dfs(s + lis[i], i + 1, cnt + 1)


dfs(0, 0, 0)

print(n, k, sum0, lis, res)