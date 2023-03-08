'''
编写一个数组求和函数void Add(int n, int* a1, int* a2, int* result); 其中n<100是数组长度，a1是第一个数组，a2是第二个数组，result是a1和a2的和。
假设a1={2, 4, 5, 8}, a2={1, 0, 4, 6}，则result={3, 4, 9, 14};
　　编写main函数测试该函数的正确性。依次输入n, a1, a2, 输出result。
输入：
4
2 4 5 8
1 0 4 6

输出：
　　3 4 9 14
'''
n = int(input())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
res = []


def summatiion(n, a1, a2):
    for i in range(n):
        res.append(a1[i] + a2[i])

    return res


ans = summatiion(n, arr1, arr2)
for i in range(len(ans)):
    if i == len(ans) - 1:
        print(ans[i])
    else:
        print(ans[i], end=' ')