'''
自己写的错误多，先看看题解的做法先
'''

# 2022.3.18
# 蓝桥杯算法训练-24点
# 知识点：深度优先搜索算法
# 我的思路：在一个由4个数字组成的列表中，让每一个数字都与其他三个数字进行
# 加减乘除，并将计算得到的结果加入进列表中，同时在列表中删除进行计算的两个数字，
# 通过递归进行，递归出口为列表长度为1的时候。

n = int(input())
nums = [[] for i in range(n)]
for i in range(n * 4):
    nums[i // 4].append(int(input()))


def dfs(arr):
    # print(arr)
    global res, flag, sto  # res为计算结果；flag标记计算结果是否为24；sto用于储存小于24的计算结果
    if flag == 1:  # flag==1说明找到最终结果了
        return
    if len(arr) == 1:  # 递归出口
        res = arr[0]
        if res == 24:
            flag = 1
            sto = [24]  # 当计算结果为24时，直接令sto=[24]
            return
        elif res > 24:  # 计算结果大于24的不要
            return
        else:
            sto.add(res)  # 计算结果小于24的加入集合中，最后取集合最大值得到最终结果
            return

    for i in range(len(arr)):
        a = arr[i]
        arr2 = arr.copy()  # 作用与回溯相同，用了arr2就不需要回溯了
        arr2.pop(i)
        for j in range(len(arr2)):
            b = arr2[j]

            c = a + b  # 加法，把a与b的和加入列表中，同时删除a与b。
            arr2.pop(j)
            arr2.insert(j, c)
            dfs(arr2)
            arr2.pop(j)  # 回溯
            arr2.insert(j, b)  # 回溯

            d = a - b  # 减法
            arr2.pop(j)
            arr2.insert(j, d)
            dfs(arr2)
            arr2.pop(j)  # 回溯
            arr2.insert(j, b)  # 回溯

            e = a * b  # 乘法
            arr2.pop(j)
            arr2.insert(j, e)
            dfs(arr2)
            arr2.pop(j)  # 回溯
            arr2.insert(j, b)  # 回溯

            if b != 0:
                if a % b == 0:
                    f = a // b  # 除法
                    arr2.pop(j)
                    arr2.insert(j, f)
                    dfs(arr2)
                    arr2.pop(j)  # 回溯
                    arr2.insert(j, b)  # 回溯


for arr in nums:
    sto = set([])
    flag = 0
    res = 0
    dfs(arr)
    end = max(sto)
    print(end)
