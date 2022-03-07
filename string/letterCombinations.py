

def letterCombinations(digits: str):
    if not digits:
        return []
    digits_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    r = [' '] * len(digits)
    class BaseNode:
        def __init__(self, last, next, digits, pos):
            self.last = last
            self.next = next
            self.digits = digits
            self.pos = pos
            self.set_val(0)

        def set_next(self, next):
            self.next = next

        def plus(self):
            next_val = self.val + 1
            if next_val == self.digits:
                self.last.plus()
                self.set_val(0)
            else:
                self.set_val(next_val)

        def set_val(self, val):
            self.val = val
            if self.pos is not None:
                r[self.pos] = digits_map[digits[self.pos]][val]

    head = BaseNode(None, None, 2, None)
    tail = head
    for i, d in enumerate(list(digits)):
        d_ = 4 if d in ('7', '9') else 3
        n = BaseNode(tail, None, d_, i)
        # set last's next
        tail.next = n
        tail = n

    ans = []
    while head.val != 1:
        ans.append(''.join(r))
        tail.plus()
    return ans


# 更优解，深度优先DFS

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == "__main__":
    ds = '24'
    print(letterCombinations(ds))
