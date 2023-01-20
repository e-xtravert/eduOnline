"""
翻转链表
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        if head is None:
            return head
        else:
            p0 = None
            p1 = head
            while p1 is not None:
                tem = p1.next
                p1.next = p0
                p0 = p1
                p1 = tem
            return p0