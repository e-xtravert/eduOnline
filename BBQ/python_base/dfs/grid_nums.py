'''
牛客nc109 岛屿数量，用dfs解法
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数
注意，相邻的1都算同一个岛屿
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    # 深度优先算法
    def dfs(self, grid: List[List[chr]], i: int, j: int):
        # dfs深度优先搜索遍历与i， j相邻的1
        n = len(grid)
        m = len(grid[0])

        grid[i][j] = '0'  # 关键操作，每一次迭代都是置0，0要是字符

        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if i + 1 < n and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j + 1 < m and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)

    def solve(self, grid: List[List[str]]) -> int:
        # write code here
        n = len(grid)  # 记录行数
        # 空矩阵情况
        if n == 0:
            return 0
        m = len(grid[0])  # 记录列数
        count = 0  # 记录岛屿数量
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1  # 计数
                    self.dfs(grid, i, j)
        return count



