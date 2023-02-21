'''
AB23 素因子
kotori拿到了一些正整数。她决定从每个正整数取出一个素因子。但是，kotori有强迫症，她不允许两个不同的正整数取出相同的素因子。
她想知道，最终所有取出的数的和的最小值是多少？
若一个数有且仅有两个因子，则称其是素数。显然1只有一个因子，不是素数。

输入：4
12 15 28 22
输出17
分别取3，5，7，2，可保证取出的数之和最小

不能取出不同的最小的素因子了，即为无合法取值的情况
'''
import math

n = int(input())
lis = list(map(int, input().split()))

# prim = dict()
# for i in lis:
#     prim[i] = []
prim = [[] for i in range(n)]
factor = dict()


# # get factors
# def get_factor(num):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factor[num] = i
#
#
# # check prime
# def prime(num):
#     if num == 1:
#         print(0)
#     elif num == 2:
#         print(num)
#     for i in range(2, num + 1):
#         if (num % i) != 0:
#             prim[num] = i
#

# get all factors

# for j in range(len(lis)):
#     get_factor(lis[j])
#
# for k in range(len(factor)):
#     prime(factor[k])
# 目前这个程序还是有问题的，抛出错误是vis[prim[y][i]]没有初始化，要先将其初始化为0，后面再去做

# 判断素数，注意那个循环的用法，在后面+1和在sqrt参数+1问题
def is_prime(num):
    if num == 1:
        return 0
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def get_factor(num, x):
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                prim[x].append(i)
            # if i * i != num and is_prime(num // i):
            #     prim[x].append(num // i)


res = 0x3f3f3f3f
flag = 0
sums = 0
vis = dict()


def dfs(y):
    if y == n - 1:
        global res
        global sums
        res = min(res, sums)
        global flag
        flag = 1
        return
    sums = 0
    for i in range(len(prim[y])):
        if not bool(vis[prim[y][i]]):
            sums += prim[y][i]
            vis[prim[y][i]] = 1
            dfs(y + 1)
            sums -= prim[y][i]
            vis[prim[y][i]] = 0


for i in range(n):
    get_factor(lis[i], i)
get_factor(lis[0], 0)
dfs(0)
if flag == 1:
    print(res)
else:
    print(-1)

# prim[0].append(3)
# prime(lis[0])
# get_prime(lis[0])
print(prim)
