# @Time    : 2024/3/3 12:06
# leetcode733 图像渲染
from queue import Queue


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 乍一看是bfs
        # 题解一看都可以 bfs

        # 起始颜色和目标颜色相同，返回原图
        if color == image[sr][sc]:
            return image
        # 设置四个方向的偏移量
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        # 用的第二种方法使用队列 把起始点放进去 注意只放了坐标点而不是坐标值
        que = Queue()
        que.put((sr, sc))

        # 初始颜色
        origin_color = image[sr][sc]
        # 当队列不为空的时候
        while not que.empty():
            # 取出队列点
            point = que.get()
            image[point[0]][point[1]] = color  # 取出的是一个坐标点 就是一个元组list
            # 遍历四个方向
            for direction in directions:
                # 新的坐标点
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                # 判断是否符合条件 在区域内 并且是相同的点
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == origin_color:
                    que.put((new_i, new_j))

        return image
