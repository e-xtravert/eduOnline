'''
进制转换 牛客nc112

'''


#

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 进制转换
# @param M int整型 给定整数
# @param N int整型 转换到的进制
# @return string字符串
#
class Solution:
    def solve(self, M: int, N: int) -> str:
        # write code here 取模运算 是几进制，取多少的模即可
        flag = False
        s = '0123456789ABCDEF'  # 一个小技巧，取模之后返回其中对应的值，转换几进制余数恰好就是以余数为下标的s中对应的值
        res = ''
        if M < 0:
            flag = True  # 用flag是先需要对m操作，然后再判断正负加符号
            M = abs(M)

        while M:
            res = s[M % N] + res
            M //= N

        if flag:
            res = '-' + res

        return res
