'''
对于一个日期，我们可以计算出年份的各个数位上的数字之和，也可以分别计算月和日的各位数字之和。请问从 1900 年 1 月 1 日至 9999 年 12 月 31 日，总共有多少天，年份的数位数字之和等于月的数位数字之和加日的数位数字之和。
　　例如，2022年11月13日满足要求，因为 2+0+2+2=(1+1)+(1+3) 。
　　请提交满足条件的日期的总数量。
答案提交
　　这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
'''


def year_sum(year):
    num = 0
    year = str(year)
    for i in range(len(year)):
        num += int(year[i])

    return num


# 还需要考虑闰年闰月之类的
print(year_sum(1900))
res = 0
for i in range(1900, 10000):
    sum_year = year_sum(i)
    for j in range(1, 13):
        for k in range(1, 32):
            if sum_year == j + k:
                res += 1

print(res)