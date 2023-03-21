# @Time    : 2023/3/21 19:31
'''
小蓝给学生们组织了一场考试，卷面总分为 100 分，每个学生的得分都是一个 0 到 100 的整数。
请计算这次考试的最高分、最低分和平均分。
输入描述
输入的第一行包含一个整数
接下来 n 行，每行包含一个 0 至 100 的整数，表示一个学生的得分。
输出描述
输出三行。
第一行包含一个整数，表示最高分。
第二行包含一个整数，表示最低分。
第三行包含一个实数，四舍五入保留正好两位小数，表示平均分。
输入：7
80
92
56
74
88
99
10
输出：
99
10
71.29
'''
n = int(input())
grades = []
# 小东西 居然还给我搞输入的是数组了
for i in range(n):
    item = int(''.join(input().split()))
    grades.append(item)

max_score = max(grades)
min_score = min(grades)

average_score = sum(grades) / n

print(max_score, min_score, '%.2f' % average_score)
