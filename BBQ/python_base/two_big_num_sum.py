# str = 'this is test sentence'
#
# print(str.zfill(30))
#
# print(ord('3'))
#
# res = '142151545423'
#
# print(res[::-1])

'''
描述
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。

数据范围：s.length,t.length \le 100000s.length,t.length≤100000，字符串仅由'0'~‘9’构成
要求：时间复杂度 O(n)O(n)

'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self , s: str, t: str) -> str:
        # write code here
        maxlen = max(len(s), len(t))
        s = s.zfill(maxlen)
        t = t.zfill(maxlen)

        res = ''
        carry = 0
        for i in range(-1, -maxlen-1, -1):
            # -96是因为是Unicode编码，数字的编码要减去96
            temp = ord(s[i]) + ord(t[i]) - 96 + carry
            if temp >= 10:
                temp -= 10
                carry = 1
            else:
                carry = 0
            res += str(temp)
        if carry:
            # 最后要有进到最高位就要最前面补一个1
            res += str(1)
        # 计算是从后往前加的计算，但是写入结果时是加在前面的，所以下面这个是倒序输出的意思
        return res[::-1]