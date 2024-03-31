# @Time    : 2024/3/31 10:30
s = input()
t = input()
q = int(input())

s1 = [0] * (len(s) + 1)
t1 = [0] * (len(t) + 1)

# 计算前缀和
for i in range(1, len(s) + 1):
    if s[i - 1] == 'X':
        s1[i] += 1
    if s[i - 1] == 'H':
        s1[i] += 2
    s1[i] += s1[i - 1]

# 计算前缀和
for i in range(1, len(t) + 1):
    if t[i - 1] == 'X':
        t1[i] += 1
    if t[i - 1] == 'H':
        t1[i] += 2
    t1[i] += t1[i - 1]

# 读取q次
for i in range(q):
    a, b, c, d = map(int, input().split())
    a1 = s1[b] - s1[a - 1]
    b1 = t1[d] - t1[c - 1]
    if a1 % 3 == b1 % 3:
        print("YES")
    else:
        print("NO")

# while q > 0:
#     ai, bi, ci, di = map(int, input().split())
#     a1 = s1[bi] - s1[ai - 1]
#     b1 = t1[di] - t1[ci - 1]
#     if a1 % 3 == b1 % 3:
#         print("YES")
#     else:
#         print("NO")
#     q -= 1

