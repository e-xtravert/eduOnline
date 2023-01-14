'''
输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。
数据范围： 0 \le n \le 10000≤n≤1000，-1000 \le 节点值 \le 1000−1000≤节点值≤1000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

如输入{1,3,5},{2,4,6}时，合并后的链表为{1,2,3,4,5,6}，所以对应的输出为{1,2,3,4,5,6}，转换过程如下图所示：
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # write code here
        # 哈希表
        res = []
        # python的字典函数dictionary()
        hash = dict()

        # range（a, b）从a到b不包含b，循环次数是b-a
        for i in range(0, len(numbers)):
            temp = target - numbers[i]
            if temp not in hash:
                hash[numbers[i]] = i
            else:
                res.append(hash[temp] + 1)
                res.append(i + 1)
                break

        # print(hash,res)
        return res

