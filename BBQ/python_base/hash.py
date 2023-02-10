'''
NC97 字符串出现次数的TopK问题
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
class Solution:
    def topKstrings(self , strings: List[str], k: int) -> List[List[str]]:
        # write code here
        has = dict()
        for i in range(len(strings)):
            if strings[i] not in has:
                has[strings[i]] = 1
            else:
                has[strings[i]] += 1  # 这里必须用else，如果不是则怎样

        return(sorted(has.items(), key=lambda x: (-x[1], x[0])))[:k]  # 最后这个[:k]是截取前k个数



