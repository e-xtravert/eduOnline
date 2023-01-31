'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

数据范围：1 \leq n \leq 401≤n≤40
要求：时间复杂度：O(n)O(n) ，空间复杂度： O(1)O(1)
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self, number: int) -> int:
        # write code here
        # python用不了递归？
        # if number == 0:
        #     return 1
        # if number == 1:
        #     return 1

        # return jumpFloor(number - 1) + jumpFloor(number - 2) 或者直接把他的方法删掉，然后自定义函数时可以return自己的


        if number <= 1:
            return 1

        res = 0
        a = 1
        b = 1
        # 下面是求n的数，循环次数要从1开始就要使用n，如果是0开始就循环到n+1见上面
        for i in range(2, number + 1):
            res = a + b
            a = b
            b = res
        return res


# 递归法
class Solution:
    def jumpFloor(self , number: int) -> int:
        #从0开始，第0项是1，第一项是1
        if number <= 1:
            return 1
        #根据公式递归调用函数，原来是要使用self调用函数
        return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


# fibonacci数列
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Fibonacci(self, n: int) -> int:
        # write code here
        # 不知道为什么不行了这个
        # if n <= 2:
        #     return 1
        # return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

        if n <= 2:
            return 1
        res = 0
        a = 1
        b = 1
        # 下面是求n的数，循环次数要从1开始就要使用n，如果是0开始就循环到n+1见上面
        for i in range(2, n):
            res = a + b
            a = b
            b = res
        return res


# 第n编递归还是不能秒了
import sys

# 实际还是fabonicci
inp = int(input())

# print(inp)



if inp <= 1:
    print(1)
else:
    res = 0
    a = 1
    b = 1

    for i in range(2, inp + 1):
        res = a + b
        a = b
        b = res

    print(res)
