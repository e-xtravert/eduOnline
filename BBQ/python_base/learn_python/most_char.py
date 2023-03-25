# @Time    : 2023/3/25 21:46
'''

'''

s = str(input())
has = dict()

for i in range(len(s)):
    if s[i] not in has:
        has[s[i]] = 1
    else:
        has[s[i]] += 1

char = ''
# 这里需要获取has的values里面的最大值 之前看过但是没注意 一直用的数组麻烦办法

# 先按字典序将has从大到小排序 然后再输出字典序最大的 即使有相同的最大值 那也会输出第一个出现的 即字典序最小的满足
has_ = dict(sorted(has.items(), key=lambda x: x[0], reverse=False))  # True是降序
ret = max(has, key=lambda x: has[x])

print(has, has_, ret)
print(has[ret])
