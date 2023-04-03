# @Time    : 2023/3/28 22:51
'''
input
10
output
2 3 5 7
4
'''
n = int(input())
res = []


# 用一个单独的函数求比较合适
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True


for i in range(2, n):
    if isPrime(i):
        res.append(i)
        # print(i, end=' ')
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i])
    else:
        print(res[i], end=' ')

print(len(res))