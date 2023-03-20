#include<bits/stdc++.h>
using namespace std;
#define MAXN 6005
int h[MAXN];
int v[MAXN];
vector<int> son[MAXN];
int f[MAXN][2];
void dp(int x)
{
//  先把值定义出来，下面才可以进行dp，初始化
    f[x][0]=0;  //x要是不去，那开心值就是0
    f[x][1]=h[x];  //x去了，开心值是x员工增加的happy值
//找到根里面的每一个子节点的所有孩子，到最底下的那个孩子的快乐值就是
    for(int i=0; i<son[x].size(); i++)
    {
        int y=son[x][i];
        dp(y);  //递归，如果孩子还有孩子那就更新最底下的根节点的开心值，到最底层时候，员工的开心值就是员工的开心值
        f[x][0]+=max(f[y][0],f[y][1]);  //领导不去的开心值就是员工去或者不去的值的最大值，员工就是孩子
        f[x][1]+=f[y][0];  //领导去了的开心值就是孩子不去的加上领导的
    }
}
int main()
{
    int n;
    cin>>n;
//  开心值
    for(int i=1; i<=n; i++)
        cin>>h[i];
    for(int i=1; i<=n-1; i++)
    {
        int x,y;
        cin>>x>>y;
        son[y].push_back(x);  //领导为节点，下属为孩子放进领导为下标的数组中
        v[x]=1;
    }
    // 把输入画作一颗树，可以发现唯一没有被v[i]标记的就是根节点
    int root;
//cout << root << endl;
    for(int i=1; i<=n; i++)
        if(!v[i])
        {
            root=i;
            break;
        }
    // for 孉一直再进行，root肯定会有值的，就是根节点，不是任何人的孩子，就是所有人的祖宗
    dp(root);
    cout<<max(f[root][0],f[root][1])<<endl;
    return 0;
}
/*
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
*/
