from typing import List
from itertools import combinations

class Solution:
    def maximizeSquareArea(
        self,
        m: int,
        n: int,
        hFences: List[int],
        vFences: List[int]
    ) -> int:

        maxL = 0
        seen = set()

        def findLen(fences: List[int], calM: bool):
            nonlocal maxL
            fences.sort()  # sorting = faster combos 🚀

            for x, y in combinations(fences, 2):
                length = y - x

                if calM:
                    if length > maxL and length in seen:
                        maxL = length
                else:
                    seen.add(length)

        hz, vz = len(hFences) + 2, len(vFences) + 2

        # swap if horizontal fences are more than vertical
        if hz > vz:
            return self.maximizeSquareArea(n, m, vFences, hFences)

        hFences += [1, m]
        vFences += [1, n]

        findLen(hFences, False)
        findLen(vFences, True)

        return -1 if maxL == 0 else (maxL * maxL) % (10**9 + 7)
