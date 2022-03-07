# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。


# 方法: DP
# 状态方程:
# 当字符串长度大于 2 时: dp[i,j] = dp[i+1,j-1] & (S[i] == S[j])
# 当字符串长度等于 1 时: dp[i,j] = true
# 当字符串长度等于 2 时: dp[i,j] = (S[i] == S[j])
def longestPalindromeDp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ''
    for l in range(n):
        for i in range(n):
            j = i + l
            if j >= n:
                break
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j + 1]
    return ans
