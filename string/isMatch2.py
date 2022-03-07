# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。

# 两个字符串完全匹配才算匹配成功。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。


def isMatch(s, p):
    ls = len(s)
    lp = len(p)
    dp = [[False] * (lp + 1) for _ in range(ls + 1)]
    dp[0][0] = True
    for i in range(ls + 1):
        for j in range(1, lp + 1):
            if i == 0:
                dp[i][j] = dp[i][j - 1] and (p[j - 1] == '*')
                continue
            if s[i - 1] == p[j- 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
                continue
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[ls][lp]


if __name__ == "__main__":
    s = "adceb"
    p = "*a*b"
    print(isMatch(s, p))