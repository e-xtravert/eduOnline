# @Time    : 2023/3/25 11:41
'''
格子刷油漆
宽长为 2 x N 个格子 只能相邻或对焦刷油漆 求总方案数
当已知 N 时，求总的方案数。当 N 较大时，结果会迅速增大，请把结果对
10 ** 9 + 7 取模。
输入输出
2
24
'''

# 题目给的标签是动态规划 就是从灭一个格子开始刷的总数吗？我感觉用bfs合适吧，把所有满足条件的结果加起来
n = int(input())

# bfs不好做 ，看来对bfs，dfs适用还是不熟，需要了解 todo
# 这题难点在于如何找到dp的表达式 看了网上半天解释还是一知半解 寄了
# 一个 https://blog.csdn.net/m0_55982600/article/details/123145946
'''
把代码复制过来了 看不懂dp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#define int long long
#define mod 1000000007
using namespace std;
 
int n, dp[1005][2]; 
//dp[i][0]表示长度为i的格子，从左上角出发遍历全部格子然后返回起点上或下面点的方案数
//dp[i][1]表示长度为i的格子，从左上角出发遍历全部格子然后到任意终点的方案数 
 
signed main()
{
	cin >> n;
	dp[1][0] = 1, dp[2][0] = 2;
	dp[1][1] = 1, dp[2][1] = 6;
	for(int i = 3; i <= n; i++)
	{
		dp[i][0] = dp[i-1][0]*2%mod;
		dp[i][1] = (4*dp[i-2][1]%mod+2*dp[i-1][1]%mod+2*dp[i-1][0]%mod)%mod;
	}
	int ans = 4*dp[n][1]%mod;//四个角落为起点的方案数 
	for(int i = 2; i <= n-1; i++)
		ans = (ans+4*dp[i][0]*dp[n-i][1]%mod+4*dp[n-i+1][0]*dp[i-1][1]%mod)%mod;
	cout << ans;
    return 0;
}
'''

