'''
ALGO-1005
给定一个1～N的排列a[i]，每次将相邻两个数相加，得到新序列，再对新序列重复这样的操作，显然每次得到的序列都比上一次的序列长度少1，最终只剩一个数字。
　　例如:
　　3 1 2 4
　　4 3 6
　　7 9
　　16
　　现在如果知道N和最后得到的数字sum，请求出最初序列a[i]，为1～N的一个排列。若有多种答案，则输出字典序最小的那一个。数据保证有解。
没读懂题目啊，题目说是1 - N的排列，就是说是连续的四个数不同的排列这个意思，不然这猜数字也太难了
一定要多读几遍题目，比如1-4，那就是1,2,3,4进行排列
'''
n, sum = map(int, input().split())
vis = [0] * (n + 1)
res = 0
path = []
ans = []

if n == 1:  # 已经及格了，但是为了凑那个得分
    print(1)


def dfs(step):
    global res
    global ans
    if step == n:  # 第二次修改在这里，为了测试写成固定值4了
        res = path[:]
        # 下面是一种依次求一个n个数的数组中相邻两个数的和，具体做法是把相邻两个数的和放进相邻的数中的前一个数中保存，即res[i] = res[i] + res[i + 1],最后一个总和的算法
        for i in range(len(path) - 1):  # 这里还是要按照规则来加的
            for j in range(len(path) - i - 1):  # 这里为什么要-1，因为下面有一个res[j + 1],这样才不会越界，但是又能把元素都计算在内
                res[j] += res[j + 1]
                if res[0] == sum:
                    return True

    for i in range(1, n + 1):  # 这里控制的是第一层循环，最外层如何如何,外层确定第一个数如何选择，后面的加入数组和弹出数组确定后面的数如何选择
        # 说到底就是一种循环遍历，第一层遍历四个数，第二层也遍历四个数，取消重复的，然后依次判断是否符合，否则弹出，进入下一个层面的数选择
        if vis[i] == 1:
            continue
        vis[i] = 1
        path.append(i)
        if dfs(step + 1):
            return True
        path.pop(-1)
        vis[i] = 0

    return False


dfs(0)
# print("".join(path))  # 这种转换要求数组中元素是str, 第一次修改是在这里，我看他输出结果只有空格隔开的数字，我直接输出数组了
print(" ".join(str(i) for i in path), end="")
# print(n, sum)