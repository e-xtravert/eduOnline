'''
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以数字和为target的组合。
并且，candidates中的数字可以无限制重复选取。同时，题目中所给出的数字全部为正整数；解集中不能包含重复的集合。
如输入数组为candidates = [2, 3, 6, 7]、目标数为target = 7，则返回结果为[[2, 2, 3], [7]]。
'''

candidates = [int(i) for i in input().split(",")]
target = int(input())
candidates.sort()
path = []
res = []
# sorted(candidates)


def backtrack(nums, goal, start):
    if goal == target:
        res.append(path[:])
        return

    for i in range(start, len(nums)):  # 如果要依次往后进行，而不需要已经访问的数，那么可以传入参数控制，这里控制树的分支
        if (goal + nums[i]) <= target:  # 超过了，就不要了
            path.append(nums[i])
            backtrack(nums, goal + nums[i], i)  # 这里没有加，所以还是从最开始循环，这样符合candidates数可以无限取
            # 上面那个注释修改一下，不是从最前面开始，而是从自己开始，如果不要自己，则要加1
            # goal -= nums[i]  # 不需要减，为什么？  # 因为返回上一层之后的goal就是之前的goal 而不是增加之后的
            path.pop(-1)
        # else:
        #     i += 1


backtrack(candidates, 0, 0)
print(res)
# print(candidates, target)
