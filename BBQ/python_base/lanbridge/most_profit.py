# @Time    : 2023/3/21 13:37
'''
问题描述
　　Chakra是一位年轻有为的企业家，最近他在进军餐饮行业。他在各地开拓市场，共买下了N个饭店。
在初期的市场调研中，他将一天划分为M个时间段，并且知道第i个饭店在第j个时间段内，会有Aij位服务员当值和Bij位客户光临。
他还分析了不同饭店不同时间段客户的需求，得到第i个饭店在第j个时间段内，平均每位客户消费Cij元。
为了创设品牌形象，Chakra决定每个饭店每天只选择一个时间段营业，每个服务员至多接待一位顾客（若顾客数多于服务员数，超过部分的顾客当天就无法在该店消费了）。
　　企业家的目的终究还是获利。请你安排营业时间，并告诉Chakra每天消费总额最多为多少。
输入格式
　　第一行两个整数，N、M。
　　第二行开始依次给出三个矩阵A(N*M)、B(N*M)、C(N*M)。
输出格式
　　一行一个整数，最大消费总额。
样例输入 分别是服务员数量 顾客数量 顾客平均消费数量
2 3
1 2 3
3 2 1
3 2 1
1 2 3
4 5 2
3 1 6
样例输出
16
'''
# 最大获利那不是说服务员最少，顾客最多，消费最多， 两家店可以选择不同的时间段，比如第一家店最大是中午挣10万，第二家店是晚上挣6万
# 主要就是读题 我还以为要调整服务员的数量之类的
# 来自网络的答案
while True:
    try:
        N,M = map(int,input().split())
        A,B,C = [],[],[]
        ans = 0
        for i in range(N):
            A.append(list(map(int,input().split())))
        for i in range(N):
            B.append(list(map(int,input().split())))
        for i in range(N):
            C.append(list(map(int,input().split())))   #完成输入
        for x in range(N):   #大循环
            temp = []
            res = []
            for y in range(M):
                temp.append(min(A[x][y],B[x][y]))  # 选择服务员和顾客的最小值，因为一名服务员只能服务一个顾客
            for z in range(M):
                res.append(temp[z] * C[x][z])
            ans += max(res)
        print(ans)
    except:
        break


