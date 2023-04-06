# @Time    : 2023/4/5 22:52
'''
灭鼠先锋
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

// 用于记录当前状态是否被搜索过
unordered_map<string, bool> m;
bool check(string s) {
  return count(s.begin(), s.end(), '0') == 1;
}
bool dfs(string s) {
  if (m.count(s))
      return m[s];
  if (check(s))
      return m[s] = false;
  // 模拟下一步是一颗棋子
  for (int i = 0; i < 8; ++i) {
      if (s[i] == '0') {
          string tmp = s;
          tmp[i] = 'X';  // 将修改后的s传入下次dfs
          // 如果下一步是必败的，那么我们这步必胜
          if (!dfs(tmp))
              return m[s] = 1;  // 对于每一步的改变后的s做标记
      }
  }
  // 模拟下一步是二颗棋子
  for (int i = 0; i < 2; ++i) {
      for (int j = 0; j < 3; ++j) {
          int k = i * 4 + j;
          if (s[k] == '0' && s[k + 1] == '0') {
              string tmp = s;
              tmp[k] = tmp[k + 1] = 'X';
              if (!dfs(tmp))
                  return m[s] = 1;
          }
      }
  }
  // 运行到此，这说明不存在下一步是必败的情况，所有我们这一步输了
  return m[s] = false;
}
int main() {
  string s[4] = {"X0000000", "XX000000", "0X000000", "0XX00000"};
  for (auto i: s) {
      cout << (dfs(i)? 'L': 'V');
  }
  return 0;
}

'''
