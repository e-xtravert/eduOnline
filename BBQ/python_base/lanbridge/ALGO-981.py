'''
ALGO-981过河马
由于过河马积累了许多的怨念，所以这次它过了河之后，再也没有什么东西可以限制它，它可以自由自在的在棋盘上驰骋。一开始，它是在一个n行m列棋盘的左下角（1,1）的位置，它想要走到终点右上角（n，m）的位置。而众所周知，马是要走日子格的。可是这匹马在积累了这么多怨念之后，它再也不想走回头路——也就是说，它只会朝向上的方向跳，不会朝向下的方向跳。
　　那么，这匹马它也想知道，它想从起点跳到终点，一共有多少种走法呢？
输入格式
　　第一行两个数n，m，表示一个n行m列的棋盘，马最初是在左下角（1,1）的位置，终点在右上角（n，m）的位置。
输出格式
　　输出有一行，一个数表示走法数。由于答案可能很大，所以输出答案除以1000000007所得的余数即可。
样例输入
4 4
样例输出
2
样例2
8 5
输出15
'''
# 题目做多了果然有用，看了一眼就知道该怎么写了，虽然没有全ac，但是方法是对的
# 第一次提交，成功是成功了，但是只有30分，还有两个测试用例超时了，栓q
# 第二次分析的时候发现之前只考虑了他会向右上角跳，而题目说向上跳，也可以向左上角跳，于是改进,又加了几个递归，但是直接宕机了，估计不对，看了一下网上的答案，用do的比较多
import sys

n, m = map(int, input().split())
res = 0


def check_x(x, y):
    if x + 2 <= m and y + 1 <= n:
        return True
    return False


def check_y(x, y):
    if x + 1 <= m and y + 2 <= n:
        return True
    return False


def check_x_1(x, y):
    if x - 1 >= 1 and y - 2 >= 2:
        return True
    return False


def check_x_2(x, y):
    if x - 2 >= 1 and y - 1 >= 1:
        return True
    return False


def check(x, y):
    global res
    if x > m or y > n:
        return
    if x == m and y == n:
        res += 1
    if check_x(x, y):
        check(x + 2, y + 1)
    if check_y(x, y):
        check(x + 1, y + 2)
    if check_x_1(x, y):
        check(x - 1, y - 2)
    if check_x_2(x, y):
        check(x - 2, y - 1)


check(1, 1)
print(res % 1000000007)
