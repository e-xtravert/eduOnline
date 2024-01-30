# @Time    : 2024/1/30 23:56


t1, t2 = map(str, input().split())
print(t1, t2)

def time(s):
    return int(s[0:2]) * 60 * 60 * 100 + int(s[3:5]) * 60 * 100 + int(s[6:8]) * 100 + int(s[9:11])

print(abs(time(t1) - time(t2)))