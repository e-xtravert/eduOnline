#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#

def merge(A, m, B, n):
    # write code here
    # 归并排序
    i = 0
    j = 0
    p = 0
    C = [0 for i in range(m + n)]
    while i < m and j < n:
        if A[i] <= B[j]:
            C[p] = A[i]
            i += 1
        else:
            C[p] = B[j]
            j += 1

        p += 1

    while i < m:
        C.append(A[i])
    while j < n:
        C[p] = B[j]
        j += 1
        p += 1

    # for i in range(0, len(C) - 1):
    #     A[i] = C[i]
    print(C)
# 在函数外面调用函数的时候要把self变量去掉
merge([4, 5, 6], 3, [1, 2, 3, 7, 9], 5)
