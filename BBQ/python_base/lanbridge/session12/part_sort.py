'''
排序，0表示降序，1表示从当前位置升序
3 3
0 3
1 2
0 2
输出
3 1 2
'''
# 没做完，先不做了，明天考英语，有点心不在焉，这题没什么难度，纯逻辑和计算
leng, times = map(int, input().split())
act = [list(map(int, input().split())) for _ in range(times)]


# 判断是升序还是降序，用截取数组的方法，最后再把缺少的数组元素拼接上，就完咯
def sort(arr, x, y):
    if x == 0:
        sorted(arr[0:y], reverse=False)
        for i in range(y + 1, leng):
            arr.append(y + 1 + i)
    if x == 1:
        sorted(arr[y:], reverse=True)
        for i in range(1, y + 1):
            arr1 = [i]
            arr = arr1 + arr


arr0 = []
for i in range(1, leng + 1):
    arr0.append(i)

for i in range(len(act)):
    sort(arr0, act[i][0], act[i][1])

print(leng, times, act, arr0)