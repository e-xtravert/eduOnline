'''
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int n,sum;
int s=0,f=0;
int a[30],b[30];
void dfs(int x)
{
    int i,k;
    if(s>=sum)			//还是老样子，函数需要先写结束条件，判断是否结束
    {			//这道题里当s大于条件和时，就没必要再进行递归了，直接进行判断
        if(s==sum)			//当s等于条件和
        {
            if(f==0)	//f是判断时候有符合条件的输出，当没有符合的时，f始终为0
                f=1;
            if(f)
            {				//符合条件，输出
                printf("Yes\n");
                for(i=0; i<n; i++)		//所有数的下表
                {
                    if(b[i])				//利用数组b判断是否需要输出
                        printf("%d ",a[i]);
                }
                printf("\n");
            }
        }
    }
    for(k=x; k<n; k++)
    {
        s=s+a[k];		//当前元素，加和  s
        b[k]=1;			//当前元素的下标，在数组b中标记为1
        dfs(k+1);		//进入下个dfs
        s=s-a[k];		//回溯，减去加上的元素
        b[k]=0;			//回溯，把数组b中标记的1返回为0，以便于下次dfs使用
    }
}
int main()
{
    int i,j,k;
    memset(b,0,sizeof(b));		//把数组b全部设为0，便于标记
    scanf("%d %d",&n,&sum);
    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }
    dfs(0);							//从第一个数进入dfs
    if(f==0)				//此时递归结束，如果f仍为0，则说明没有符合条件的组合
        printf("No\n");
        return 0;
}

'''