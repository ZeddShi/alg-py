
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

def firstMissingPositive(nums):
    pos_dict = {pos: 1 for pos in nums if pos > 0}
    ans = 1
    while True:
        if pos_dict.get(ans):
            ans += 1
        else:
            break
    return ans


def firstMissingPositiveReplace(nums):
    mark = object()
    empty = object()
    for i in range(len(nums)):
        