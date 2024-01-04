# @Time    : 2024/1/3 22:24
import os
import sys

# 请在此输入您的代码
n, m = map(int, input().split())
# print(n, m)
g = []
fa = [i for i in range(n + 1)]
# print(fa)
for i in range(m):
  u, v, w = map(int, input().split())
  g.append([u, v, w])

# print(g)
g.sort(key = lambda x:(x[2]))  # 按w排序
# print(g)
def find(x):
  if fa[x] == x: return x
  fa[x] = find(fa[x])
  return fa[x]


def kruskal():
  res = 0
  cnt = 0
  for i in range(m):
    u, v, w = g[i]
    fu, fv = find(u), find(v)
    if fu != fv:
      res += w
      cnt += 1
      fa[fu] = fv
  if cnt < n - 1:
    return -1
  else:
    return res

print(kruskal())