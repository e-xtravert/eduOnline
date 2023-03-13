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
# 确实不如二分
n, s = map(int, input().split())
gifts = [int(i) for i in input().split()]
res = 0


def _sum(arr, start, end):
    sum_ = 0
    for i in range(start, end):
        sum_ += arr[i]

    return sum_


mid = len(gifts) // 2
# 这里控制条件还是需要调整
while mid:
    if _sum(gifts, 0, mid) <= s and _sum(gifts, mid, mid * 2) <= s:
        res = mid * 2
        break
    else:
        mid = mid // 2


print(n, s, gifts, res)