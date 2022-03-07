

def countS(s):
    cs = []
    for i, c in enumerate(s):
        if i == 0 or c != s[i - 1]:
            cs.append(1)
            cs.append(c)
            continue
        cs[-2] += 1
    return ''.join([str(x) for x in cs])

def countAndSay(n):
    if n == 1:
        return '1'
    ls = countAndSay(n - 1)
    return countS(ls)
