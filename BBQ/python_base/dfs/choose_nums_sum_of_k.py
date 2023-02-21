'''
题目描述
给定整数a1、a2、…an，判断是否可以从中选出若干数，使它们的和恰好为K。
输入
首先，n和k，n表示数的个数，k表示数的和。
接着一行n个数。
（1<=n<=20,保证不超int范围）
输出
如果和恰好可以为k，输出“YES”，并按输入顺序依次输出是由哪几个数的和组成，否则“NO”
样例输入
4 13
1 2 4 7
样例输出
YES
2 4 7
'''
# 这道也是存在问题的，没有结果，建议debug一下，然后主要关注dfs里面的for循环问题,没做出来，看part_sum做法吧还是
n, sum_ = map(int, input().split())
lis = [int(i) for i in input().split()]
is_choose = [0 for _ in range(n + 1)]
flag = 0
sum0 = 0
res = []


def dfs(num):
    global flag
    global sum0
    if sum0 >= sum_:
        if sum0 == sum_:
            if flag == 0:
                flag = 1
            if flag:
                print('yes')
                for i in range(n):
                    if is_choose[i]:
                        res.append(lis[i])
    for i in range(num, n):  # 第一次循环结束后num+1，会进入下一个数，所以按理来说会到2开始往后面加的
        sum0 += lis[num]
        is_choose[num] = 1
        dfs(num + 1)
        sum0 -= lis[num]
        is_choose[num] = 0


dfs(0)
if flag == 0:
    print('no')
if flag == 1:
    print(res)



# print(n, lis)
