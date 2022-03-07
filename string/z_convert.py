# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。


def convert(s, numRows):
    if numRows <= 1:
        return s
    cycle = 2 * (numRows - 1)
    n = len(s)
    div_times = n // cycle
    times = div_times + 1 if (div_times * cycle < n) else div_times
    row = 1
    ans = ''
    while row <= numRows:
        for i in range(times):
            if ((row - 1) + (i * cycle)) < n:
                ans += s[(row - 1) + (i * cycle)]
            if row not in (1, numRows) and ((cycle - row + 1) + (i * cycle)) < n:
                ans += s[(cycle - row + 1) + (i * cycle)]
        row += 1
    return ans
