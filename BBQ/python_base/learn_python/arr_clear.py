'''
如何把数组一下子清空
'''

arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr.pop(-1)

print(arr, arr.clear())