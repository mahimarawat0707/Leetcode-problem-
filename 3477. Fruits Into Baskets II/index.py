from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = n

        for fruit in fruits:
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    unplaced -= 1
                    break

        return unplaced

if __name__ == "__main__":
    fruits = [4, 2, 3]
    baskets = [2, 3, 5]
    solution = Solution()
    print("Number of unplaced fruits:", solution.numOfUnplacedFruits(fruits, baskets))
