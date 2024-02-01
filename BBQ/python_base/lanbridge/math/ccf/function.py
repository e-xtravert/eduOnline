# @Time    : 2024/2/1 15:38

# coding=utf-8
def reconstruct_polynomial(n, m):
    # Step 1: 计算最高幂次k
    k = 0
    temp_m = m
    coefficients = []
    while temp_m > 0:
        remainder = temp_m % n
        quotient = temp_m // n
        coefficients.append(quotient)
        temp_m = quotient
        k += 1

    # Step 2: 计算每一项的系数
    polynomial = ''
    for i in range(k - 1, -1, -1):
        if coefficients[i] > 0:
            if i != k - 1:
                polynomial += '+'
            polynomial += str(coefficients[i])
            if i > 1:
                polynomial += 'x^' + str(i)
            elif i == 1:
                polynomial += 'x'

    # Step 3: 判断是否需要输出"x"
    if n > 1:
        polynomial += '+1'

    return polynomial


# 输入n和m
n, m = map(int, input().split())
# 调用函数进行还原并输出多项式
polynomial = reconstruct_polynomial(n, m)
print(polynomial)