from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs[0])

        for i in range(n):
            column = []
            for word in strs:
                column.append(word[i])

            if column != sorted(column):
                cnt += 1

        return cnt
