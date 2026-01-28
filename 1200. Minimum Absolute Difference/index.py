from typing import List

class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        n = len(A)
        minDiff = 2_000_001
        res = []

        for i in range(1, n):
            diff = A[i] - A[i - 1]

            if diff < minDiff:
                minDiff = diff
                res = [[A[i - 1], A[i]]]
            elif diff == minDiff:
                res.append([A[i - 1], A[i]])

        return res
