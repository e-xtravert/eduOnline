'''
描述
给定一棵二叉树，分别按照二叉树先序，中序和后序打印所有的节点。

数据范围：0 \le n \le 10000≤n≤1000，树上每个节点的val值满足 0 \le val \le 1000≤val≤100
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
样例解释：
如图二叉树结构
示例1
输入：
{1,2,3}
返回值：
[[1,2,3],[2,1,3],[2,3,1]]
说明：
如题面图
示例2
输入：
{}
返回值：
[[],[],[]]
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
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self, root: TreeNode) -> List[List[int]]:
        # write code here
        # 本质就是函数回调，属于递归一类的题目
        def preorder(root):
            if not root:
                return []
            else:
                return [root.val] + preorder(root.left) + preorder(root.right)

        def midorder(root):
            if not root:
                return []
            else:
                return midorder(root.left) + [root.val] + midorder(root.right)

        def lastorder(root):
            if not root:
                return []
            else:
                return lastorder(root.left) + lastorder(root.right) + [root.val]

        return [preorder(root), midorder(root), lastorder(root)]









