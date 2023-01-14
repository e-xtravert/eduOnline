'''
描述
有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。

给定一个整数数组 a ,同时给定它的大小n和要找的 k ，请返回第 k 大的数(包括重复的元素，不用去重)，保证答案存在。
要求：时间复杂度 O(nlogn)O(nlogn)，空间复杂度 O(1)O(1)
数据范围：0\le n \le 10000≤n≤1000， 1 \le K \le n1≤K≤n，数组中每个元素满足 0 \le val \le 100000000≤val≤10000000
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class Solution:
    def findKth(self, a: List[int], n: int, K: int) -> int:
        # write code here
        # quick_sort from bigger to smaller

        def quick_sort(arr, low, high):
            # 第一次自己写就是漏了这个（if low < high），导致排序出现混乱
            if low < high:
                partition_index = partition(arr, low, high)
                # 第三次查错发现自己下面这个回调函数用的是partition，服了
                quick_sort(arr, low, partition_index - 1)
                # 第一次查错写下面这个也没注意，这表示后面那部分区间做排序
                quick_sort(arr, partition_index + 1, high)
                # 第二次查错下面这个也写错了，写到if函数外面去了，表示如果low>=high返回了
                return arr

        # partition method
        def partition(arr, low, high):
            pivot = arr[low]

            while low < high:
                while low < high and arr[high] <= pivot:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] >= pivot:
                    low += 1
                arr[high] = arr[low]

            arr[low] = pivot
            return low

        lists = quick_sort(a, 0, n - 1)

        print(lists, K, lists[K - 1])
        return lists[K - 1]
