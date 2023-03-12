'''

'''
import sys

# 这种只要一个换行就能得到新的一行的数据，woc，爱了，之前一直执着于input，把这个忘了
for line in sys.stdin:
    a = line.split()
    print(a)
