from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell
            idx = bisect_left(potions, min_potion)
            result.append(n - idx)

        return result

if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    sol = Solution()
    print(sol.successfulPairs(spells, potions, success))
