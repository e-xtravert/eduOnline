'''
题目描述 找出所有相加之和为n的k个数的组合。组合中只允许含有1-9的正整数，并且每种组合中不存在重复的数字。
如输入为k = 3、n = 9，则返回结果为[[1, 2, 6], [1, 3, 5], [2, 3, 4]]。
首先，题目给出的输入形式与第四个问题-组合相同。不同的是，前者要求返回的是具体组合，而本题要求返回的组合满足和为n的条件，再综合上一题的解答。
另外，由于题目要求组合中只允许含有1-9的正整数，则需要再对其中的某些情况剪枝。程序如下：
'''
# 指定长度

k, n = map(int, input().split())
path = []
res = []


def path_sum(arr):
    s = 0
    for i in arr:
        s += i
    return s


# 当然把n和k放进函数里面也行
def backtrack(start):
    if path_sum(path) >= n:
        if path_sum(path) == n and len(path) == k:  # 指定长度的
            res.append(path[:])

    for i in range(start, n):
        if i > 9:
            return
        path.append(i)
        backtrack(i + 1)
        path.pop(-1)


backtrack(1)
print(res)
