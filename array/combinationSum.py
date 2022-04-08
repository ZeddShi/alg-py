# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# candidates 中的数字可以无限制重复被选取。

# combinationSum(nums, target, index) =
# combinationSum(nums, target - nums[index], index) +
# combinationSum(nums, target, index + 1)
def combination_sum(numbers, target_number):
    ans = []

    def dfs(combine, remain, index):
        if index == len(numbers):
            return
        if remain == 0:
            ans.append(combine)
            return
        dfs(combine, remain, index + 1)
        if remain - numbers[index] >= 0:
            dfs(combine + [numbers[index]], remain - numbers[index], index)

    dfs([], target_number, 0)
    return ans


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 12, 16]
    target = 4
    print(combination_sum(nums, target))
