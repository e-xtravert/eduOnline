'''
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
nums = [int(i) for i in input().split()]

path = []  # put middle process
res = []  # result
v = [0] * len(nums)


def backtrack(nums, vis):
    if len(path) == len(nums):
        res.append(path.copy())  # 必须copy不然出事
        return

    for i in range(len(nums)):  # 使用length不行呀
        if vis[i] == 1:  # 后面把完整数组放进去了，挨个选择，自然要把已经选了的不要了
            continue
        vis[i] = 1
        path.append(nums[i])
        backtrack(nums, vis)  # 数组放进去重新挨个选择
        path.pop(-1)
        vis[i] = 0


ans = set(res)
backtrack(nums, v)
print(res, res)