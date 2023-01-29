'''
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）

数据范围：0 \le n \le 15000≤n≤1500,树上每个节点的val满足 |val| <= 1500∣val∣<=1500
要求：空间复杂度：O(n)O(n)，时间复杂度：O(n)O(n)

step 1：首先判断二叉树是否为空，空树没有打印结果。
step 2：建立辅助队列，根节点首先进入队列。不管层次怎么访问，根节点一定是第一个，那它肯定排在队伍的最前面，初始化flag变量。
step 3：每次进入一层，统计队列中元素的个数，更改flag变量的值。因为每当访问完一层，下一层作为这一层的子节点，一定都加入队列，而再下一层还没有加入，因此此时队列中的元素个数就是这一层的元素个数。
step 4：每次遍历这一层这么多的节点数，将其依次从队列中弹出，然后加入这一行的一维数组中，如果它们有子节点，依次加入队列排队等待访问。
step 5：访问完这一层的元素后，根据flag变量决定将这个一维数组直接加入二维数组中还是反转后再加入，然后再访问下一层。
'''


from sys import flags
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#

import queue

class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        head = pRoot
        res = []
        if not head:
            return res
        # 用队列存储
        temp = queue.Queue()
        temp.put(head)
        flag = True
        while not temp.empty():
            row = [] # 记录二叉树的行
            flag = not flag
            n = temp.qsize() # 记录每一层的大小，也是要循环的次数

            for i in range(n):
                p = temp.get()
                row.append(p.val)
                if p.left:
                    temp.put(p.left)
                if p.right:
                    temp.put(p.right)
            if flag: # flag奇数行反转，最开始就是奇数行设置为true，偶数行就不反转，反转设置在最后
                row = row[::-1]
            res.append(row)

        return res
'''
打印二叉树
'''
import queue


class Solution:
    def PrintFromTopToBottom(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            # 如果是空，则直接返回空数组
            return res
        # 队列存储，进行层次遍历
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            res.append(cur.val)
            # 若是左右孩子存在，则存入左右孩子作为下一个层次
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        return res
