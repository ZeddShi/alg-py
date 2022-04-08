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


if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5, 3, 0, 3, 4, 6, 8, 9, 7]
    print(find_repeat_numbers(numbers))
