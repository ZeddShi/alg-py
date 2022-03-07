# 两数之和 LC: 1

# 1. 暴力解
# 两层嵌套 for in 遍历

# 2. 更优解
# 用空间换时间，用hashmap存储遍历过的数据



def sum2(l, target):
    d = {}
    index1 = None
    index2 = None
    for i, v in enumerate(l):
        distance = target - v
        if d.get(distance):
            index1, index2 = d[distance][0], i
            break
        d.setdefault(distance, [])
        d[v].append(i)
    return index1, index2
