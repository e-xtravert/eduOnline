# @Time    : 2023/3/16 10:38
'''
问题描述
　　住在有顶天的天人Tensi对自己的住处很不满。终于有一天她决定把门前碍眼的要石通通丢掉（怒扔要石）。控制要石自然是很容易的事，不过也会消耗灵力。
假设搬走一块质量为1的要石会消耗1点灵力，而且由于要石都是连着放置的缘故所以每次除了搬走一颗，也可以搬走连续的任意数量的要石，自然质量是算在一起的。
现在Tensi准备最多使用M次灵力，但是她太懒……所以每次只会使用同量的灵力， 也因为她太烂，所以也不愿意多花一点灵力……现在很懒的Tensi需要你帮她计算最少一次需要消耗多少灵力，能够在M次内把所有要石都丢到人间去……
输入格式
　　第一行两个数N,M，用一个空格分隔。1<=n<=1000,1<=m<=400
　　表示一共有N颗要石需要搬走已经Tensi最多发动M次灵力。
　　接下来包括N 个正整数 0<=ai<=40000 顺序表示每一颗要石的质量。
输出格式
　　输出一个数T
　　表示Tensi 每次至少消耗T灵力。0<=T<=1000000
　　如果无解输出-1.
样例输入
5 3
1 2 1 1 1
样例输出
3
'''
# 没看懂题目 笑死
n, m = map(int, input().split())
stones = [int(i) for i in input().split()]

def check(d):
    count = 0
    sum_ = 0

print(stones)