'''
蓝桥杯训练系统第二题 礼物
问题描述
　　JiaoShou在爱琳大陆的旅行完毕，即将回家，为了纪念这次旅行，他决定带回一些礼物给好朋友。
　　在走出了怪物森林以后，JiaoShou看到了排成一排的N个石子。
　　这些石子很漂亮，JiaoShou决定以此为礼物。
　　但是这N个石子被施加了一种特殊的魔法。
　　如果要取走石子，必须按照以下的规则去取。
　　每次必须取连续的2*K个石子，并且满足前K个石子的重量和小于等于S，后K个石子的重量和小于等于S。
　　由于时间紧迫，Jiaoshou只能取一次。
　　现在JiaoShou找到了聪明的你，问他最多可以带走多少个石子。
样列输入
8 3
1 1 1 1 1 1 1 1
样列输出
6
'''

# 明天再找几个二分的题目做一下先，根据结果，选择区间，不断二分渐进
n, s = map(int, input().split())
gifts = [int(i) for i in input().split()]
val = [0 for _ in range(n)]  # 用来计算前缀和

# 下面是一种计算前缀和的方法，有点像动态规划,适合一些求数组前后段的和，不妨设置成差的形式
for i in range(n):
    val[i] = gifts[i] + val[i - 1]


# 首先用哪种方法，对其中思想一定要熟悉


def check(item):
    for i in range(item, n - item + 1):
        if val[i] - val[item] <= s and val[i + item] - val[i] <= s:
            return True

    return False


l = 1
r = int(1e6)  # 10的6次方，浮点数
while l < r:
    mid = (l + r + 1) // 2  # 原文是用了再二进制的形式上右移1位的手段达到除2的目的
    if check(mid):
        l = mid
    else:
        r = mid - 1
# print(n, s, gifts, val, 2 * l)
print(2 * l)