# @Time    : 2023/3/27 22:55
'''
顺子日期
2022年中一共有多少个
'''
res = 0


def zero(date):
    if date < 10:
        return '0' + str(date)
    else:
        return str(date)


for i in range(12):
    for j in range(31):
        d = zero(i) + zero(j)
        for k in range(len(d) - 2):
            if int(d[k]) + 1 == int(d[k + 1]) and int(d[k]) + 2 == int(d[k + 2]):
                res += 1

print(res)
