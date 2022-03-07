
# 搜索旋转排序数组某个值
# 如: [4,5,6,7,0,1,2]

def search(self, nums, target):
    if not nums:
        return -1

    start_index = 0
    end_index = len(nums) - 1

    while True:
        if start_index == end_index:
            if nums[start_index] == target:
                return start_index
            return -1

        if (start_index + 1) == end_index:
            if nums[start_index] == target:
                return start_index
            elif nums[end_index] == target:
                return end_index
            else:
                return -1

        middle_index = (start_index + end_index) // 2
        if nums[start_index] < nums[middle_index]:
            if nums[start_index] <= target <= nums[middle_index]:
                end_index = middle_index
            else:
                start_index = middle_index + 1
        else:
            if nums[middle_index] <= target <= nums[end_index]:
                start_index = middle_index
            else:
                end_index = middle_index - 1
