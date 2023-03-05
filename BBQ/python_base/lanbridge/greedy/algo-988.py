'''
蓝桥杯训练题
n一定是偶数咯，妹子每次也是最优的取数，要求的是先手的最优，即最大的数
8
5 2 4 3 1 7 8 6
应该是输出20吧，测试用例自己编的
'''
# 下面是自己最开始写得，考虑不恰当，并不应该只看最前和最后的数字大小，还有看取走数之后的大小，就是说第一次看似取了一个较小的，但是后面加起来却是更大的。
num = int(input())
lis = [int(i) for i in input().split()]
res = 0
path = []
mei = []
for i in range(num):
    if len(lis) == 0:
        break
    if i % 2 == 0:
        # 先手那就是奇数次序咯，但是下标是从0开始呀，那还是偶数,下面写得有些复杂不想改了
        if lis[0] > lis[len(lis) - 1]:
            res += lis[0]
            path.append(lis.pop(0))
        else:
            res += lis[len(lis) - 1]
            path.append(lis.pop(-1))
    else:
        if lis[0] > lis[len(lis) - 1]:
            mei.append(lis.pop(0))
        else:
            mei.append(lis.pop(-1))

print(res, path, mei)
