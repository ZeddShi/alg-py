# 最长有效括号子串

# dp[i]表示以索引为i的字符结尾的最长有效括号子串，且满足s[i]必定为 ')'
# 状态转移方程:
# 当 s[i - 1] 为 '('，则 dp[i] = dp[i - 2] + 2
# 当 s[i - 1] 为 '）'，则需判断 s[i - dp[i - 1] - 1] 是否为 '('，与 s[i] 闭合形成有效括号，如果不是那么dp[i] = 0。
# 最终 dp[i] = dp[i - dp[i - 1] - 2] + 2 + dp[i - 1]
# 注意数组向前越界

def longestValidParentheses(s):
    ans = 0
    n = len(s)
    dp = [0] * n
    for i in range(n):
        if i == 0:
            continue
        if s[i] != ')':
            continue
        if s[i - 1] == '(':
            dp[i] = (dp[i - 2] + 2) if (i - 2) >= 0 else 2
        else:
            if not dp[i - 1]:  # 前面一个')'结尾不能构成有效字符串
                continue
            j = i - dp[i - 1] - 1
            if j < 0 or s[j] != '(':  # j不能越界
                continue

            # j必须大于0，不然越界
            dp [i] = (2 + dp[i - 1] + dp[i - dp[i - 1] - 2]) if j > 0 else (2 + dp[i - 1])
        if dp[i] > ans:
            ans = dp[i]
    return ans
