from typing import List

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)

        for i in range(1, L):
            for j in range(i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break

        return N
