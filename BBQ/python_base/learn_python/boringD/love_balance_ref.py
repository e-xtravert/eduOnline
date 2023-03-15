# @Time    : 2023/3/15 16:34
'''
问题描述
　　娜娜是一个特别可爱的女孩子，作为学神的她最近在情感方面出现了一点点小问题。
　　她暗恋的琦琦是一名学霸，他只喜欢长得漂亮和学习很好的女生。
　　娜娜学习确实很神，但是她在琦琦面前却总是表现不出平时的神力。
　　琦琦感受到了娜娜对他的爱，但是他还是觉得娜娜的学习并不是特别好，于是他出了一道题给娜娜。
　　“娜娜，我们之间的关系需要在不断深入的同时保持一定的平衡，不可以你总是强势或者我总是弱势。”
　　琦琦给了娜娜一些两两不等的数，希望娜娜能把这些数分成两组A和B，满足以下条件：
　　1：每一次只能操作一个数，即只取出一个数分入A中或B中；
　　2：每一次操作完成后，A中数之和与B中数之和的差不能超过r。
　　新时代的丘比特们啊，帮帮娜娜吧！
输入格式
　　输入共两行。
　　第一行包括两个正整数n和r，n表示琦琦一共给了n个数，r的意义见题目描述。
　　第二行包括n个正整数，分别表示琦琦给的n个数。
输出格式
　　输出共两行，分别把A与B两组数按从小到大输出。
　　注意输入中n个数的第一个必须分入A组。
　　琦琦保证这样的输出唯一。
样例输入
4 10
9 6 4 20
样例输出
4 6 9
20
'''
# 没测试，不想做了，谢谢
n, r = map(int, input().split())
nums = [int(i) for i in input().split()]
vis = [0 for _ in range(n)]


def check(d, l_, r_):
    if abs(d) > r:
        return 0
    if len(l_) + len(r_) == n:
        if nums[0] in l_:
            print(l_)
        else:
            print(r_)
        return 1
    for i in range(n):
        if not vis[i]:
            vis[i] = 1

            l_.appeng(nums[i])
            if check(d + nums[i], l_, r_) == 1:
                break

            l_.pop(-1)

            r_.append(nums[i])
            if check(d + nums[i], l_, r_) == 1:
                break
            r_.pop(-1)

            vis[i] = 0
    return 0


print(nums)
