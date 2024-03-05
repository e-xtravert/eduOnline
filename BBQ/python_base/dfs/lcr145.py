# @Time    : 2024/3/5 21:00
# 判断对称二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True

        # 这样其实是判断两个子树是否相同 并没有对称
        # elif root.left != self.checkSymmetricTree(root.right) or \
        #    root.right != self.checkSymmetricTree(root.left):
        #    return False

        # return root

        def recur(l, r):
            # 其实前面的 都算终止条件 最后的是操作
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return recur(l.left, r.right) and recur(l.right, r.left)

        return not root or recur(root.left, root.right)