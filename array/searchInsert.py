# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。


def searchInsert(nums, target):
    if not nums:
        return 0

    start = 0
    end = len(nums)

    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start
