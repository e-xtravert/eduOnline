# @Time    : 2023/3/28 15:59
'''
向数组中插入数组，将数组转化成list形式
'''

arr = []

for i in range(10, 15):
    a = [i, i]
    arr.extend(a)  # extend直接把我要插入值的数组解构了
    arr.insert(0, a)  # insert 是可以的 就是数组元素的位置变化了 当然也可以插入参数是数组长度 - 1 的位置， 即末尾
    del a

print(arr)
print(len(arr))
