'''
问题描述
　　请找到一个大于 2022 的最小数，这个数转换成十六进制之后，所有的数位（不含前导 0）都为字母（A 到 F）。
　　请将这个数的十进制形式作为答案提交。
答案提交
　　这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
'''


n = int(input())
a = int('AAA', 16)

print(hex(n), a)