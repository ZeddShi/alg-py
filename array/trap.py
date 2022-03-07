# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


def traps(height):
    left_max = 0
    right_max = 0
    sum = 0
    left = 1
    right = len(height) - 2
    for _ in range(len(height) - 2):
        # 从左
        if height[left - 1] < height[right + 1]:
            left_max = max(height[left - 1], left_max)
            if left_max > height[left]:
                sum += left_max - height[left]
            left += 1
        else:
            right_max = max(height[right + 1], right_max)
            if right_max > height[right]:
                sum += right_max - height[right]
            right -= 1
    return sum
