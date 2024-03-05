# @Time    : 2024/3/5 17:39
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        # 这个翻转真是不好理解呀 当他递归到最深的时候为叶子节点返回了， 和左子节点交换 交换完
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        # 然后这里把上面的交换之后的root返回去了到上一层去
        return root

