'''
判断给定的链表中是否有环。如果有环则返回true，否则返回false。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 双指针，主要是快慢指针
        if not head:
            return False  # 标答这里是head

        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True
        return False




