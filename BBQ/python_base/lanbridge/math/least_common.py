# @Time    : 2023/4/3 17:09
'''
最小公倍数
'''

# 请在此输入您的代码
# 两两 最小公倍数
# 最小公倍数 * 最大公约数 = 两数乘积
# 最大公约数 = 辗转相除法

def f(x):
    if x < 3: return x
    i = 6
    for j in range(4,x + 1):
        a, b = i, j
        while b:
            # print(a,b)
            a, b = b, a % b
        # 最大公约数a  a b最小公倍数 a*b/a
        i = (i * j) // a
    return i

n = int(input())
print(f(n))