# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

def longest_unrepeat_substring(s):
    if not s:
        return 0
    n = len(s)
    p = 0
    tmp_dict = {}
    max_len = 0
    for i in range(n):
        while p < n and not tmp_dict.get(s[p]):
            tmp_dict[s[p]] = 1
            p += 1
        del tmp_dict[s[i]]
        max_len = max(max_len, p - i)
    return max_len
