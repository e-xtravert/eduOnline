# @Time    : 2023/3/16 14:25
'''
问题描述
　　用递归函数实现二分法查找数组元素。
　　补充：要求给定数组采用如下代码定义
　　int data[200];
　　for (i=0; i<200; i++）
　　data[i]=4*i+6;
输入格式
　　输入一个待查找的整数（该整数一定在数组data中）。
输出格式
　　该整数在数组中的指标。
样例输入
一个满足题目要求的输入范例。
例1：
262
例2:
438
例3:
774
样例输出
与上面的样例输入对应的输出。
例1：
64
例2:
108
例3:
192
数据规模和约定
　　输入数据中每一个数的范围。
　　输入数据必须满足4*i＋6，i＝0,1,2,3,...,198,199。
'''

n = int(input())
nums = [4 * i + 6 for i in range(200)]


def check(num):
    if num >= n:
        return 1
    else:
        return 0


l = 0
r = len(nums)
while l < r:
    mid = (l + r) // 2
    if check(nums[mid]) == 1:
        r = mid  # 这里 - 1 结果会小1
    else:
        l = mid + 1

# print(n, nums[64], l)  # 262
print(l)