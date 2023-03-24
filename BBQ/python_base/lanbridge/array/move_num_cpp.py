# @Time    : 2023/3/24 10:41
'''
//移动
//给定一个n长的数列，有m次操作，第i次操作表示将整个数列循环移动mi位，询问每次操作结束后的开头k个数字
//输入格式
//第一行三个整数n,m,k。
//第二行n个整数表示数列。
//接下来m行，每行一个整数mi，表示移动位数，若mi为正，表示向左移mi位，若mi为负数，表示向右移-mi位。

#include<iostream>
//#include<bits/stdc++.h>

using namespace std;

int main()
{
    long n;
    int m, k;
    cin >> n >> m >> k;
    int lst[n];
    int out[m][k];//记录输出结果
    for (int i = 0; i < n;i++)
    {
        cin >> lst[i];
    }
    long flag = 0;//数列循环移动后的第一个下标，最初为0
    int count = 0;//记录out的行
    for (int i = 0;i<m;i++)
    {
        long mi;
        cin >> mi;
        mi %= n;//mi的数可能比较大，通过这个操作去掉无用的循环
        flag += mi;
        if(flag>n)
            flag %= n;
        if(flag<0)//flag<0，应该从后往前移动
            flag = n + flag;
        for (int j = 0; j < k;j++)//输出的数存入到out数组中
        {
            out[count][j] = lst[(flag + j) % n];
        }
        count++;
    }
    for (int i = 0;i<m;i++)
    {
        for (int j = 0; j < k;j++)
        {
            cout << out[i][j] << " ";
        }
        cout << endl;
    }
    system("pause");
    return 0;
}
'''