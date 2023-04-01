# @Time    : 2023/4/1 22:58
'''
最小公倍数
'''

n = int(input())
res = []
for i in range(69720375229712477164533808935312303556800):
    for j in range(1, n + 1):
        if i % j == 0:
            res.append(i)

print(res[0])