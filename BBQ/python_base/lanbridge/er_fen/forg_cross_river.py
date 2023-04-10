# @Time    : 2023/4/7 10:04
'''
https://www.lanqiao.cn/problems/2097/learning/?first_category_id=1&sort=students_count&second_category_id=3&name=%E9%9D%92%E8%9B%99%E8%BF%87%E6%B2%B3
5 1
1 0 1 0
output
4
input
50 134053
50 134053 3168 7656 7692 3922 5732 3197 9606 8858 9669 2089 158 5681 2907 3769 7600 3940 7574 9337 8902 8023 2877 8559
3841 3192 4128 4898 6745 1280 229 7744 8794 5193 7300 6335 7661 7358 4821 2351 4083 5358 9188 1058 2193 8487 8900 6149
2761 2584 4557
output
50
'''
# 我tm 照着答案写的 为毛不通过 笑死
# r, x = map()
# 左移右移不是直观的乘除 而是要在二进制的角度下 左移右移
# print(2 + 4 >> 2)
# print(6 >> 3)

n, m = map(int, input().split())  # 问题好像是出在这里 他有些测试数据是不按这个格式来的
lis = [int(i) for i in input().split()]
# sum_ = [0 for _ in range(n)]
# sum_1 = [0 for _ in range(n)]
sum_1 = [0] * n

# for i in range(len(lis)):
#     sum_[i + 1] = sum_[i] + lis[i]  # 前缀和

for i, x in enumerate(lis):
    sum_1[i + 1] = sum_1[i] + x  # 前缀和


def check(y):
    for i in range(n - y):
        if sum_1[i + y] - sum_1[i] < 2 * m:  # 这里变量混了 结果半天没看出哪儿出错 变量尽量要不同 区分开
            return False
    return True


l, r = 0, n
while l < r:
    mid = l + r >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1

print(l)

