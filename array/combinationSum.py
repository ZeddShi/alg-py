# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 

# combinationSum(nums, target, index) = combinationSum(nums, target - nums[index], index) + combinationSum(nums, target, index + 1)
def combinationSum(nums, target):
    ans = []
    def dfs(combine, target, index):
        if index == len(nums):
            return
        if target == 0:
            ans.append(combine)
            return
        dfs(combine, target, index + 1)
        if target - nums[index] >= 0:
            dfs(combine + [nums[index]], target - nums[index], index)
    dfs([], target, 0)
    return ans


if __name__ == "__main__":
    nums = [2,4,6,8,12,16]
    target = 4
    print(combinationSum(nums, target))
