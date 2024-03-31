# @Time    : 2024/3/25 21:47
coins = [1, 2, 5]
amount = 5
size = len(coins)
res = []


def dfs(nums, target, path, begin, res):
    if sum(path) == target:
        res.append(path[:])
        return
    if sum(path) > target:
        return

    for i in range(begin, len(nums)):
        path.append(nums[i])

        dfs(nums, target, path, begin + 1, res)
        path.pop()


dfs(coins, amount, [], 0, res)
print(res)