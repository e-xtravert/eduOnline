# @Time    : 2023/4/8 9:58
'''
给定 a, b，求 1 ≤ x < a
b 中有多少个 x 与 a
b 互质。由于答案可能很大，你
只需要输出答案对 998244353 取模的结果。
【输入格式】
输入一行包含两个整数分别表示 a, b，用一个空格分隔。
【输出格式】
输出一行包含一个整数表示答案。
2 5
16
12 7
11943936
'''
a, b = map(int, input().split())
cnt = 0


def zhi(n):
    for j in range(2, n):  # 这里忘记缩小一点了 不然还能优化
        if n % j == 0 and a ** b % j == 0:
            return False
    return True


# 公因式只有1的两个数互质
for i in range(2, a ** b):
    # print(i)
    if zhi(i):
        cnt += 1


print(cnt)