# @Time    : 2024/3/7 9:52
# str = '9854256'
# print(str[0:2])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 直接遍历一下 然后数组排序
        # self.res = []

        # 在不同的函数种还是要用self全局
        self.res = []
        min_ = float('inf')

        self.dfs(root)
        for i in range(len(self.res) - 1):
            min_ = min(abs(self.res[i] - self.res[i + 1]), min_)
            print(min_)

        return min_

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)