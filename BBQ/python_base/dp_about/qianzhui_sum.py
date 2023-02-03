'''

牛客dp-34
'''



n, q = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

pre = [0 for i in range(n)]
pre[0] = data[0]

for i in range(1, n):
    pre[i] = pre[i - 1] + data[i]

for i in range(q):
    l, r = map(int, input().strip().split())
    res = pre[r - 1] - pre[l - 1] + data[l - 1]
    print(res)
