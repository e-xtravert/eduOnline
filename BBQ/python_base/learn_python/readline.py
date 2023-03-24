# @Time    : 2023/3/24 9:39
import sys

option = [1, 2, 3, 4, 5]
option.reverse()
option_ = option.copy()
option.reverse()
# while 1:
#     line = sys.stdin.readline()
#     if line:
#         line = list(map(int, line.strip()))
#     else:
#         break
#
#     option.append(line)

# 如何获取未知行数 然后输入 以换行结束的方法似乎是无法实现的mmp
# while 1:
#     i = 0
#     option.append(int(input()))
#     if len(option) > i:
#         option.append(int(input()))
#     else:
#         break


# print(option[2:len(option)])  # 左闭右开
# option1 = option_r[len(option) - 2:len(option)]
# option1.reverse()  # 这其实是一个过程 没有返回值 所以不能直接再下面加操作
# op = option[2:len(option)] + option1
# print(op[:3])

print(option[-2:])
print(option[:-2])
option_1 = option_[:-2]
print(option_1)



