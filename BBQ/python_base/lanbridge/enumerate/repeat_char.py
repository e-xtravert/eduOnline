# @Time    : 2023/3/28 11:06
'''
重复子串 需要修改几个字符
2
aabbaa
2
'''
# 答案来自网络 也没有完全通过 50%
# 输入
k = int(input())
string = input()

# 判断特殊情况
if not string or len(string) % k != 0:
    print(-1)

dp = [0] * (k + 1)  # 创建dp数组
i = 0  # dp下标
l = len(string) // k  # 重复l次
for i in range(k):
    lst = [0] * 26  # 用一个列表计数
    for j in range(l):
        # 这种思路真的巧妙 可以把二维数组压缩成一维 对于需要使用 map 的数据也是能够处理
        lst[ord(string[i + j * k]) - ord('a')] += 1  # ord 是求ASCII编码意思 把字符串中每一个字符都和字符a对比 差值， 都和a对比当作基准
    dp[i + 1] = dp[i] + (l - max(lst))  # l是每一个子串的长度 ，max（lst）表示在子串对应字符对比的过程中 差值最多出现的 一般表示相同数目最多的 l - 这个值即最少需要修改的
print(dp[-1])
