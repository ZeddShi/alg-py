# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
# 示例:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]


def searchRange(nums, target):
    left_idx = extreme_insertion_index(nums, target, True)
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]
    return [left_idx, extreme_insertion_index(nums, target, False) - 1]


def extreme_insertion_index(nums, target, left):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid+1

    return lo
