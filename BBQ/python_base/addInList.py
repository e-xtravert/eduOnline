'''
描述
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
数据范围：0 \le n,m \le 10000000≤n,m≤1000000，链表任意值 0 \le val \le 90≤val≤9
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。
输入：
[9,3,7],[6,3]
返回值：
{1,0,0,0}
说明：
如题面解释
'''


class Solution:
    # 反转链表
    def ReverseList(self, pHead: ListNode):
        if pHead == None:
            return None
        cur = pHead
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        # 两个链表反转
        head1 = self.ReverseList(head1)
        head2 = self.ReverseList(head2)

        # 添加表头
        res = ListNode(-1)
        head = res
        # 进位符号
        carry = 0

        while head1 != None or head2 != None or carry != 0:
            val1 = 0 if head1 == None else head1.val
            val2 = 0 if head2 == None else head2.val

            temp = val1 + val2 + carry
            carry = (int)(temp / 10)
            temp %= 10
            head.next = ListNode(temp)
            head = head.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        return self.ReverseList(res.next)
