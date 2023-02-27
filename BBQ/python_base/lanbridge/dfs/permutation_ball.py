'''
排列小球
https://www.lanqiao.cn/problems/546/learning/
输入：3 6 0
输出：3
用 r 表示红球，g 表示绿球，可能的方案包括：
rrrgggggg
grrrggggg
ggrrrgggg
1.初步看题可知为枚举各种颜色小球的数量，来实现递增序列，故确定思路为dfs.
2.我们应该如何枚举小球呢？可以利用递增条件，记录上一次枚举的数量，下一次枚举需要大于这个数量。
dfs(sum,x,last)表示在sum个球中，前面选了颜色为last色的，x个球。
接着再选j个颜色为i的，那么剩下的球的选法和整体的选法相同，为dfs(sum-j,i,j) 3.递归边界为三数字的累加。
剪枝一为：last表示，这个选的小球和上次选的小球相同，则跳过。剪枝二为每次枚举递增数量的小球
'''

# 就是选小球出来，选出来的三种颜色的球要按照递增的排的方案有几种
# 涉及到几个因素，小球的总数量，选小球的颜色，选了某种颜色小球的数量

# 使用数组下标来表示小球颜色,下标分别表示颜色类别，例如color[0]为第一种颜色小球数量
color = [int(i) for i in input().split()]
_sum = sum(color)
res = 0


def dfs(ball_sum, pre_quantity, last_color):
    global res
    global _sum
    if ball_sum == 0:
        res += 1
        return
    for cur_color in range(len(color)):
        if cur_color == last_color:
            continue
        # if color[cur_color] == 0:
        #     return
        for j in range(pre_quantity + 1, color[cur_color] + 1):  # 如果没有小球了，在这里控制，没有就上循环去换一个颜色选小球
            color[cur_color] -= 1
            dfs(ball_sum - j, j, cur_color)
            color[cur_color] += 1


dfs(_sum, 0, -1)
print(res)
