'''
题目描述 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。这里将顺序不同的序列视为不同的组合。
如输入为nums = [1, 2, 3]、target = 4，则返回结果为7、即[[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]。
首先，题目将顺序不同的序列视为不同的组合，则回溯时可以到当前位置的前面去寻找，这与第二个问题-全排列一致。此外，根据输入输出实例，可以在重复选取数组中的元素，
则我们可以在此基础上不使用used数组来判断是否选取重复元素。程序如下：
1 2 3
4
'''

# import path_sum() from combination_4 as path_sum()  想引用一下，但是不知道啥原因不行
lis = [int(i) for i in input().split()]
target = int(input())
res = 0
path = []


def path_sum(arr):
    s = 0
    for i in arr:
        s += i
    return s


def backtrack(arr):
    global res
    if path_sum(path) >= target:
        if path_sum(path) == target:
            res += 1
        return  # 别忘了把return加上，不然无限不循环了

    for i in range(len(arr)):
        path.append(arr[i])
        backtrack(arr)
        path.pop(-1)


backtrack(lis)
print(res)