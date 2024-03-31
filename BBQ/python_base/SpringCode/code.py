# @Time    : 2024/3/31 10:00
s = input()
a = [0,0,0,0,0,0,0]
k=0

for i in range(7):
  if i == 0 :
    a[4] = s[i]
  elif i== 1:
    a[5] = s[i]
  elif i== 2:
    a[6] = s[i]
  elif i== 3:
    a[0] = s[i]
  elif i== 4:
    a[1] = s[i]
  elif i== 5:
    a[2] = s[i]
  elif i== 6:
    a[3] = s[i]

for i in range(7):
  if a[i] == "a":
    a[i] = 97
  elif a[i] == "b":
    a[i] = 98
  elif a[i] == "c":
    a[i] = 99
  elif a[i] == "d":
    a[i] = 100
  elif a[i] == "e":
    a[i] = 101
  elif a[i] == "f":
    a[i] = 102
  elif a[i] == "g":
    a[i] = 103
  elif a[i] == "h":
    a[i] = 104
  elif a[i] == "i":
    a[i] = 105
  elif a[i] == "j":
    a[i] = 106
  elif a[i] == "k":
    a[i] = 107
  elif a[i] == "l":
    a[i] = 108
  elif a[i] == "m":
    a[i] = 109
  elif s[i] == "n":
    a[i] = 110
  elif a[i] == "o":
    a[i] = 111
  elif a[i] == "p":
    a[i] = 112
  elif a[i] == "q":
    a[i] = 113
  elif a[i] == "r":
    a[i] = 114
  elif a[i] == "s":
    a[i] = 115
  elif a[i] == "t":
    a[i] = 116
  elif a[i] == "u":
    a[i] = 117
  elif a[i] == "v":
    a[i] = 118
  elif a[i] == "w":
    a[i] = 119
  elif a[i] == "x":
    a[i] = 120
  elif a[i] == "y":
    a[i] = 121
  elif a[i] == "z":
    a[i] = 122

# 将数组中整数元素转换为字符元素
for i in range(7):
  a[i] = str(a[i])
print(int(''.join(a)))