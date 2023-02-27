'''
本题的序列可包含重复数字，按要求返回所有不重复的全排列。
如输入数组为[1, 1, 2]，则返回结果为[[1, 1, 2], [1, 2, 1], [2, 1, 1]]。
'''

nums = [int(i) for i in input().split()]
v = [0] * (len(nums) + 1)
res = []
path = []


def backtrack(num, vis):
    if len(path) == len(num):
        res.append(path.copy())
        return

    for i in range(len(num)):
        if i > 0 and num[i] == num[i - 1] and not vis[i - 1]:  # i从第二个数开始，如果和前一个值相等，或者前一个值未访问
            continue
        if vis[i] == 1:
            continue
        vis[i] = 1
        path.append(num[i])
        backtrack(num, vis)
        path.pop(-1)  # 容易把这个忘了
        vis[i] = 0


backtrack(nums, v)
print(res)

