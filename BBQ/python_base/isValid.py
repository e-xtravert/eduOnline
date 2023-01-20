# arr = ['one', 'two', 'three']
#
# for i, element in enumerate(arr):
#     print(element)
#
# print(arr[-1])

'''
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s: str) -> bool:
        # write code here
        st = []
        for i, element in enumerate(s):
            if element == "(":
                st.append(')')
            if element == "{":
                st.append('}')
            if element == '[':
                st.append(']')

            elif len(st) == 0:
                return False

            elif (st[-1] == element):
                st.pop()

        return len(st) == 0
