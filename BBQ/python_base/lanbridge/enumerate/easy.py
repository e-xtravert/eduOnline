# @Time    : 2023/3/27 23:04
'''
找到一个2019的整倍数 每一个数位都是奇数的最小数
'''
# todo
res = []
for i in range(2019, 1000000):  # 这里也是试探了几个数
    if i % 2019 == 0:
        for j in range(len(str(i))):
            if int(str(i)[j]) % 2 != 0:
                if j == len(str(i)) - 1:
                    res.append(i)
                else:
                    continue
            else:
                break


print(res[0])