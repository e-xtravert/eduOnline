# @Time    : 2023/3/24 22:51
'''
LANQIAO
3

'''

# print('AIAO' > 'AAIO')  # 这边有个问题 不知道啥情况 先标记一下
#  解决了 没问题 是因为理解错题目了 题目是从前往后删除 而不是选择删除 结束
#
# print('aia0' > 'aaio')  # 如果是小写就是挨个比较 但是大写好像不一样

s = str(input())
n = int(input())
# s.replace(s[0], '')  # 最开始这里不生效的原因是 这是一个过程 函数返回一个结果 需要接收
cnt = 0
while cnt < n:
    if s[0] > s[1]:
        s = s.replace(s[0], '')
    else:
        s = s.replace(s[1], '')

    cnt += 1

print(''.join(s))

