from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) - 1

        # Quick edge check
        if nums[0] == nums[n]:
            return nums[0]

        # Check nearby duplicates
        for i in range(n - 1):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]

        # Fallback (guaranteed to exist)
        return nums[0]
