'''
描述
给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

数据范围：0\le arr.length \le 10^50≤arr.length≤10
5
 ，0 < arr[i] \le 10^50<arr[i]≤10
5
'''



import sys

for line in sys.stdin:
    a = line.split() # 默认获取到的是字符串格式
    print(int(a[0]) + int(a[1]))
# 给的答题板是上面的内容，结果重置了一下代码恢复正常了
# 双指针和哈希的结合使用
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr: List[int]) -> int:
        # write code here
        # pre = 0
        # cur = 0

        # hash = dict()

        # for i in range(0, len(arr) - 1):
        #     for j in range(0, len(arr) - 1):
        #         if hash[arr[j]] <= 1:
        #             hash[arr[j]] = 1
        #             j += 1
        #             cur = j

        #     i += 1
        #     pre = i

        # return cur - pre
        mp = dict()
        left = 0  # 在其他域用到的变量最后main里面还需要就要在外面先定义一个变量，再去用
        res = 0  # 一般结果都用res，在外面定义了，函数里面用到最后也能返回出去
        for right in range(len(arr)):
            if arr[right] in mp:
                mp[arr[right]] += 1
            else:
                mp[arr[right]] = 1

            while mp[arr[right]] > 1:
                mp[arr[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res






