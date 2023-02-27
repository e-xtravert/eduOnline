'''
班里 NN 个小朋友，每个人都有自己最崇拜的一个小朋友（也可以是自己）。
在一个游戏中，需要小朋友坐一个圈，每个小朋友都有自己最崇拜的小朋友在他的右手边。
求满足条件的圈最大多少人？
输入：
9
3 4 2 5 3 8 4 6 9
输出：4
就是按自然数那么排列，前面的数字崇拜后面的数字，给出的数据所在的位置的数是他的崇拜数（从1开始，比如第一个数是3，那么1崇拜3，第二个数是4，那么2崇拜4
'''

n = int(input())
lis = [int(i) for i in input().split()]
lis.reverse()
lis.append(0)
lis.reverse()  # 在数组前面加个0 ，或者直接lis = [0] +
vis = [0 for _ in range(n + 1)]
global res
res = 0


def dfs(child_num, index):  # 传入的参数是lis中的数还有，长度，长度就依次加1就行
    if vis[child_num]:
        global res
        res = max(res, index - vis[child_num])  # 取出最长的res
        return

    vis[child_num] = index  # 这里为什么是这样赋值的，因为题目是根据自然数的排列前后顺序来确定lis中谁崇拜谁的下标是多少
    # 比如第一个数3,3崇拜的数是3的下一个数是4，4的下标是3的下标+1，就是2，所以把vis[4]值为下标值存放，后面直接将i - vis[child_num]
    dfs(lis[child_num], index + 1)


for i in range(1, n + 1):
    if not vis[i]:
        dfs(i, 1)

print(res)





