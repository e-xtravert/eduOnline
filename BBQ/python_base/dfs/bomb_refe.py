'''
这是有关炸弹那个题目的网上的做法，我虽然是参考的，但是个人认为我的做法更好理解，在bomb文件里面，下面是网上的answer
他的做法也看了，就是有几个点不一样，在dfs里面，他是把当前的炸弹置0，然后再无差别搜索新的1
但是我是在当前是1的情况下，向后面或下面搜索1，不再重复搜索，最后在判断是否是炸弹那里加条件，如果已经搜索过了，说明那个炸弹已经爆炸了，就不需要包含了
#include<cstdio>
int n,m,cnt;
char mp[1005][1005];
bool vx[1005],vy[1005];
//xv[i]表示第i行是否被访问，vy[i]表示第i列是否被访问
void dfs(int x,int y){
	mp[x][y]='0';
	if(!vx[x]){
		vx[x]=1;
		for(int i=0;i<m;++i){
			if(mp[x][i]=='1'){
				dfs(x,i);
			}
		}
	}
	if(!vy[y]){
		vy[y]=1;
		for(int i=0;i<n;++i){
			if(mp[i][y]=='1'){
				dfs(i,y);
			}
		}
	}
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;++i)
		scanf("%s",mp[i]);
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			if(mp[i][j]=='1'){
				++cnt;
				dfs(i,j);
			}
		}
	}
	printf("%d\n",cnt);
	return 0;
}
'''

