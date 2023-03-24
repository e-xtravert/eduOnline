# @Time    : 2023/3/24 8:53
'''

input
5 2 3
1 2 3 4 5
2
-2
output
3 4 5
1 2 3

anther
5 9 3
33 100 51 29 98
-1
4
-2
-5
-2
-1
-1
2
4

98 33 100
29 98 33
100 51 29
100 51 29
98 33 100
29 98 33
51 29 98
98 33 100
29 98 33

'''

# 思路很简单 就是用两个数组 一个数组存放数据 另一个数组存放 他的反转数列 然后用两个数组的拼接模拟 数组移动
# 但是很可惜 错了 应该是模拟出错了
n, m, k = map(int, input().split())
lis = [int(i) for i in input().split()]  # 别搞错了
lis.reverse()
lis_ = lis.copy()
lis.reverse()

option = []
res = []
for i in range(m):
    option.append(int(input()))

# 正数表示向左移动 负数向右移动
for i in option:
    if i >= 0:
        lis1 = lis[i:len(lis)]
        lis_1 = lis_[len(lis_) - i:len(lis)]
        lis_1.reverse()
        lis2 = lis1 + lis_1
        res.append(lis2[:k])
        # print(' '.join(str(i) for i in lis2[:k]))
    else:
        lis[i:].reverse()
        lis_1 = lis[:i]
        lis2 = lis + lis_1
        res.append(lis2[:k])
        # print(' '.join(str(i) for i in lis2[:k]), end='')

print(option, lis, lis_, k, res)
