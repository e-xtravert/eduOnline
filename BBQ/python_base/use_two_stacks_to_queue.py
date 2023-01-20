'''
描述
用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。 队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素。

数据范围： n\le1000n≤1000
要求：存储n个元素的空间复杂度为 O(n)O(n) ，插入与删除的时间复杂度都是 O(1)O(1)

思路：

元素进栈以后，只能优先弹出末尾元素，但是队列每次弹出的却是最先进去的元素，如果能够将栈中元素全部取出来，才能访问到最前面的元素，此时，可以用另一个栈来辅助取出。

具体做法：

step 1：push操作就正常push到第一个栈末尾。
step 2：pop操作时，优先将第一个栈的元素弹出，并依次进入第二个栈中。
1
2
3
//将第一个栈中内容弹出放入第二个栈中
while(!stack1.isEmpty())
    stack2.push(stack1.pop());
step 3：第一个栈中最后取出的元素也就是最后进入第二个栈的元素就是队列首部元素，要弹出，此时在第二个栈中可以直接弹出。
step 4：再将第二个中保存的内容，依次弹出，依次进入第一个栈中，这样第一个栈中虽然取出了最里面的元素，但是顺序并没有变。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()

        # 取完要把人家的元素还给人家
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res
