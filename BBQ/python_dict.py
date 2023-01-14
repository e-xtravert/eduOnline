'''
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

数据范围：2\leq len(numbers) \leq 10^52≤len(numbers)≤10
5
 ，-10 \leq numbers_i \leq 10^9−10≤numbers
i
​
 ≤10
9
 ，0 \leq target \leq 10^90≤target≤10
9

要求：空间复杂度 O(n)O(n)，时间复杂度 O(nlogn)O(nlogn)
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

