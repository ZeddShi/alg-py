# 盛最多水的容器


def maxArea(height):
    index1, index2 = 0, len(height) - 1
    max_val = 0
    while True:
        if index1 == index2:
            break

        area = min(height[index1], height[index2]) * (index2 - index1)
        if area > max_val:
            max_val = area
        if height[index1] <= height[index2]:
            index1 += 1
        else:
            index2 -= 1 
    return max_val


if __name__ == "__main__":
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    r = maxArea(a) 
    print(r)
