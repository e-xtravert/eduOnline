'''
蓝桥杯 训练题24点
问题描述
　　24点游戏是一个非常有意思的游戏，很流行，玩法很简单：给你4张牌，每张牌上有数字（其中A代表1，J代表11，Q代表12，K代表13），你可以利用数学中的加、减、乘、除以及括号想办法得到24，例如：
　　((A*K)-J)*Q等价于((1*13)-11)*12=24
　　加减乘不用多说了，但除法必须满足能整除才能除！这样有一些是得不到24点的，所以这里只要求求出不超过24的最大值。
输入格式
　　输入第一行N(1<=N<=5)表示有N组测试数据。每组测试数据输入4行，每行一个整数(1到13)表示牌值。
输出格式
　　每组测试数据输出一个整数，表示所能得到的最大的不超过24的值。
样例输入
3
3
3
3
3
1
1
1
1
12
5
13
1
样例输出
24
4
21
'''

# 想法有，就是加减乘除四个运算嘛，分别回溯，然后遇到24输出，否则输出最大的
# 先放进数组里面

n = int(input())
lis = [[0] * 4 for _ in range(n)]
for i in range(n):
    for j in range(4):
        lis[i][j] = int(input())
res = []
dp_max = []


def dfs(cur_ans, arr, i):
    if i == 4:
        res.append(max(dp_max))
        for i in range(len(dp_max)):
            dp_max.pop(-1)
        # dp_max.clear()
        return
    if cur_ans > 24:
        return
    if cur_ans == 24:
        res.append(24)
    # 这里错了，看一下题解咯
    for k in range(len(arr)):

        cur_ans = cur_ans + arr[k][i]
        dfs(cur_ans, arr, i + 1)
        cur_ans = cur_ans - arr[k][i]

        cur_ans = cur_ans - arr[k][i]
        dfs(cur_ans, arr, i + 1)
        cur_ans -= arr[k][i]

        cur_ans *= arr[k][i]
        dfs(cur_ans, arr, i + 1)
        cur_ans /= arr[k][i]

        if cur_ans % arr[k][i] == 0:
            cur_ans /= arr[k][i]
            dfs(cur_ans, arr, i + 1)
            cur_ans *= arr[k][i]
        else:
            return

        dp_max.append(cur_ans)


dfs(0, lis, 0)
print(n, lis, res, dp_max)
