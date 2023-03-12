'''

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用bfs求到的就是最小的，为什么呢？是不是因为是第一个出现的最短的，还是需要加一个vis判断是否访问过，然后 == 表示 is
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queen = []
        res = 1  # 什么都没有也算一层
        queen.append(root)

        while queen:
            # res += 1  加的位置要在下面循环结束，确定当前节点确实是一个有效节点
            size = len(queen)
            for i in range(size):  # 这里循环有必要吗？每次都放一个节点，不全部放进去，会造成不能得出最短的结果，那就会是第一个放进去的分支上的最短的
                node = queen.pop(0)  # 弹出数组最前方的元素

                if node.left is None and node.right is None:
                    return res

                if node.left is not None:
                    queen.append(node.left)

                if node.right is not None:
                    queen.append(node.right)

            res += 1  # while循环一次确定一个点

        return res
