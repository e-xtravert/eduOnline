'''

牛客dp-34
在lanqiaobridge的enumerate中也有
'''

# 在对一些求子矩阵 子数组和的情况下 都可以考虑前缀和的方法
n, q = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

pre = [0 for i in range(n)]
pre[0] = data[0]

for i in range(1, n):  # 前缀和保存的是前面的元素和 和当前元素的和
    pre[i] = pre[i - 1] + data[i]

for i in range(q):
    l, r = map(int, input().strip().split())
    res = pre[r - 1] - pre[l - 1] + data[l - 1]
    print(res)
