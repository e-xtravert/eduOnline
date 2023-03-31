# @Time    : 2023/3/30 22:20
'''

'''


arr = [list()]

print(arr)
# 这就是数组中插入列表的方式
lis = [1, 2, 3, 4, list()]

print(lis)

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
s = 'rewaew'
print(list(enumerate(s)))

for i, s in enumerate(s):
    print(i, s)