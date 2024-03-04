# @Time    : 2024/3/3 12:14
# dfs 栈做法 具体解释可以参考bfs文件夹下的new_color部分
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # # 乍一看是bfs
        # # 题解一看都可以 bfs

        # return image
        # if color == image[sr][sc]:
        #     return image
        # stack, old_color = [(sr, sc)], image[sr][sc]
        # while stack:
        #     point = stack.pop()
        #     image[point[0]][point[1]] = color
        #     for new_i, new_j in zip((point[0], point[0], point[0] + 1, point[0] - 1),
        #                             (point[1] + 1, point[1] - 1, point[1], point[1])):  # 全部的x和y坐标
        #         if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == old_color:
        #             stack.append((new_i, new_j))

        # return image

        # dfs递归法
        if image[sr][sc] != color:
            old_color, image[sr][sc] = image[sr][sc], color  # 旧的染色 新的再变成旧的
            for i, j in zip((sr, sr + 1, sr, sr - 1), (sc + 1, sc, sc - 1, sc)):
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == old_color:
                    self.floodFill(image, i, j, color)
        return image
