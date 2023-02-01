'''
leetcode 77 组合
回溯法格式：
    回溯法函数
        判断条件，收集结果
        循环 起点是当前树的深度到树的总深度
            填装结果
            递归调用回溯函数
            回溯精髓，返回上一步，数组pop
    调用回溯函数
    return 结果
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        path = []  # 记录组合，用来回溯的一个容器，体现
        res = []

        def backtracking(n, k, start_index):
            if len(path) == k:
                # 相当于path.copy()，直接用path不行，path是动态变化的，要用深拷贝
                res.append(path[:])
                return
            # path.append(start_index)
            # 这里是当前到树的深度的位置，计算比较细节
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)  # 把值装进去
                backtracking(n, k, i + 1)  # 写成下面的形式会有重复的值
                # backtracking(n, k, start_index + 1)
                # 如果上面的判断条件退出，则这里就弹出最开始的，从第二棵子树开始，即为2开头的组合
                path.pop()  # 回溯精髓所在

        backtracking(n, k, 1)  # 从1开始
        return res




