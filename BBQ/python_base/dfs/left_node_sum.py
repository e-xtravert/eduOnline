# @Time    : 2024/3/4 22:32
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# leetcode404
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # res = 0
        # def dfs(root):
        #     if not root:
        #         return 0
        #     else:
        #         res += root.val
        #         dfs(root.left)

        # 左右节点都遍历了 只是右子节点不计数
        isLeftNode = lambda node: not node.left and not node.right  # 判断是不是叶子节点

        # def dfs(node: TreeNode) -> int:
        #     ans = 0
        #     if node.left:
        #         ans += node.left.val if isLeftNode(node.left) else dfs(node.left)
        #     if node.right and not isLeftNode(node.right):
        #         ans += dfs(node.right)  # 只遍历 不计数右子节点 计数右子树的左子节点

        #     return ans

        # return dfs(root) if root else 0

        # 广度优先写一个

        if not root:
            return 0

        q = collections.deque([root])
        ans = 0

        while q:
            node = q.popleft()
            if node.left:
                if isLeftNode(node.left):
                    ans += node.left.val
                else:
                    q.append(node.left)
            if node.right:
                if not isLeftNode(node.right):
                    q.append(node.right)

        return ans

