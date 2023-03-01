'''
蓝桥杯训练题 拿糖果
kAc有n堆糖果，每堆有A[i]个。
　　kAc说你只能拿m次糖果，聪明的你当然想要拿最多的糖果来吃啦啦啦~
　　//第二天，kAc问你还想吃糖果么？（嘿嘿嘿）说着眼角路出奇怪的微笑...
输入格式
　　第一行两个数字n和m，第二行有n个数字A[i]。
输出格式
　　输出一行表示最多能拿几个糖果。
样例输入
2 2
1 2
样例输出
3
'''
n, m = map(int, input().split())
candy = [int(i) for i in input().split()]
candy.sort()
candy.reverse()
res = 0

for i in range(m):
    res += candy[i]

print(res)