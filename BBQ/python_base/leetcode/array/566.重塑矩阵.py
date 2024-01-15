#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
# https://leetcode.cn/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (64.62%)
# Likes:    414
# Dislikes: 0
# Total Accepted:    153.1K
# Total Submissions: 236.9K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x
# c）的新矩阵，但保留其原始数据。
# 
# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
# 
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
# 
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：mat = [[1,2],[3,4]], r = 1, c = 4
# 输出：[[1,2,3,4]]
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[1,2],[3,4]], r = 2, c = 4
# 输出：[[1,2],[3,4]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
# 
# 
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 能转化的话 行列的乘积应该是相等的
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            # 找规律 这种转换的关注下标的关系
            ans = [[0] * c for i in range(r)]
            for x in range(len(mat) * len(mat[0])):
                ans[x // c][x % c] = mat[x // len(mat[0])][x % len(mat[0])]  # 取模的解读：每一行整除之后下一行的模就是列的下标
        
        return ans
# @lc code=end

