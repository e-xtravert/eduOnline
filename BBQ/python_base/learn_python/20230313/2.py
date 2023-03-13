'''
这是一道做优惠券的题目
'''
m, d, w = map(int, input().split())
p = int(input())
cash = []
for i in range(p):
    cash.append(int(input()))


# 满减属于每满100元可以用一张
# 是只能使用两种优惠券吗？题目没说啊
# 无非就是四种情况，优惠券两两组合
def m_d1(num):
    time = min(num // 100, m) + 1
    num = num - min(num // 100, m) * 10
    num = 0.92 * num
    arr = [num, time]
    return arr


def m_d2(num):
    time = min(num // 100, m) + 1
    num = 0.92 * num
    num = num - min(num // 100, m) * 10
    arr = [num, time]
    return arr


def m_w1(num):
    time = min(num // 100, m) + w
    num = num - min(num // 100, m) * 10
    num = num - w * 5
    arr = [num, time]
    return arr


def m_w2(num):
    time = min(num // 100, m) + w
    num = num - w * 5
    num = num - min(num // 100, m) * 10
    arr = [num, time]
    return arr


def d_w1(num):
    time = w + 1
    num = 0.92 * num
    num = num - w * 5
    arr = [num, time]
    return arr


def d_w2(num):
    time = w + 1
    num = num - w * 5
    num = 0.92 * num
    arr = [num, time]
    return arr


for i in range(len(cash)):
    arr1 = m_d1(cash[i])
    arr2 = m_d2(cash[i])
    arr3 = m_w1(cash[i])
    arr4 = d_w1(cash[i])
    arr5 = m_w2(cash[i])
    arr6 = d_w2(cash[i])
    ans = min(arr1[0], arr2[0], arr3[0], arr4[0], arr5[0], arr6[0])
    print(int(ans), end=' ')

    if ans == arr1[0]:
        print(int(arr1[1]))
    if ans == arr2[0]:
        print(int(arr2[1]))
    if ans == arr3[0]:
        print(int(arr3[1]))
    if ans == arr4[0]:
        print(int(arr4[1]))
    if ans == arr5[0]:
        print(int(arr5[1]))
    if ans == arr6[0]:
        print(int(arr6[1]))

# print(m, d,w, p, cash)
