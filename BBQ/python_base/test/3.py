# @Time    : 2023/4/8 9:32
'''
输入字符串，在 ？ 号位置填充 0 或者 1 使得 字符串中不重叠的 11 和 00 出现最多 输出总数
1110?0
'''
s = input()
cnt = 0
for i in s:
    if i == '?':
        cnt += 1

def chuli(s, i):
    ans0 = 0
    ans1 = 0
    s[i] = '0'
    for j in range(len(s), 2):
        if s[j] == s[j + 1]:
            ans0 += 1
        else:
            continue
    s[i] = '1'
    for j in range(len(s), 2):
        if s[j] == s[j + 1]:
            ans1 += 1
        else:
            continue
    return max(ans0, ans1)

# for j in s:
#     for k in range(2 ** cnt):
#         if j == "?":
#             l = len(str(k))
#             for m in range(l):
#                 j == bin(k)[2:][m]
#         else:
#             continue



print(s, bin(2 ** cnt)[2:], cnt)