'''
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树层序遍历的结果是
[
[3],
[9,20],
[15,7]

]
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型二维数组
#

import queue
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # write code here
        res = []
        # if root empty return []
        if not root:
            return res
        # else put in queue
        q = queue.Queue()
        q.put(root)
        # cur reference the element now
        cur = None
        while not q.empty():
            # mark the row of tree_node
            row = []
            # get the loop times, the size of the queue
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                row.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            res.append(row)
        return res


