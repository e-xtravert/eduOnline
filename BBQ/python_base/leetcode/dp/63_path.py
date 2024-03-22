# @Time    : 2024/3/12 11:42
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * m
        if obstacleGrid[0][0] == 0:  # 判断边缘是路障 不如判断不是路障的情况
            f[0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0  # 如果有路障就是0
                    continue

                if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]  # 滚动数组

        return f[-1]