'''
卡片，这里面有个知识点就是count计数函数，最先达到的肯定是1啊
我的建议是做题目之前直接去看解题有什么新的函数，然后再自己写，不然很麻烦
'''

import os
import sys

# 请在此输入您的代码
num = 0
for i in range(1, 10000):
    num += str(i).count('1')

    if num == 2021:
        break

print(i)


