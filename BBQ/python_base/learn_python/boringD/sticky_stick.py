'''
问题描述
　　有N根木棍，需要将其粘贴成M个长木棍，使得最长的和最短的的差距最小。
输入格式
　　第一行两个整数N,M。
　　一行N个整数，表示木棍的长度。
输出格式
　　一行一个整数，表示最小的差距
样例输入
3 2
10 20 40
样例输出
10
'''
# 首先，每层递归都会决定一个木棍的走向：一个for循环，决定该木棍去到堆1~堆m。
# 然后，每层递归所决定的木棍应不同(往后递进的)：参数为存放木棍数组元素下标，每次+1调用。
# 最后，要保证每个木棍都得用上：整一个对应的bool数组，存放状态。
# (最后) 因为会存在这样的情况：某木棍"去过"所有堆后(该层循环结束)，再进入下一层时，上层的木棍哪个堆都没去，这怎么行？最终出现所有木棍哪个堆都没去的情况，结果为0，那就出错了。所以得确保所有木棍都用上。
# 一样的思路，python就会超市，c++就轻松通过，唉，蓝桥杯比完，写算法还是c++
n, m = map(int, input().split())
sticks = [int(i) for i in input().split()]
vis = [0 for _ in range(n)]  # 标记：第几个木棍是否已经使用：未使用 0，已使用 1
add = [0 for _ in range(m)]  # 表示各个分组的和(该分组内所有木棍的总长度)
min_sum = 1e9


def func(x):
    global min_sum
    # 所有木棍分完了，就来
    if x >= n:
        for i in range(n):
            if vis[i] != 1:
                return

        min_ = add[0]
        max_ = add[0]

        # 获取各个分组的最长和最短的差值
        for i in range(m):
            if min_ > add[i]:
                min_ = add[i]

            if max_ < add[i]:
                max_ = add[i]

        # 更新差值，找到最小的
        if min_sum > max_ - min_:
            min_sum = max_ - min_

        return

    for i in range(m):
        # 把这个木棍粘到第i组
        add[i] += sticks[x]
        vis[x] = 1
        func(x + 1)

        # 不把这个木棍粘到第i组
        add[i] -= sticks[x]
        vis[x] = 0
        func(x + 1)


func(0)
# print(n, m, sticks, min_sum)
print(min_sum)