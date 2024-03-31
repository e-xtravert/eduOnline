# @Time    : 2024/3/31 8:41

# 获取输入的字符串
s = input()
# 从1循环到9
for i in range(1, 10):
    # 如果i不在s中
    if str(i) not in s:
        # 输出i
        print(i)
        # 退出循环
        break

# a的ascii