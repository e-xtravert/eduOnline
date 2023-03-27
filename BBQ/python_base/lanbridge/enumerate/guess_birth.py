# @Time    : 2023/3/27 16:04
'''
才生日
'''


# 注意这个日期格式问题就行
def zero(num):
    if num < 10:
        return '0' + str(num)


for i in range(1900, 2000):
    for j in range(31):
        if j < 10:
            j = zero(j)
            birth = int(str(i) + '06' + j)
        else:
            birth = int(str(i) + '06' + str(j))
        if birth % 2012 == 0 and birth % 3 == 0 and birth % 12 == 0:
            print(birth)