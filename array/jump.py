# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# [2, 3, 1, 1, 4]


def jump(nums):
    times = 0
    pos = 0
    n = len(nums)
    while True:
        if pos >= n - 1:
            break

        grid = nums[pos]
        if pos + grid >= n - 1:
            times += 1
            break

        max_jump = 0
        good_grid = 0
        while grid > 0:
            jump_grid = nums[pos + grid] + grid
            if jump_grid > max_jump:
                max_jump = jump_grid
                good_grid = grid
            grid -= 1

        pos += good_grid
        times += 1

    return times
