# # '''
# # 这里一般用来写一些demo，简单来说就是用来打草稿的
# # '''
# # #
# # # arr = [1, 2, 3]
# # #
# # # dp_about_lqb = [[0] * (len(arr) + 1) for i in range(len(arr) + 1)]
# # # print(dp_about_lqb)
# #
# #
# # # print(arr, '\n',dp_about_lqb)
# #
# # # print(sum(x[2**2 - 1: 2**2+2**2-1]))
# #
# # import os
# # import sys
# #
# # # 请在此输入您的代码,数字2021个，能拼多少个数
# # # inp = input()
# # # num = 0
# # # for i in range(1, 2):
# # #     for j in range(0, len(str(i))):
# # #         if '1' == str(i)[j]:
# # #             num += 1
# # #
# # #         if num == 1:
# # #             print(10)
# # #
# # #         print(num)
# # #             # if num == 10:
# # #             #     print(i)
# #
# # '''
# # numpy测试纵向合并数组,合并成二维数组
# # '''
# # import numpy as np
# #
# # a = [-4, -5, -10, -3, 1]
# # b = [7, 5, -9, 3, -10]
# # # c = np.vstack((a, b))
# # d = [10, -2, 6, -10, -4]
# # fin = np.vstack((a, b, d))
# # print(fin)
# #
# #
# # n, m = map(int, input().split())
# # dp_about_lqb = [[*map(int, input().split())] for _ in range(n)]
# # direct = [(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1),(3,0)]
# # for x in range(n):
# #   for y in range(m):
# #     res = []
# #     for dx,dy in direct:
# #       lx = x - dx
# #       ly = y - dy
# #       if(lx>=0 and ly>=0 and lx<n and ly<m):
# #         res.append(dp_about_lqb[lx][ly])
# #     dp_about_lqb[x][y] += max(res) if len(res)!=0 else 0
# # print(dp_about_lqb[-1][-1])
# #
#
# import os
# import sys
# # import numpy as np
#
# # 请在此输入您的代码,他这里的机制是一行输入，使用一个input（）
# # 用dp[i]表示当前最大的权值
# n, m = map(int, input().split())
#
# # a = [int(i) for i in input().split()]
# # b = [int(i) for i in input().split()]
# # c = [int(i) for i in input().split()]
# # # 数组纵向合并？一闪而过的,可惜没有这个库， 但是你上面一行一行打印这种方式也太蠢了，
# # 多在评论区看看人家的写法吧
# # # s =  np.vstack((a, b, c))
# # 这里的*是收集列表中多余的值，也是为了将map转成列表形式
# map1 = [ [*map(int, input().split())] for _ in range(n)]
# # 还是用一个另外相似结构的数据结构来保存状态
# dp = [[-100]*(m+3) for i in range(n+3)]
# # for i, j in [(0, 1), (0, 2), (0, 3)]:
# #   print(i, j) # 会输出0 1； 0 2这样的形式，应该是结构了
# for i in  range(n):
#   for j in range(m):
#     # if i - 3 < 0 or j - 3 < 0:
#     dp[0][0] = map1[0][0]
#     #   dp_about_lqb[i][j] = 0
#     dp[i][j] = map1[i][j] + max(dp[i - 1][j], dp[i - 2][j],
#     dp[i - 3][j], dp[i - 2][j - 1], dp[i][j - 1], dp[i - 1][j - 2], dp[i][j - 3],
#     dp[i][j - 2], dp[i - 1][j - 1])
#
# # dp_about_lqb[i][j] = dp_about_lqb[i][j] + max(dp_about_lqb[i- 1][j], dp_about_lqb[i][j - 1])
# print(n, m, map1[2][4], dp[n - 1][m - 1])
res = 0
for i in range(-1, -2):
  res = i
  print(i)

print(res)