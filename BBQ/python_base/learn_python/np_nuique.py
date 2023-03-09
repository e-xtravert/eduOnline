import numpy as np

arr = [1, 2, 3, 4, 5, 4, 5]
# 作为np对象不能使用直接使用append
# 要使用np.append(arr, element)赋值给这个对象
unique, count = np.unique(arr, return_counts=True)

print(unique, count)
