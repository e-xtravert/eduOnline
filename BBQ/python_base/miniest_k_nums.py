'''
给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4(任意顺序皆可)。
数据范围：0\le k,n \le 100000≤k,n≤10000，数组中每个数的大小0 \le val \le 10000≤val≤1000
要求：空间复杂度 O(n)O(n) ，时间复杂度 O(nlogk)O(nlogk)

示例1
输入：
[4,5,1,6,2,7,3,8],4
返回值：
[1,2,3,4]
说明：
返回最小的4个数即可，返回[1,3,2,4]也可以
示例2
输入：
[1],0
返回值：
[]
示例3
输入：
[0,1,2,1,2],3
返回值：
[0,1,1]
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        # 先排序然后输出前k个数

        def quick_sort(arr, left, right):
            if left < right:
                pivot_index = partition(arr, left, right)

                quick_sort(arr, left, pivot_index - 1)
                quick_sort(arr, pivot_index + 1, right)
                return arr

        def partition(arr, left, right):
            pivot = arr[left]

            while left < right:
                while left < right and arr[right] >= pivot:
                    #  如果比基准值大则向前进一位，否则将值赋给左边，
                    #  其实就是找到第一个小于基准值的数， 只不过判断条件反过来了
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= pivot:
                    left += 1
                arr[right] = arr[left]

            arr[left] = pivot
            return left

        lists = quick_sort(input, 0, len(input) - 1)
        new_lists = []
        for i in range(0, k):
            new_lists.append(lists[i])

        return new_lists




