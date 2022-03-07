# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 


def combinationSumNoRepeat(candidates, target):
    candidate_pairs = get_candidate_pairs(candidates)
    ans = []
    def dfs(combines, pos, rest):
        if rest == 0:
            ans.append(combines)
            return
        if pos >= len(candidate_pairs):
            return
        if candidate_pairs[pos][0] > rest:
            return
        dfs(combines, pos + 1, rest)  # 不选
        for i in range(1, candidate_pairs[pos][1] + 1):
            if rest >= i * candidate_pairs[pos][0]:
                dfs(combines + [candidate_pairs[pos][0]] * i, pos + 1, rest - i * candidate_pairs[pos][0])
    dfs([], 0, target)
    return ans


def get_candidate_pairs(candidates):
    candidates.sort()
    candidate_pairs = []
    for can in candidates:
        if candidate_pairs and candidate_pairs[-1][0] == can:
            candidate_pairs[-1][1] += 1
        else:
            candidate_pairs.append([can, 1])
    return candidate_pairs


if __name__ == "__main__":
    # nums = [2,2,1,3,4,6,7,2,1,4,2,3,4,5,1,6,7,8,8]
    nums = [4,4,4]
    print(combinationSumNoRepeat(nums, 4))
    # print(get_candidate_pairs(nums))
