# 三数之和


def threeSum(nums):
    nums.sort()
    d = {}
    for i, v in enumerate(nums):
        d.setdefault(v, [])
        d[v].append(i)

    l = len(nums)
    result = []
    rem = {}
    for index_a in range(l):
        for index_b in range(index_a + 1, l):
            c = 0 - nums[index_a] - nums[index_b]
            if c in d and d[c][-1] > index_b:
                s = (nums[index_a], nums[index_b], c)
                rem_k = '%s-%s-%s' % s
                if rem_k in rem:
                    continue
                result.append(s)
                rem[rem_k] = 1
    return result


def threeSumOptimize(nums):
    n = len(nums)
    nums.sort()
    ans = list()
    
    # 枚举 a
    for first in range(n):
        # 需要和上一次枚举的数不相同
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        # c 对应的指针初始指向数组的最右端
        third = n - 1
        target = -nums[first]
        # 枚举 b
        for second in range(first + 1, n):
            # 需要和上一次枚举的数不相同
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            # 需要保证 b 的指针在 c 的指针的左侧
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            # 如果指针重合，随着 b 后续的增加
            # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])
    
    return ans


if __name__ == "__main__":
    n = [-1,0,1,2,-1,-4]
    print(threeSum(n))
