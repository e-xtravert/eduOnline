'''
给定一个链表，删除链表的倒数第 n 个节点并返回链表的头指针
例如，
给出的链表为: 1\to 2\to 3\to 4\to 51→2→3→4→5, n= 2n=2.
删除了链表的倒数第 nn 个节点之后,链表变为1\to 2\to 3\to 51→2→3→5.

数据范围： 链表长度 0\le n \le 10000≤n≤1000，链表中任意节点的值满足 0 \le val \le 1000≤val≤100
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
备注：
题目保证 nn 一定是有效的
快慢指针
具体做法：

step 1：给链表添加一个表头，处理删掉第一个元素时比较方便。
step 2：准备一个快指针，在链表上先走nnn步。
step 3：准备慢指针指向原始链表头，代表当前元素，前序节点指向添加的表头，这样两个指针之间相距就是一直都是nnn。
step 4：快慢指针同步移动，当快指针到达链表尾部的时候，慢指针正好到了倒数nnn个元素的位置。
step 5：最后将该节点前序节点的指针指向该节点后一个节点，删掉这个节点。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # write code here
        # 倒数第几个，快指针比满指针多几步
        # if head is None:
        #     return head

        # low = head
        # fast = head

        # # print(fast.next.val)
        # 我这里就不应该用 fast.next就应该用fast，然后下面再用fast = fast.next
        # while fast.next is not None:
        #     low = low.next
        #     for i in range(n):
        #         fast = fast.next

        # print(fast.val)
        # # 就是删除slow后面那个？
        # low.next = low.next.next
        # return head

        res = ListNode(-1)
        res.next = head

        cur = head
        pre = res
        fast = head
        while n:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            pre = cur
            cur = cur.next
        pre.next = cur.next

        return res.next
