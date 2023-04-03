# @Time    : 2023/3/29 9:38
'''
给定一个正整数  。你可以对
将该位数字加 1 。如果该位数字已经是 9 , 加 1 之后变成 0 。
将该位数字减 1 。如果该位数字已经是 0 , 减 1 之后变成 9 。
你现在总共可以执行 1 号操作不超过  次, 2 号操作不超过  次。 请问你最大可以将
123 1 2
933
'''
# 对两个操作不能混用 要么全用操作1 要么全用操作2
# 做题要根据题目给出的信息模拟出测试用例 不要被题目给的测试用例先入为主带偏了
# 做题首先要有思路 不然 答案都看不懂
# https://www.luogu.com.cn/problem/P8801
n, a, b = map(int, input().split())
ans = 0
n = str(n)
# print(n)


def dfs(i, v):
    global a, b, ans
    if i >= len(str(n)):
        ans = max(ans, v)
        return
    x = int(n[i])
    if n[i]:
        t = min(a, 9 - x)
        a -= t
        dfs(i + 1, v * 10 + x + t)

        a += t
        if b > x:
            b -= x + 1
            dfs(i + 1, v * 10 + 9)
            b += x + 1
    # else:
    #     ans = max(ans, v)


dfs(0, 0)
print(ans)

'''
一个题解
n,a,b=map(int,input().split())
li=list(map(int,list(str(n))))
res=0
def dfs(i,v,a,b):
    global res
    if i <len(li):
        x=li[i]
        d=min(a,9-x)
        dfs(i+1,v*10+x+d,a-d,b)
        if b>=x+1:
            dfs(i+1,v*10+9,a,b-x-1)
    else:
        res=max(res,v)
dfs(0,0,a,b)
print(res)
'''