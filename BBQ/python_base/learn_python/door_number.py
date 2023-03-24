# @Time    : 2023/3/24 22:31
'''

'''

res = 0
for i in range(1, 2021):
    num = str(i)
    for i in range(len(num)):
        if int(num[i]) == 2:
            res += 1

print(res)
