# 最接近的三数之和

def threeSumClosest(nums, target):
    nums.sort()
    closest_num = None
    distance = None

    l = len(nums)
    for i in range(l - 2):
        index_l = i + 1
        index_r = l - 1
        while True:
            if index_l == index_r:
                break
            aplusbplusc = nums[i] + nums[index_l] + nums[index_r]

            if aplusbplusc > target:
                index_r -= 1
            elif aplusbplusc < target:
                index_l += 1
            else:
                return aplusbplusc

            tmp_distance = abs(aplusbplusc - target)
            if distance is None or distance > tmp_distance:
                closest_num = aplusbplusc
                distance = tmp_distance

    return closest_num


if __name__ == "__main__":
    target = 1
    nums = [-1,2,1,-4]
    sorted_nums = [-4,-1,1,2]
    print(threeSumClosest(nums, target))
