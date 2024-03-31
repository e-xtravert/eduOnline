# @Time    : 2024/3/23 16:56
res = []


def dfs(path, n, k, begin, res):
    if len(path) == k:
        res.append(path[:])
        return

    for i in range(begin, n + 1):
        path.append(i)

        dfs(path, n, k, i + 1, res)
        path.pop()
n = 4
k = 2

dfs([], n, k, 1, res)
print(res)