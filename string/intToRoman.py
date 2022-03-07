# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。


def intToRoman(self, num: int) -> str:
    ans = ''

    if num // 1000:
        ans += 'M' * (num // 1000)
        num -= num // 1000 * 1000

    if num // 900:
        ans += 'CM'
        num -= 900
    elif num // 500:
        ans += 'D'
        num -= 500

    if num // 400:
        ans += 'CD'
        num -= 400
    elif num // 100:
        ans += 'C' * (num // 100)
        num -= num // 100 * 100

    if num // 90:
        ans += 'XC'
        num -= 90
    elif num // 50:
        ans += 'L'
        num -= 50

    if num // 40:
        ans += 'XL'
        num -= 40
    elif num // 10:
        ans += 'X' * (num // 10)
        num -= num // 10 * 10

    if num // 9:
        ans += 'IX'
        num -= 9
    elif num // 5:
        ans += 'V'
        num -= 5

    if num // 4:
        ans += 'IV'
        num -= 4
    if num // 1:
        ans += 'I' * (num // 1)

    return ans
