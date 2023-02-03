import math

inp = int(input())

lis = [int(i) for i in input().split()]
newlis = list(reversed(lis))

# for num in newlis:
#     for j in range(len(str(num))):
#         str(num)[j] = str(num)[j] * int(math.pow(16, j))


# for i in range(-1, 2):
#     print(i)
print(inp, lis, newlis)

