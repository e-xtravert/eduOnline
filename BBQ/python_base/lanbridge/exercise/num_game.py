'''
ALGO-1005
给定一个1～N的排列a[i]，每次将相邻两个数相加，得到新序列，再对新序列重复这样的操作，显然每次得到的序列都比上一次的序列长度少1，最终只剩一个数字。
　　例如:
　　3 1 2 4
　　4 3 6
　　7 9
　　16
　　现在如果知道N和最后得到的数字sum，请求出最初序列a[i]，为1～N的一个排列。若有多种答案，则输出字典序最小的那一个。数据保证有解。
给定N个数的排列和总和sum,没读懂题目啊，题目说是1 - N的排列，就是说是连续的四个数不同的排列这个意思，不然这猜数字也太难了。
'''
n, m = map(int, input().split())
path = []
res = []


def backtrack(leng, sum):  # leng represents the length of list, it means N that the title gives
    global res
    # if leng == 1:  # if length is 1, the list is sum
    #     return
    # if len(path) < leng:  # if path' length less than N, it means the list is not full,
    #     # and if one of number <= 0, that the one chosen is false, return directly
    #     if sum <= 0:
    #         return
    # if len(path) == leng:  # if path' length is N,the numbers is satisfied
    #     res = path.copy()
    if sum <= 0:
        return
    if leng == 0:
        if len(path) == n:
            res = path.copy()

    for i in range(1, sum):  # maybe there has another cycle in this cycle that traverses the two numbers
        path.append(i)  # put the num into path
        path.append(sum - i)
        backtrack(leng - 2, i)
        backtrack(leng - 2, sum - i)
        path.pop(-1)  # if not satisfied, pop the num
        path.pop(-1)




backtrack(n, m)
print(n, m, res)
