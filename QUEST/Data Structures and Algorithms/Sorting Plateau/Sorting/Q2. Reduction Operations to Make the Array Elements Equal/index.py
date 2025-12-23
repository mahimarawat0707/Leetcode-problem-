from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)

        operations = 0
        prev_unique = nums[0]

        for i in range(1, len(nums)):
            # Skip if the number is the same as previous
            if nums[i] == prev_unique:
                continue

            # If a smaller number is found, add operations
            if nums[i] < prev_unique:
                operations += i

            # Update previous unique number
            prev_unique = nums[i]

        return operations
