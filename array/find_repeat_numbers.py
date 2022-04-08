# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 22:26
# @Author  : ziggy
# @File    : find_repeat_numbers.py
def find_repeat_numbers(nums):
    repeats = set()
    for i in range(len(nums)):
        while nums[i] != i:
            tmp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            if tmp == nums[i]:
                repeats.add(tmp)
                break
            nums[i] = tmp
    return repeats


def find_repeat_numbers_once_with_no_modify(nums):
    """ 不修改数组的基础上找出一个重复的数字 """
    length = len(nums)
    right = length - 1
    left = 1
    while True:
        if right == left:
            return right

        middle = int((right + left) / 2)
        left_count = 0
        for num in nums:
            if left <= num <= middle:
                left_count += 1

        if left_count > middle - left + 1:
            right = middle
        else:
            left = middle + 1


if __name__ == '__main__':
    numbers = [1, 2, 1]
    print(find_repeat_numbers(numbers))
    print(find_repeat_numbers_once_with_no_modify(numbers))
