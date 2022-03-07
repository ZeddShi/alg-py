# 寻找2个正序数组的中位数

# 当 m+n 为奇数 中位数为 (m+n) // 2 + 1
# 当 m+n 为偶数，中位数为 (m+n) // 2 和 (m+n) // 2 + 1这两个数的平均数

def findMedianSortedArrays(nums1, nums2):
    def getKelement(k):
        index1, index2 = 0, 0
        while True:
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            comp = k // 2 - 1
            real_index1 = min(index1 + comp, m - 1)
            real_index2 = min(index2 + comp, n - 1)
            if nums1[real_index1] <= nums2[real_index2]:
                k = k - (real_index1 - index1 + 1)
                index1 = real_index1 + 1
            else:
                k = k - (real_index2 - index2 + 1)
                index2 = real_index2 + 1

    m, n = len(nums1), len(nums2)
    if m == n == 0:
        return 0
    if (m + n) % 2 > 0:
        return getKelement((m + n) // 2 + 1)
    else:
        return (getKelement((m + n) // 2) + getKelement((m + n) // 2 + 1)) / 2


if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    r = findMedianSortedArrays(a, b)
    print(r)
