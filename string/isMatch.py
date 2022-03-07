# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
        # 0 <= s.length <= 20
        # 0 <= p.length <= 30
        # s 可能为空，且只包含从 a-z 的小写字母。
        # p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
        # 保证每次出现字符 * 时，前面都匹配到有效的字符


# --------------
# *** 分析 ***
# 使用动态规划解决
# https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/


def isMatch(s, p):
    m, n = len(s), len(p)

    def matches(i: int, j: int) -> bool:
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]

    f = [[False] * (n + 1) for _ in range(m + 1)]
    f[0][0] = True
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                f[i][j] |= f[i][j - 2]
                if matches(i, j - 1):
                    f[i][j] |= f[i - 1][j]
            else:
                if matches(i, j):
                    f[i][j] |= f[i - 1][j - 1]
    return f[m][n]
