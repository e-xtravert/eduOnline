'''
蓝桥杯训练系统 算法训练第二题 拿金币
有一个N x N的方格,每一个格子都有一些金币,只要站在格子里就能拿到里面的金币。你站在最左上角的格子里,每次可以从一个格子走到它右边或下边的格子里。请问如何走才能拿到最多的金币。
3
1 3 3
2 2 2
3 1 2
输出 11
dp[i][j] = max(dp[i - 1][j] + gold[i][j], dp[i][j - 1] + gold[i][j])
 '''
n = int(input())
gold = [[] * (n + 1) for _ in range(n + 1)]
# dp留一行一列设置为0防止溢出
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in input().split():
        gold[i].append(int(j))
    # 因为是按照dp来循环的，所以gold最好和dp的数据结构对应好，具体做法是补0,当然这就需要后面的循环过程就要设置好gold的下标
    gold[i].append(0)
# dp[1][1] = gold[1][0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # if i == 1 and j == 1:
        #     dp[i][j] = gold[1][0]
        dp[i][j] = max(dp[i - 1][j] + gold[i][j - 1], dp[i][j - 1] + gold[i][j - 1])

print(dp[n][n])