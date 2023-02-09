'''
牛客nc141

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str: str) -> bool:
        # write code here
        leng = len(str)
        for i in range(leng):
            if str[i] != str[leng - 1 - i]:
                return False

        return True
