'''
蓝桥杯训练题 ALGO-994最大分解
问题描述
　　给出一个正整数n，求一个和最大的序列a0，a1，a2，……，ap，满足n=a0>a1>a2>……>ap且ai+1是ai的约数，输出a1+a2+……+ap的最大值
输入格式
　　输入仅一行，包含一个正整数n
输出格式
　　一个正整数，表示最大的序列和，即a1+a2+……+ap的最大值
样例输入
10
样例输出
6
看了一下他们的做法，思路都是大同小异，取出因数最大的保存，然后因子是1的时候停止，然后输出长度
'''
n = int(input())
res = []
path = []



def max_len(num):
    for i in range(1, num + 1):
        if num % i == 0:
            path.append(i)
    fac = max(path)
    res.append(fac)

    if num == 1:
        return
    else:
        max_len(fac)



max_len(n)
print(n, res)