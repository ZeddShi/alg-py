# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 22:19
# @Author  : ziggy
# @File    : 720.py
class Solution:
    def longestWord(self, words) -> str:
        len_list = []
        for i in range(30):
            len_list.append([])
        min_len = None
        for word in words:
            length = len(word)
            if min_len is None:
                min_len = length
            else:
                if min_len > length:
                    min_len = length
            len_list[length - 1].append(word)

        if min_len is None:
            return ''

        def is_ok(index, target):
            new_target = target[:-1]
            new_index = index - 1
            if index >= 1:
                l = len_list[new_index]
                if new_target in l:
                    return is_ok(new_index, new_target)
                else:
                    return False
            else:
                return True

        result = None
        index = 29
        while True:
            if index < min_len - 1:
                break
            for word in len_list[index]:
                ok = is_ok(index, word)
                if ok:
                    if result is None:
                        result = word
                    else:
                        if result > word:
                            result = word

            if result:
                break

            index -= 1
        return result or ''

    def longestWord1(self, words):
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        print(words)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest


if __name__ == '__main__':
    s = Solution()
    s.longestWord1(["wo","wor","worl","world"])