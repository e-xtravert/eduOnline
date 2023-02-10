'''
NC109 岛屿数量
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
例如：

bfs解法通常需要一个队列，弹出队头进行操作，然后再入队进行判断之类等等等等
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型

#
from queue import Queue, LifoQueue, PriorityQueue


class Solution:
    def solve(self, grid: List[List[str]]) -> int:
        # write code here
        n = len(grid)
        # 空矩阵情况
        if n == 0:
            return 0

        m = len(grid[0])
        count = 0  # 记录岛屿数

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":

                    count += 1  # 岛屿数量
                    grid[i][j] = "0"  # 遇到1全部置为0
                    q = Queue()  # 记录后续bfs的坐标
                    q.put([i, j])

                    while not q.empty():  # 只要q.empty()不为空就会循环
                        temp = q.get()  # 获取队头
                        row = temp[0]
                        col = temp[1]

                        # 四个方向依次检查：不越界且为1
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            q.put([row - 1, col])
                            grid[row - 1][col] = "0"
                        if row + 1 < n and grid[row + 1][col] == "1":
                            q.put([row + 1, col])
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            q.put([row, col - 1])
                            grid[row][col - 1] = "0"
                        if col + 1 < m and grid[row][col + 1] == "1":
                            q.put([row, col + 1])
                            grid[row][col + 1] = "0"

        return count
