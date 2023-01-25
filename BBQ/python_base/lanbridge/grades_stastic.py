import os
import sys

# 请在此输入您的代码 ,很简单，秒了
n = int(input())
f = 0
a = 0

for i in range(n):
  info = int(input())
  if info >= 60:
    f += 1
  if info >= 85:
    a += 1

print(str(int(f/n  * 100 + 0.5)) + '%')
print(str(int(a/n * 100 + 0.5)) + '%')
# print(n)