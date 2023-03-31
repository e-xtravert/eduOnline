# @Time    : 2023/3/25 22:06
'''
dict求values最值 返回key
'''

num = [10, 11, 12]
print(max(num, key=lambda i: i * i))  # 12 后面表示遍历 num中的元素 返回 元素平方值最大的元素


dic = {'k1': 10, 'k2': 200, 'k3': 20}

# ax 的第一个参数是迭代对象，而 dict 默认迭代Key， 匿名函数冒号后面是返回值，按照返回值的内容进行比较，而最后的max返回的对象是key值。而这也就是 max函数 key 的自定义功能。
ret = max(dic, key=lambda x: dic[x])  # k2 lambda 后面跟的是函数 即用dict的key值当作x参数传入dict[x]函数中然后遍历， 返回值最大的key
print(ret)


ret = max(dic, key=lambda x: x)  # k3 这里没有经过处理 就是遍历dic中的key值 返回最大的是k3
print(ret)  # k3

lst = [
    {'name': 'egon', 'price': 100},
    {'name': 'rdw', 'price': 666},
    {'name': 'zat', 'price': 1}
]
ret = max(lst, key=lambda dic: dic['price'])  # 指定比较内容
print(ret)  # {'price': 666, 'name': 'rdw'}
'''
上述分析过程 不细究了
（1）先取{'name': 'egon', 'price': 100}，以{'name': 'egon', 'price': 100}为参传入匿名函数作为dic，
 
经dic['price']处理得100，
 
（2）再取{'name': 'rdw', 'price': 666}，以{'name': 'rdw', 'price': 666}为参传入匿名函数作为dic，
 
经dic['price']处理得666，
 
（3）最后取{'name': 'zat', 'price': 1}，以{'name': 'zat', 'price': 1}为参传入匿名函数作为dic，
 
经dic['price']处理得1
 
（4）集中比较100,666,1得666最大，返回666对应的参数dic，即{'name': 'rdw', 'price': 666}。
 
（5）因为返回是字典，所以可能乱序，即上面结果{'price': 666, 'name': 'rdw'}
'''

# 还有一些排序的用法放在typora了

# set() 函数创建一个无序不重复元素集
s = set()
s.add('fdasf')
print(s)
