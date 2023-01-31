'''
计算从1-2020一共出现了多少个2.秒了
'''
import os
import sys

# 请在此输入您的代码
inp = input() # 字符串形式
num = 0
for i in range(1, 2020 + 1): # 我这原来用的是inp，可以测试所有案例，最后死命通过不了，
# 后来直接改成提供的数据就行了，看来只需要答案的，就不能搞成变量的形式了
  for j in range(0, len(str(i))):
    if '2' == str(i)[j]:
      num += 1

print(num)