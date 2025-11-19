from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)   # Faster lookups
        value = original

        while value in num_set:
            value *= 2

        return value

if __name__ == "__main__":
    nums = [5, 3, 6, 1, 12]
    original = 3
    sol = Solution()
    print(sol.findFinalValue(nums, original))  # Output: 24
