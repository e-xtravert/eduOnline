'''

'''
n, m = map(int, input().split())
if (m - (7 - n)) % 7 == 0:
    res = 7
else:
    res = (m - (7 - n)) % 7


print(res)