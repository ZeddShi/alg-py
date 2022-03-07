# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的括号组合。


def generateParenthesis(n: int):
    ans = []
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left+1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right+1)
            S.pop()

    ts = []
    backtrack(ts, 0, 0)
    return ans


if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))
