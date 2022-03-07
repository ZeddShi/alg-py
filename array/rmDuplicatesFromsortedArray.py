

def removeDuplicates(nums):
    if not nums:
        return 0
    p1 = p2 = 0
    while p2 < len(nums):
        if nums[p1] != nums[p2]:
            p1 += 1
            nums[p1] = nums[p2]
        p2 += 1
    return p1 + 1