

def nextPermutation(nums):
    index_1 = None
    for i in range(len(nums))[::-1]:
        if i == (len(nums) - 1):
            continue
        if nums[i] < nums[i + 1]:
            index_1 = i
            break
    if index_1 is None:
        nums.sort()
        return

    index_2 = index_1 + 1
    for i in range(index_2, len(nums)):
        if nums[index_1] < nums[i] <= nums[index_2]:
            index_2 = i

    tmp = nums[index_1]
    nums[index_1] = nums[index_2]
    nums[index_2] = tmp

    p1 = index_1 + 1
    p2 = len(nums) - 1
    while p1 < p2:
        tmp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = tmp
        p1 += 1
        p2 -= 1
    return


if __name__ == "__main__":
    l = [2,3,1,3,3]
    r = nextPermutation(l)
    print(l)