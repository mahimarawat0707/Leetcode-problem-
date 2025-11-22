from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for x in nums:
            if x % 3 != 0:
                ops += 1
        return ops


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print("Minimum operations:", sol.minimumOperations(nums))
