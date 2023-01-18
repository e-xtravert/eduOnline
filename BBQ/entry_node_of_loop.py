'''
描述
给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。

数据范围： n\le10000n≤10000，1<=结点值<=100001<=结点值<=10000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 哈希第一个重复的数字就是入口方向
        hash = dict()
        head = pHead

        while head != None:
            if head not in hash:
                hash[head] = 1

            if hash[head] > 1:
                return head

            else:
                hash[head] += 1

            head = head.next
