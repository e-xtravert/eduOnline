# @Time    : 2023/3/19 10:40
'''
选课洛谷p2014 https://www.luogu.com.cn/problem/P2014
#include<cstdio>
const int MAXN = 300 + 5;
const int MAXM = 300 + 5;

inline void chk_max(int &a,int b)
{
    if(a<b)
        a=b;
}

//前向星存图
struct Edge
{
    int next,to;
} e[MAXN];
int head[MAXN],ecnt=0;
inline void add(int u,int v)
{
    ++ecnt;
    e[ecnt].next=head[u];
    e[ecnt].to=v;
    head[u]=ecnt;
}

int m;
int dp[MAXN][MAXM];

void solve(int u)
{
    for(int i=head[u]; i; i=e[i].next)
        solve(e[i].to);//先处理子节点

    //背包部分
    for(int i=head[u]; i; i=e[i].next)
        for(int j=m, v=e[i].to; j>0; --j)
            for(int k=0; k<j; ++k)
                chk_max(dp[u][j], dp[u][j-k]+dp[v][k]);
}

int main(void)
{

    int n;
    scanf("%d%d",&n,&m);
    ++m;//上文提到了
    for(int i=1; i<=n; ++i)
    {
        int fa;
        scanf("%d%d",&fa,&dp[i][1]);//思考：为什么直接用dp[i][1]？
        add(fa,i);
    }

    solve(0);
    printf("%d",dp[0][m]);
    return 0;
}
/*
7  4
2  2
0  1
0  4
2  1
7  1
7  6
2  2
*/

'''
# 没看懂
