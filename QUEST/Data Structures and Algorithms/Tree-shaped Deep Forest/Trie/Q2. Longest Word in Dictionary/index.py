from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)   # faster lookups
        result = ""

        words.sort()

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break

            if valid:
                if len(word) > len(result):
                    result = word

        return result
