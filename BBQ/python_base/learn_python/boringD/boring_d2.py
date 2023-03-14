'''
问题描述
　　逗志芃在干了很多事情后终于闲下来了，然后就陷入了深深的无聊中。不过他想到了一个游戏来使他更无聊。他拿出n个木棍，然后选出其中一些粘成一根长的，
然后再选一些粘成另一个长的，他想知道在两根一样长的情况下长度最长是多少。
输入格式
　　第一行一个数n，表示n个棍子。第二行n个数，每个数表示一根棍子的长度。
输出格式
　　一个数，最大的长度。
样例输入
4
1 2 3 1
样例输出
3
'''
# 还有一种是用公式求解的，网上看到的
# woc 居然过了，牛逼
n = int(input())
sticks = [int(i) for i in input().split()]
add = sum(sticks) // 2
max_sum = 0
min_sum = float('inf')

sticks.sort(reverse=True)  # true是降序

for i in range(n):
    if add - max_sum >= sticks[i]:  # 他这里 add再变化， max_sum也在变，其实和dfs原理是一样，只不过这是公式
        max_sum += sticks[i]  # 也是分堆，只不过这里直接把右边那堆给到max_sum了
        min_sum = min(min_sum, add - max_sum)


print(max_sum, min_sum)
