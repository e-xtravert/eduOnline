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
这题还是比较经典的，很多接替方案
'''
# 这题很好，在网上看了一下解析，大致就是将木棍分成两堆，然后进行处理数据
# 下面用dfs做一下，就是从左边最多的堆分木棍到右边，然后再剪枝

n = int(input())
sticks = [int(i) for i in input().split()]
add = sum(sticks)
max_sum = 0


# 涉及选与不选的问题， 可以退回到上一步的状态这些就可以用dfs了
# 当然最开始要想好这个结构， 分堆
def dfs(arr, i, left, right):
    global max_sum
    if left == right and max_sum <= left:
        max_sum = left
        return

    if left < right or i >= n:
        return
    else:
        dfs(arr, i + 1, left - arr[i], right + arr[i])  # 选择左边的木棍放到右边
        dfs(arr, i + 1, left, right)  # 不选择
        dfs(arr, i + 1, left - arr[i], right)  # 放弃这个木棍
        return


sticks.sort()  # 升序排列可以一个一个来
dfs(sticks, 0, add, 0)
# print(n, sticks, add, max_sum)
print(max_sum)